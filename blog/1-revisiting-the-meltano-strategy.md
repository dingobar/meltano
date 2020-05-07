# Revisiting the Meltano strategy, direction, and focus: a return to our roots

This is part 1 of a 2 part series. If you've been following the Meltano project for a while or would like to have some historical context, start here. If you're new to the Meltano project and mostly interested in what's next, start with [part 2](#).

---

The Meltano team and project were [founded](https://about.gitlab.com/blog/2018/08/01/hey-data-teams-we-are-working-on-a-tool-just-for-you/) inside GitLab about 2 years ago to serve the [GitLab Data Team](https://about.gitlab.com/handbook/business-ops/data-team/). The goal was to build a complete solution for data teams: an open source tool for the entire data lifecycle from extraction to dashboarding, that would allow data engineers, analytics engineers, analysts, data scientists, and business end-users looking for insights to come together and collaborate within the context of a single version controlled Meltano project.

At its core, the project would specify a collection of plugins, one or more for every stage of the data lifecycle, that would describe how data should be extracted, loaded, and transformed, how pipelines should be orchestrated, and how the data should ultimately be modeled for analysis. The Meltano tool would be used in the context of such a project, install and manage the plugins, take care of tying it all together, and offer a visual interface for point-and-click analysis and report and dashboard creation.

Plugins for common data sources and use cases could be shared using Git and collaborated on by the community, to be added to any team's Meltano project with just a few keystrokes, while team-specific plugins could be implemented and stored right inside the Meltano project repository. As a result, anyone with access to the project (or a set of community-built plugins) would be able to go from data to dashboard in a matter of minutes. Pretty intriguing, right?

For a while, the Meltano team was making great process through its close collaboration with the GitLab Data Team, until it became clear that GitLab's and the Data Team's needs were growing at a pace that the Meltano team would not be able to keep up with, at which point the decision was made for the Data Team to switch to a more traditional stack, so that its results would not be adversely affected by its dependence on a tool that was only just getting off the ground.

That didn't deter the Meltano team, however, who continued to work to realize the end-to-end vision. Because the different users involved in the different stages of the journey from extraction to analysis have different needs and skills, and since we could see Meltano bringing value to [data teams with engineers on staff, as well as those without](https://about.gitlab.com/blog/2018/10/08/meltano-functional-group-update-post/), the decision was made to develop the Meltano CLI and UI in parallel, so that Meltano could serve both technical and non-technical users.

Since every next stage of the data lifecycle depends on the result of the one that came before it (we're talking about data pipelines after all), our prioritization process had a cyclical nature. We would start with the first stage (extraction and loading), and keep iterating on Meltano's capabilities in that area right up to the point where they would unlock further improvements in the next stage (transformation). Then we'd move on and direct our focus there, until it once again became time to move on to the next stage (orchestration), and so on. Once the final stage (analysis) was reached, we would go all the way back to the first stage and the journey through the stages would start again.

In October 2019, we released [Meltano Version 1](https://meltano.com/blog/2019/10/07/meltano-graduates-to-version-1-0/), which marked the completion of one such journey through the stages, and the realization of the end-to-end vision. Assuming a data warehouse or simple Postgres database had already been set up, you could now install Meltano on your local machine, initialize a project, spin up the web-based UI, install a data source (with would add the relevant extractor, loader, transform, and model plugins to your project), enter your connection details, hit the Connect button, and find yourself looking at reports and dashboards visualizing your data a few minutes later. A most impressive demo, if you ask me!

In spite of our aspirations, though, we had not yet managed to attract an open source community to build this tool (and its plugins!) with us, and while there had been a lot of interest in the project from the beginning, no data teams were jumping at the chance to replace their existing stack with Meltano yet. While we had certainly proven the concept, we had not yet gotten it to a place where the value it could bring was significant or obvious enough that new or existing data teams would actually consider it an alternative to more traditional stacks.

To address that, we decided to focus on the user who ultimately gets the most value out of any data pipeline: the end-user who consumes the reports, has an insight, and then uses it to improve they way their business is run. Specifically, [we picked a persona](https://meltano.com/blog/2019/11/11/clarifying-the-target-persona-for-meltano/) for whom the no-coding-needed batteries-included end-to-end nature of Meltano would be significant selling point: the non-technical startup founder. They may not have a data stack at all yet, but are very likely to be using a bunch of common SaaS tools to run their business, which means a lot of data is being collected that they could (and should!) be learning from.

What this meant is going all-in on turning Meltano into an UI-first analytics and dashboarding tool with built-in support for those data sources most commonly used at early startups, that could be connected with a click and would come with a set of default dashboards and reports to save the user having to build these all from scratch.

Since this user could not be expected to be comfortable installing a Python package or setting up a Postgres database, we decided to make installation as easy as clicking a button, by offering [hosted Meltano instances](https://meltano.com/blog/2019/11/26/were-going-saas-let-us-set-you-up-with-free-hosted-dashboards/).

These users could also not be expected to implement extractors, transformations or models, so we took on this burden ourselves. We were, after all, attempting to prove the value that Meltano could bring by showing that _assuming that plugins exist_, it is really powerful to have a single tool take care of everything from extraction to analysis, so that an end-user can forget about the nitty gritty details and simply go straight from connecting their data source to viewing a dashboard.

In doing so, we effectively put ourselves into the shoes of the data and analytics engineers on a data team who would be tasked with maintaining and deploying a Meltano project and writing Meltano plugins (extractors, loaders, transformations, and models), while the end-user took the role of, well, the end-user look for insights. This directly exposed us to all of the challenges one might face when using Meltano in one of these roles, and we were able to make many improvements to the tooling because of it.

Working closely with users of Meltano's analysis functionality also let us iterate heavily on the UI and cater it better to people not already intimately familiar with data pipelines. We wrapped the Extract, Load, and Transform concepts up into "Connections", and introduced a new "dashboard" plugin type that allowed us to build default reports and dashboards that would be installed automatically along with a data source's extractor, transformations, and models.

This past March, about 6 months into this adventure, we found ourselves in a much better place with Meltano Analyze, and were about to embark on a new effort to not just ship transformations, models and default dashboards and reports for individual data sources, but for [combinations of data sources](https://gitlab.com/meltano/meltano/-/issues/518) as well, since it's from the combinations of different but related data sets that the most interesting insights will often arise. Meltano already supported this in principle, meaning that more technical users setting up Meltano and building plugins themselves could figure it out, but the challenge would be in allowing these connections to be made through the UI, and offering our non-technical end-user out-of-the-box support for all reasonable combinations of data sources that they had connected.

Since the value that hosted Meltano could bring was a function of both the actual functionality the Meltano tool offered as the extent of our out-of-the-box data source support, improving the experience for our non-technical end-users would come down to us taking on the significant burden of developing and maintaining all of the plugins they would ever use, ourselves.

By then, the 6 month experiment had certainly proven the point that "Meltano can bring significant value to non-technical people as an integrated tool to go from data to dashboard", and from that perspective should be seen as a great success. It had also made us realize, however, that as a way of demonstrating the value of Meltano to the data teams that might one day adopt it and offer its analytics interface to _their_ non-technical end-users, the approach of simply compensating for its current lack of plugin support by trying to implement them all ourselves was not going to scale.

We had built a pretty useful hosted analytics tool for startup founders looking to learn from their sales funnel performance, and we had learned a lot along the way, but continuing further on this path would not bring us closer to our overarching goal of building an end-to-end tool for all data teams and all use cases.

So what's next, then?

If the non-technical user experience of Meltano will only ever be as good as the quantity and quality of its plugins, we need to get more people involved in writing them, so it's time to pivot back and return our focus to open source, the self-hosted experience, and the technical end-user!

But wasn't that exactly what we had been doing for the first year and a half of Meltano's life, while we were working towards Version 1, and before we decided to pivot to the startup founder persona?

What we had been doing then had worked in at least one significant way: we managed to build an actual end-to-end tool for the data lifecycle! But while that end-to-end vision had gotten many excited, that by itself did not ultimately turn out to be enough to attract a community of active users and contributors to Meltano and its plugins.

So if we wanted to do better on that front this time around, we would have to come up with a new strategy.

To figure out what that could look like, and where Meltano might go from here, I've spent much of the last few weeks diving deep into and talking with various people (inside and outside of GitLab) about:

1. Meltano's history: what was the original vision, how was it presented, what resonated with people, what got some of them to contribute, and what got most of them to ultimately lose interest?
2. The state of the industry: how do data teams currently solve these problems, what tools do they use for data integration, analysis and everything in between, and how do these stack up against each other?
3. Meltano's opportunity: where does it fit in the space, and where can it bring the most value, both in terms of what it can actually already do today, and what it might be able to do tomorrow?

The most significant conclusion came pretty quickly: As an open source project, Meltano's scope is simply too broad.

At first glance, it may seem like a broader scope would be a good thing: if the project intends to solve more different problems for more different people, it'll get more people excited, and therefore more people will contribute! Right?

If only it were that simple. Excited people do not always convert into users and contributors, and there's a difference between being excited about a vision and the prospect of one day getting to use the tool, and being excited about contributing to actually make that vision a reality.

To get an individual to invest their time and energy in anything, including an open source project, they need to feel like they'll get something out of it. The reward doesn't need to be monetary, and it doesn't need to arrive right away, but no one does anything for no reason at all. In open source, the reward is typically a solution to a problem an individual is facing, and the investment is them making changes to a project that _almost_ solves their problem to get it closer to _actually_ solving their problem, even if it may still require additional changes after that. Many people contribute to open source projects for ideological reasons or simply because they enjoy it, not because they're facing a specific problem right at that moment, but they still wouldn't pick a project that they could never see themselves benefiting from.

Of course, how much you'd be willing to invest depends on the size of the reward (how much you care about solving the problem), the size of the investment (the amount of changes you'd need to make to the project to have a meaningful impact), your confidence that the investment would actually eventually lead to the reward (how close the project already is to solving the problem, and whether your changes would get it all the way there or if future contributions would still be necessary), and how long you could expect it to take for the reward to actually arrive once you've put in your investment.

And that's where a broad and ambitious scope can hurt: if you asked an entire data team to evaluate whether contributing to Meltano would be a good investment, they might say yes (as the GitLab Data Team did!), because they can look at the vision and see how valuable Meltano could be to their team in the future, even if it would still take a while for that vision to actually be realized and for the investment to pay off. 

If you separated the team and asked the data engineer(s), analytics engineer(s), and analyst(s) seperately, though, chances are that none of them would be motivated to start contributing at all. The project doesn't seem to solve a problem they are personally facing, any hypothetical value they would get out of the end-to-end vision seems very far away and dependent on unclear external factors like "would my company ever actually consider migrating to this tool?", and they would need to contribute a significant amount of changes before they would feel like they are actually having a meaningful impact on moving the needle in the direction of that final reward.

Hence, Meltano's scope is simply too broad to attract open source contributors in any significant numbers. So if we can't go straight for end-to-end, where _do_ we start?

The plugins that will make Meltano's end-to-end vision come true for any given data source will have to be written in order by people with different roles and skillsets, so if we want to make that vision a reality _eventually_, we have to start with data engineers writing extractors and loaders, so that _later_ analytics engineers can write transformations and models, so that _after that_ data analysts and business end-users can use the models to create reports and dashboards.

The hope is that if we build a community around open source data integration and get data engineers to collaborate on extractors and loaders, analytics engineers who come across the project will eventually be motivated to also write transformations because dbt is supported out of the box. Once Meltano ships with extractors and transformations for various data sources, analytics engineers and analysts would also be motivated to give its built-in analytics functionality a try and write some models, and once those are done for a handful of data sources, we're ready for the non-technical end-user who we won't need to contribute at all, because all of the plugins will have been written already.

All of this is to say that while the end-to-end vision of Meltano is still alive as a long-term aspiration, we cannot afford to be distracted by it in the short-to-medium term.

Instead, we will go all-in on positioning Meltano as an open source self-hosted platform for running data integration and transformation (ELT) pipelines, and will treat the end-to-end vision just like early contributors to GitLab would have treated the "one tool for the entire DevOps cycle" vision, if it had been suggested at the time.

The goal is to turn Meltano into a true open source alternative to existing proprietary hosted solutions like Fivetran, in terms of ease of use, reliability, and quantity and quality of available data source connectors, since without it, an open source tool for the entire data lifecycle can never exist.

And everything that's old is new again, since GitLab Staff Data Engineer Taylor Murphy suggested pretty much exactly this [not too long after the project was originally founded](https://gitlab.com/meltano/meltano/-/issues/94#note_103950871):

> From my perspective, given what Meltano can be, the real opportunities for building a community around Meltano are initially around Extractors and Loaders and eventually Meltano Analyze. dbt already has quite a community and working well with them would be a quick way to get more people excited.

With everything I know now, I couldn't agree more.

To learn why the opportunity to build an open source platform for data integration and transformation (ELT) pipelines gets us just as excited as we have been about the end-to-end vision in the past, check out part 2:

[**Why we are building an open source data integration platform**](#)