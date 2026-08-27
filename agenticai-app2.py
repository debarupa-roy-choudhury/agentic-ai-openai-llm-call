#Open AI SDK -> AI Model(LLM)

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Tell me about recent advancements in agentic ai field in short",
)

print(response.output_text)