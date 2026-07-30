import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful, friendly assistant."}
]

print("Mini Groq Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
    )

    reply = response.choices[0].message.content
    print("Bot:", reply)

    messages.append({"role": "assistant", "content": reply})
