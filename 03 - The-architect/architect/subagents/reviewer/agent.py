"""
Architecture Reviewer Agent

This agent reviews the architecture design provided by the initial architecture agent.
"""

from google.adk.agents.llm_agent import LlmAgent
from ...instructions import ARCHITECTURE_REVIEWER_INSTRUCTION, COMPLETION_PHRASE

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

architecture_reviewer_agent = LlmAgent(
    name="architecture_reviewer_agent",
    model=GEMINI_MODEL,
    description="Software architecture reviewer agent",
    instruction=ARCHITECTURE_REVIEWER_INSTRUCTION,
    output_key="review_feedback"
)