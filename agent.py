from agno.agent import Agent
from agno.models.groq import Groq  


from agno.tools.duckduckgo import DuckDuckGoTools


from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file
import os



def build_agent():
    agent = Agent(
        model=Groq(id="qwen/qwen3-32b"), #lama-3.3-70b-versatile PROBELM with duckduckgo.
        markdown=True,
        tools=[DuckDuckGoTools()],
        instructions="You are a expert and helpful assistant that provides concise and informative responses to user queries.",
        add_datetime_to_context=True
    )
    return agent


groq_agent = build_agent()
# Print the response in the terminal
groq_agent.print_response("is it safe to travel to iran TODAY?")