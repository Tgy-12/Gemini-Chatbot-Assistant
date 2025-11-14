Conversational AI Assistant: Gemini API Integration
This project implements a fully functional, memory-aware chatbot by integrating the Gemini 2.5 Flash model via the google-genai Python SDK. It serves as a practical demonstration of integrating Large Language Models (LLMs) into custom applications.

## Key Technical Skills Demonstrated

This project showcases expertise in three core areas relevant to Generative AI and professional development:

Generative AI & LLMs:

LLM Integration: Successful connection and interaction with a state-of-the-art model (gemini-2.5-flash).

Conversation Memory: Utilizing the chats.create() session to ensure the model maintains context and history across multiple turns.

System Prompt Engineering: Defining a precise persona (Cloud/Security/Full-Stack Assistant) using system_instruction to guide the model's behavior and tone.

Software Development Best Practices:

Secure Credential Handling: API Key is loaded securely via the Linux environment variable (GENERATIVE_AI_API_KEY), ensuring the key is never exposed in the source code.

Robust Error Handling: Implementation of try...except blocks to gracefully catch and report API errors (e.g., network issues, rate limits, invalid keys).

Python & Cloud Infrastructure:

Familiarity with standard Python class structure and the os module for environment management.

Demonstration of connecting Python code to a Cloud-based API service.

## Setup and Execution
Prerequisites
Python 3.8+ and above

Gemini API Key: Obtained from Google AI Studio.

Active Virtual Environment (e.g., using venv or conda).

1. Installation
Activate your virtual environment and install the required library:


pip install google-genai
2. API Key Configuration (Linux/macOS)
For the script to run, your API key must be set as an environment variable named GENERATIVE_AI_API_KEY.

a) Temporary (for current terminal session):


export GENERATIVE_AI_API_KEY='[YOUR_ACTUAL_API_KEY]'
b) Permanent (recommended for development): Add the export line above to your ~/.bashrc or ~/.zshrc file and run source ~/.zshrc.

3. Running the Chatbot
Execute the script from your terminal:

python3 llm_chatbot.py (optional,,if u are with python3 use this unless simply use the python---)
The application will initialize the model and start the conversation loop. Type quit to exit.
