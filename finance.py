from agno.agent import Agent
from agno.models.groq import Groq  


from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv

from agno.tools.yfinance import YFinanceTools



load_dotenv()  # Load environment variables from .env file


def build_agent():
    agent = Agent(
        model=Groq(id="qwen/qwen3-32b"), #lama-3.3-70b-versatile PROBELM with duckduckgo.
        markdown=True,
        tools=[DuckDuckGoTools(), YFinanceTools()],
     #   instructions="You are a expert and helpful assistant that provides concise and informative responses to user queries.",
        add_datetime_to_context=True,
        debug_mode=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."]

    )
    return agent


groq_agent = build_agent()
# Print the response in the terminal
groq_agent.print_response("use given tools whenever possible and share the NVDA stock price, analyst recommendations, and stock fundamentals TODAY?")