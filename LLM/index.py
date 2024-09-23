from openai import OpenAI

api_key = "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"

client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(completion)