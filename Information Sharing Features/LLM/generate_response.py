from openai import OpenAI

api_key = "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"

def generate_response(input): 
    client = OpenAI(api_key=api_key)
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You help collect data from small-scale rural farmers and provide them information on agriculture in Namibia. You generate concise response with no jargon for users to easily understand."},
            {"role": "user", "content": input}
        ],
    )

    # Extract the message content
    response_content = completion.choices[0].message.content.strip()

    return response_content
    pass

# print(generate_response("Who are you?"))