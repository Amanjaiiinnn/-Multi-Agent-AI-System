from agno.team import Team
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv
load_dotenv()

import os

eng_agent = Agent(
    name="English Agent",
    role="You answer questions in English only"
)

chn_agent = Agent(
    name="Chinese Agent",
    role="You answer questions in Chinese only"
)

hin_agent = Agent(
    name="Hindi Agent",
    role="You answer questions in Hindi only"
)

team = Team(
    name="Answer and Translation Team",
    members=[eng_agent, chn_agent, hin_agent],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    tools=[DuckDuckGoTools()],
    add_datetime_to_context=True,
    instructions="all members agents must respond to answer the query."
)

response = team.run("Provide the answer in all three languages: What is the capital of France?")
print(response.content)

# print(response)

# print(response.content)          # Final answer
# print(response.messages)         # Full conversation
# print(response.metrics)          # Token usage
# print(response.status)           # COMPLETED
# print(response.member_responses) # Responses from agents