from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool

import os
import yaml



@CrewBase
class BibleAgent():
    """BibleProject crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def bible_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['bible_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def commentary_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['commentary_researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()] # Using SerperDevTool for web search capabilities
        )
    
    @agent
    def seasoned_pastor(self) -> Agent:
        return Agent(
            config=self.agents_config['seasoned_pastor'], # type: ignore[index]
            verbose=True
        )

    @task
    def search_verses(self) -> Task:
        return Task(
            config=self.tasks_config['search_verses'],
            agent=self.bible_agent(),
            expected_output="A list of Bible verses from different versions that match the user's query."
        )

    @task
    def fetch_commentary(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_commentary'],
            agent=self.commentary_researcher(),
            expected_output="A collection of commentary excerpts and explanations for the provided Bible passage or topic."
        )
    
    @task
    def pastoral_summary(self) -> Task:
        return Task(
            config=self.tasks_config['pastoral_summary'],
            agent=self.seasoned_pastor(),
            expected_output="A concise, spiritually insightful, and contextually relevant summary of the provided verses and commentary.",
            context=[self.search_verses(), self.fetch_commentary()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BibleProject crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
