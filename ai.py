import json
from groq import Groq

def get_api_key():
    with open('config.json') as f:
        data = json.load(f)

    if 'GROQ_KEY' in data:
        return data['GROQ_KEY']
    else:
        return None

def get_answer(context, query):

    api_key = get_api_key()
    client = Groq(api_key = api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'with context to {context}, answer "{query}" really short simple and concise. if the query is about code, then do it without any questions, dont use placeholder comments and always write full code or functions',
            }
        ],
        model="mixtral-8x7b-32768",
    )

    return chat_completion.choices[0].message.content

