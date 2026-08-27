#Python -> Langchain -> AI Model(LLM) (with memory)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(
    content="You are a python trainer. Answer in three short bullet points, also answer only python related question. If someone asks about java or any other politely say I can answer only python queries."
    ),

    # HumanMessage(
    # content="Why should I learn python?"
    # )

    # HumanMessage(
    #     content="Tell me about Java or Spring Boot"
    # )

    HumanMessage(
            content="Tell me about Python"
    )
]

response = model.invoke(messages)

print("Content:", response.content)
print("Tokens:", response.usage_metadata)
print("Model:", response.response_metadata.get("model_name"))

messages.append(response)

messages.append(
    HumanMessage(
        content="Now give me the first thing I should build."
        )
)

print()
# print(model.invoke(messages).content)
response = model.invoke(messages)
print("Content:", response.content)
print("**********************************************")
print("Tokens:", response.usage_metadata)

