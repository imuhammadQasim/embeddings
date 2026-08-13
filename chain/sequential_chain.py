from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", 
    temperature=0.3)

prompt1 = PromptTemplate.from_template("write a detailed note on {topic}")
prompt2 = PromptTemplate.from_template("Write a summary of this {text}")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser


result = chain.invoke({"topic": "Photgrapgy"})

print(result)
