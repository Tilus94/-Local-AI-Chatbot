# Local AI Chatbot

A Python chatbot powered by Ollama and Llama 3.2, running locally without a cloud AI API.

## Features
- Interactive command-line chatbot
- Conversation history during each session
- HTTP error handling
- JSON-formatted conversation history on exit

## Requirements
- Python 3
- Ollama
- Llama 3.2 (3B)
- Python `requests` package

## Setup
1. Install Ollama and run `ollama pull llama3.2:3b`.
2. Install Python dependencies: `python -m pip install -r requirements.txt`.
3. Run the chatbot: `python chatbot.py`.
4. Type `exit` to print conversation history and quit.

## Notes
Conversation history is stored in memory and is not saved after the program exits.