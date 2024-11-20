from openai import OpenAI

client = OpenAI()


def ask_model(user_input: str):
    completion = client.chat.completions.create(
        model="ft:gpt-4o-2024-08-06:personal::AVlKXZY3",
        messages=[
            {"role": "system", "content": "You are a product support chatbot for the ZPhone 12"},
            {"role": "user", "content": user_input}
        ],
        stream=True
    )
    for chunk in completion:
        yield chunk.choices[0].delta.content
