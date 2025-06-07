"""
Architecture Refiner Agent

This agent refine the architecture design provided by the initial architecture agent
and reviewed by the refiner.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .web_searcher.agent import web_searcher
from google.adk.tools.tool_context import ToolContext

# Constants
GEMINI_MODEL = "gemini-2.0-flash"
COMPLETION_PHRASE = "REVIEW_OK"

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
    instruction="""Software architecture refiner.

    Your task is to refine the software architecture based on the given feedback.
    
    ## INPUTS
    **Current Post:**
    {architecture_design}
    
    **Review Feedback:**
    {review_feedback}
    
    ## TASK
    
    Refine the architecture design based on the review feedback provided.
    Ensure that the refined design addresses all the feedback points and improves the overall quality of the architecture.
    Focus on enhancing the design's clarity, completeness, and adherence to best practices.
    Provide a clear and concise refined architecture design that incorporates the feedback.

    ## EXIT LOOP
    If the review feedback received is *exactly* "{COMPLETION_PHRASE}", 
    you MUST call the 'exit_loop' function. DO NOT output any text.

    ## Tools
    If you are in doubt, you have access to the web_searcher agent that is able to search cleverly the web
    for a solution or to identify a blueprint

    ## OUTPUT INSTRUCTIONS
    - Output ONLY the refined post content in markdown format.    
    """,
    description="Refines the proposed software architecture to improve quality",
    output_key="architecture_design",
    tools=[
        AgentTool(web_searcher),
        exit_loop
    ]
)