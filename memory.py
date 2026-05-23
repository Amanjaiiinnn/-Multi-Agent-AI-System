# from agno.team import Team
from agno.agent import Agent
from agno.models.groq import Groq
# from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
load_dotenv()  


from agno.db.sqlite import SqliteDb

# Setup your database
db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    agent = Agent(
        db=db,
        update_memory_on_run=True, # This enables Memory for the Agent
        add_history_to_context=True,
        model=Groq(id="qwen/qwen3-32b"), #lama-3.3-70b-versatile PROBELM with duckduckgo.
        markdown=True,
    )
    return agent


groq_agent = build_agent()

groq_agent.print_response("what is the capital of colombia?")
groq_agent.print_response("what is thebest time to visit it?")

