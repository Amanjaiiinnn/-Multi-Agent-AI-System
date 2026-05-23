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

user_id="abc@gmail.com"
# groq_agent.print_response("what is the capital of Argentina?", user_id=user_id) 
# groq_agent.print_response("what is the best time to visit it?", user_id=user_id)


groq_agent.print_response("i am abc and i am a software engineer", user_id=user_id) 
groq_agent.print_response("who am i?", user_id=user_id)

memories = groq_agent.get_user_memories(user_id=user_id)

print ("memories for user_id")
print(memories)

