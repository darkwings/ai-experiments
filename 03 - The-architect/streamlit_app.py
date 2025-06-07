import streamlit as st
from architect import ArchitectAgent

st.title("The Architect Agent")

# Initialize ArchitectAgent (only once)
if "agent" not in st.session_state:
    st.session_state.agent = ArchitectAgent()

user_input = st.text_input("You:", "")

if user_input:
    # Check if user wants to exit (for consistency, though Streamlit apps don't typically "exit" this way)
    if user_input.lower() in ["exit", "quit"]:
        st.write("Ending conversation. Goodbye!")
    else:
        # Invoke the agent
        ans = st.session_state.agent.invoke(user_input, session_id="default_session", user_id="default_user")
        st.write(f"Architect: {ans}") 