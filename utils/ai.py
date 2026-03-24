import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(question: str, data_context: str) -> str:
    prompt = f"""You are a data analyst for an e-commerce company.
You have access to the following data summary:
{data_context}

Answer this question clearly and concisely: {question}
Base your answer only on the data provided."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content