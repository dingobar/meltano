from flask import url_for

from meltano.api.models.embed_token import EmbedToken
from meltano.core.project import Project
from meltano.core.schedule_service import ScheduleService

from .sql_helper import SqlHelper


class ReportsHelper:
    VERSION = "1.0.0"

    def create_embed_snippet(self, session, name):
        try:
            embed_token = session.query(EmbedToken).filter_by(resource_id=name).one()
            is_cached = True
            embed_token = EmbedToken(resource_id=name)
            session.add(embed_token)
            is_cached = False
        finally:
            session.commit()

        embed_url = url_for("root.embed", token=embed_token.token, _external=True)
        return {
            "is_cached": is_cached,
            "url": embed_url,
            "snippet": f"<iframe src='{embed_url}' />",
        }

    def get_embed(self, session, token):
        return session.query(EmbedToken).filter_by(token=token).one()

    def get_report_with_query_results(self, report):
        project = Project.find()
        schedule_service = ScheduleService(project)
        sql_helper = SqlHelper()
        report_with_query_results = self.update_report_with_query_results(
            report, schedule_service, sql_helper
        )

        return report_with_query_results

    def update_report_with_query_results(self, report, schedule_service, sql_helper):
        m5oc = sql_helper.get_m5oc_topic(report["namespace"], report["model"])
        design = m5oc.design(report["design"])
        schedule = schedule_service.find_namespace_schedule(
            m5oc.content["plugin_namespace"]
        )

        sql_dict = sql_helper.get_sql(design, report["query_payload"])
        outgoing_sql = sql_dict["sql"]
        aggregates = sql_dict["aggregates"]

        report["query_results"] = sql_helper.get_query_results(
            schedule.loader, outgoing_sql
        )
        report["query_result_aggregates"] = aggregates

        return report
