#Python -> Langchain -> AI Model(LLM)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

response = model.invoke("Tell me more about langchain framework in short")

print(response.content)


