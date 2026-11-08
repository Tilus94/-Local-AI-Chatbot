import requests
import json


url = "http://localhost:11434/api/chat"
conversation = []

while True:

   
    
    user_prompt = input("Ask your AI something: ")

    if user_prompt.lower() == "exit":
        print("\n=== CONVERSATION HISTORY ===")
        print(json.dumps(conversation, indent=4))
        break

    messages = conversation + [
    {"role": "user", "content": user_prompt}]


    payload = {
        "model": "llama3.2:3b",
        "messages": messages,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        ollama = response.json()["message"]["content"]
        print(ollama)

        
        conversation = messages
        conversation.append({
            "role": "assistant",
            "content": ollama
            })

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
    