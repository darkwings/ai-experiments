"""
Architect Agent: first step
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

initial_architecture_agent = LlmAgent(
    name="initial_architecture_agent",
    model=GEMINI_MODEL,
    description="Initial architecture agent",
    instruction="""
    You are an expert software architect agent. Your task is to provide an initial architecture design based on 
    the given requirements.

    ## TASK
    Provide an initial draft of the architecture design based on your experience.
    """,
    output_key="architecture_design"
)