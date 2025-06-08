"""
Architect Agent: first step
"""

from google.adk.agents.llm_agent import LlmAgent
from ...instructions import INITIAL_ARCHITECTURE_INSTRUCTION

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

initial_architecture_agent = LlmAgent(
    name="initial_architecture_agent",
    model=GEMINI_MODEL,
    description="Initial architecture agent",
    instruction=INITIAL_ARCHITECTURE_INSTRUCTION,
    output_key="architecture_design"
)