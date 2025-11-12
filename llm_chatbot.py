import os
from google import genai
from google.genai import types
#let's Configur ---
API_KEY_NAME = "GENERATIVE_AI_API_KEY"
MODEL_NAME = "gemini-2.5-flash"
# The Core Functionality
class GenerativeChatbot:
    """
    Deals About simple conversational chatbot that maintains history using an LLM API.
    """
    def __init__(self, system_prompt: str):
        # API Key Check for Security Best Practice
        self.api_key = os.getenv(API_KEY_NAME)
        if not self.api_key:
            raise ValueError(
                f"API Key not found. Please set the '{API_KEY_NAME}' environment variable."
            )
        # Let's Initialize Model Client and History
        print(f"Initializing {MODEL_NAME}...")

        # +++ ACTUAL API CLIENT SETUP ---
        # Let's Initialize the client using the API key we got from Google genai
        self.client = genai.Client(api_key=self.api_key)
        # now also let's Create the chat session with the model and system instruction
        self.chat_session = self.client.chats.create(
            model=MODEL_NAME,
            config=types.GenerateContentConfig( system_instruction=system_prompt )
        )

        print("_" * 36)
        # The history list is no longer strictly needed for memory
        self.history = [{"role": "system", "content": system_prompt}]
        print(f"Chat session started with system prompt: '{system_prompt}'")

    def get_response(self, user_input: str) -> str:
        """Sends user input to the LLM and returns the generated response."""
        self.history.append({"role": "user", "content": user_input})
        # here is the  Actual API Call
        try:
            response = self.chat_session.send_message(user_input)
            self.history.append({"role": "model", "content": response.text})
            return response.text
        except Exception as e:
            return f"API Error: Could not get a response. Details: {e}"

# --- Main Execution ---
if __name__ == "__main__":
    # The chatbot's defined personality/role
    SYSTEM_PROMPT = "You are a helpful and concise technical assistant specializing in Cloud, Security, and Full-Stack development. Keep answers brief."
    try:
        # Create and run the chatbot
        bot = GenerativeChatbot(system_prompt=SYSTEM_PROMPT)
        print("\n--- Start Chatting! Type 'quit' to exit.")
        while True:
            query = input("You==> ")
            if query.lower() in ("quit", "exit", "q", ":q"):
                print("Exiting chat. Goodbye!")
                break
            bot_response = bot.get_response(query)
            print(f"Bot: {bot_response}")

    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("\nFix this error to run the code. See README for help.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
#at final I got this
'''--- Start Chatting! Type 'quit' to exit.
You==> what is the capital city of ethiopia?
Bot: Addis Ababa.
You==> how far is it from mekkele?
Bot: Approximately 780 km.
You==> you are good,,,and am pleased I make you at last.
Bot: Thank you! Happy to help.
You==> nicee, see u tommorow.
Bot: Sounds good! Have a great day.
You==>'''#which is too fasinatimg
