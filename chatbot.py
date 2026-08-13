from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", 
    temperature=0.3)

messages = [
    SystemMessage(content='You are a helpful assistant.'),
]

while True:
    user_input = input('You:')
    messages.append(HumanMessage(content=user_input))
    if user_input == 'exit'  or user_input == 'q':
        break
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(messages)
