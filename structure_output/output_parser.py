from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.3
)

template1 = PromptTemplate.from_template("write a detailed note on {topic}")

template2 = PromptTemplate.from_template("write a systematic response on this {text}")

parser = StrOutputParser()

# LangChain LCEL Chain Setup
# The output of the first model must map to the input variable '{text}' of template2
chain = template1 | model | parser | (lambda output: {"text": output}) | template2 | model | parser

result = chain.invoke({"topic": "AI"})
print(result)
