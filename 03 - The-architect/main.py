import asyncio
import logging
from architect import ArchitectAgent

# Configura il logging all'inizio dell'applicazione
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main_async():
    """Asynchronous main function to run the application."""
    
    agent = ArchitectAgent()

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Goodbye!")
            break
        
        ans = agent.invoke(user_input, session_id="default_session", user_id="default_user")
        print(f"Architect: {ans}")


def main():
    """Entry point for the application."""
    asyncio.run(main_async())


if __name__ == "__main__":
    main()