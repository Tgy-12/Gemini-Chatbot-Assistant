# Conversational AI Assistant: Gemini API Integration

This project implements a fully functional, memory-aware chatbot by integrating the Gemini 2.5 Flash model via the Google Generative AI Python SDK. It serves as a practical demonstration of integrating Large Language Models (LLMs) into custom applications.

## 🚀 Key Technical Skills Demonstrated

This project showcases expertise in three core areas relevant to Generative AI and professional development:

### **Generative AI & LLMs**
- **LLM Integration**: Successful connection and interaction with a state-of-the-art model (Gemini 2.5 Flash)
- **Conversation Memory**: Utilizing the `chats.create()` session to ensure the model maintains context and history across multiple turns
- **System Prompt Engineering**: Defining a precise persona (Cloud/Security/Full-Stack Assistant) using `system_instruction` to guide the model's behavior and tone

### **Software Development Best Practices**
- **Secure Credential Handling**: API Key is loaded securely via environment variables (`GENERATIVE_AI_API_KEY`), ensuring the key is never exposed in source code
- **Robust Error Handling**: Implementation of `try...except` blocks to gracefully catch and report API errors (network issues, rate limits, invalid keys)
- **Modular Design**: Clean separation of concerns with dedicated modules for configuration, chat logic, and utilities

### **Python & Cloud Infrastructure**
- **Python Programming**: Familiarity with standard Python class structure and the `os` module for environment management
- **Cloud API Integration**: Demonstration of connecting Python applications to cloud-based API services
- **Dependency Management**: Proper package management using `requirements.txt`

## 📋 Setup and Execution

### **Prerequisites**
- Python 3.8 or higher
- Gemini API Key (obtained from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Virtual Environment (venv, conda, or pipenv)

### **1. Installation**

Clone the repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required package
pip install google-generativeai
```
## 🔑 API Key Configuration

### **Linux/macOS**
**Temporary (current terminal session):**
```bash
export GENERATIVE_AI_API_KEY='your-actual-api-key-here'
```
###Runing
```command
# Run the chatbot
python llm_chatbot.py

# Alternatively, if you have python3 as your command
python3 llm_chatbot.py
```
