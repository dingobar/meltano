import yaml
import fnmatch
from typing import Dict, Union
from collections import namedtuple
from enum import Enum

from meltano.core.behavior.hookable import HookObject


class YAMLEnum(str, Enum):
    def __str__(self):
        return self.value

    @staticmethod
    def yaml_representer(dumper, obj):
        return dumper.represent_scalar("tag:yaml.org,2002:str", str(obj))


yaml.add_multi_representer(YAMLEnum, YAMLEnum.yaml_representer)


class PluginType(YAMLEnum):
    EXTRACTORS = "extractors"
    LOADERS = "loaders"
    MODELS = "models"
    TRANSFORMERS = "transformers"
    TRANSFORMS = "transforms"
    ORCHESTRATORS = "orchestrators"
    ALL = "all"

    def __str__(self):
        return self.value

    @property
    def cli_command(self):
        """Makes it singular for `meltano add PLUGIN_TYPE`"""
        if self is self.__class__.ALL:
            raise NotImplemented()

        return self.value[:-1]

    @classmethod
    def value_exists(cls, value):
        return value in cls._value2member_map_


class PluginRef:
    def __init__(self, plugin_type: Union[str, PluginType], name: str):
        self.type = (
            plugin_type
            if isinstance(plugin_type, PluginType)
            else PluginType(plugin_type)
        )
        self.name = name

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

    def __hash__(self):
        return hash((self.namespace, self.name))


class PluginInstall(HookObject, PluginRef):
    def __init__(
        self,
        plugin_type: PluginType,
        name: str,
        pip_url: str,
        select=set(),
        config={},
        **extras
    ):
        super().__init__(plugin_type, name)

        self.config = config
        self.pip_url = pip_url
        self._select = set(select)
        self._extras = extras or {}

    def canonical(self):
        canonical = {"name": self.name, "pip_url": self.pip_url, **self._extras}

        if self._select:
            canonical.update({"select": list(self._select)})

        if self.config:
            canonical.update({"config": self.config})

        return canonical

    @property
    def executable(self):
        return self._extras.get("executable", self.name)

    @property
    def select(self):
        return self._select or {"*.*"}

    @select.setter
    def select(self, patterns):
        self._select = set(patterns)

    def invoker(self, project, *args, **kwargs):
        "Override to have a specialize PluginInvoker class"
        pass

    def exec_args(self, files: Dict):
        return []

    @property
    def config_files(self):
        """Return a list of stubbed files created for this plugin."""
        return dict()

    @property
    def output_files(self):
        return dict()

    def cwd(self, project):
        return project.root

    def add_select_filter(self, filter: str):
        self._select.add(filter)


class Plugin(PluginRef):
    """
    Args:
    name: The unique name for the installed plugin
    pip_url: The pip-compatible installation URI, like `git+https://…` or `-e /path/to/pkg`
    executable: The plugin executable name (default: <name>)
    """

    def __init__(
        self,
        plugin_type: PluginType,
        name: str,
        namespace: str,
        pip_url: str,
        settings: list = [],
        docs=None,
        **extras
    ):
        super().__init__(plugin_type, name)

        self.namespace = namespace
        self.pip_url = pip_url
        self.settings = settings
        self.docs = docs
        self._extras = extras or {}

    def as_installed(self) -> PluginInstall:
        return PluginInstall(self.type, self.name, self.pip_url, **self._extras)
