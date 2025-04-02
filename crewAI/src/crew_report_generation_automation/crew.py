from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class CrewReportGenerationAutomationCrew():
    """CrewReportGenerationAutomation crew"""

    @agent
    def internet_forager(self) -> Agent:
        return Agent(
            config=self.agents_config['internet_forager'],
            tools=[WebsiteSearchTool()],
        )

    @agent
    def content_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['content_extractor'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def content_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_summarizer'],
            tools=[],
        )

    @agent
    def report_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config['report_compiler'],
            tools=[],
        )


    @task
    def web_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_search_task'],
            tools=[WebsiteSearchTool()],
        )

    @task
    def content_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_extraction_task'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def content_summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_summarization_task'],
            tools=[],
        )

    @task
    def report_compilation_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_compilation_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CrewReportGenerationAutomation crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
