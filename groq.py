from groq import Groq

# Initialize client with your API key
client = Groq(api_key="")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Hello Groq, What is mean by computer?"}
    ]
)

print(response.choices[0].message.content)
