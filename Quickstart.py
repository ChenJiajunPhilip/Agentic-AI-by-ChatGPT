#Python
from agentic_ai.agents import Agent
from agentic_ai.memory import Memory
from agentic_ai.tools import WebSearchTool

agent = Agent(
    name="ResearcherBot",
    role="Academic research assistant",
    tools=[WebSearchTool()],
    memory=Memory()
)

agent.run("Summarize the latest AI papers from arXiv.")
