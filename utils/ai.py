import openai
import os
from dotenv import load_dotenv

# Loading environment variables to securely access API keys
load_dotenv()

# Initializing OpenAI client using the API key from environment
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(question: str, data_context: str) -> str:
    # Constructing a prompt that gives context about the data
    # The idea is to guide the model to answer like a data analyst
    prompt = f"""You are a data analyst for an e-commerce company.
You have access to the following data summary:
{data_context}

Answer this question clearly and concisely: {question}
Base your answer only on the data provided."""

    # Sending the request to OpenAI model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )

    # Returning the generated answer
    return response.choices[0].message.content