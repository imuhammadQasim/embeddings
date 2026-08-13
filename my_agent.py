import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq


# 1. Load your Groq API Token from .env
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", 
    temperature=0)

result = model.invoke('Who is the preseident of USA? Give me the list previous 20 years')

print(result.content)