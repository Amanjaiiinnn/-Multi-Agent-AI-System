from textwrap import dedent

from agno.agent import Agent
from agno.models.groq import Groq  
from agno.tools.youtube import YouTubeTools

from dotenv import load_dotenv
load_dotenv()

youtube_agent = Agent(
    name="YouTube Agent",
    model=Groq(id="qwen/qwen3-32b"),  # Use a powerful model for detailed analysis
    tools=[YouTubeTools()],
    instructions=dedent("""\Analyze YouTube videos and provide:
                            1. Overview
                            2 . Important timestamps
                            3. Key learning points
                            4. Topic progression

                            Keep responses concise and accurate.        
    """),
    add_datetime_to_context=True,
    markdown=True,
)

# Example usage with different types of videos
youtube_agent.print_response(
    "Analyze this video: https://www.youtube.com/watch?v=96jN2OCOfLs",
    stream=True,
)

# More example prompts to explore:
# """
# Tutorial Analysis:
# 1. "Break down this Python tutorial with focus on code examples"
# 2. "Create a learning path from this web development course"
# 3. "Extract all practical exercises from this programming guide"
# 4. "Identify key concepts and implementation examples"

# Educational Content:
# 1. "Create a study guide with timestamps for this math lecture"
# 2. "Extract main theories and examples from this science video"
# 3. "Break down this historical documentary into key events"
# 4. "Summarize the main arguments in this academic presentation"

# Tech Reviews:
# 1. "List all product features mentioned with timestamps"
# 2. "Compare pros and cons discussed in this review"
# 3. "Extract technical specifications and benchmarks"
# 4. "Identify key comparison points and conclusions"

# Creative Content:
# 1. "Break down the techniques shown in this art tutorial"
# 2. "Create a timeline of project steps in this DIY video"
# 3. "List all tools and materials mentioned with timestamps"
# 4. "Extract tips and tricks with their demonstrations"
# """