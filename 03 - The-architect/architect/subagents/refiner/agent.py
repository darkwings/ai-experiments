"""
Architecture Refiner Agent

This agent refine the architecture design provided by the initial architecture agent
and reviewed by the refiner.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .web_searcher.agent import web_searcher
from google.adk.tools.tool_context import ToolContext
from ...instructions import COMPLETION_PHRASE, ARCHITECTURE_REFINER_INSTRUCTION

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# --- Tool Definition ---
def exit_loop(tool_context: ToolContext):
  """Call this function ONLY when the rewiew indicates no further changes are needed, signaling the iterative process should end."""
  print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
  tool_context.actions.escalate = True
  # Return empty dict as tools should typically return JSON-serializable output
  return {}

architecture_refiner = LlmAgent(
    name="ArchitectureRefinerAgent",
    model=GEMINI_MODEL,
    instruction=ARCHITECTURE_REFINER_INSTRUCTION,
    description="Refines the proposed software architecture to improve quality",
    output_key="architecture_design",
    tools=[
        AgentTool(web_searcher),
        exit_loop
    ]
)