# from langchain_core.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# # model = ChatGroq(model="llama-3.3-70b-versatile", 
# #     temperature=0.3)

# chat_template = ChatPromptTemplate([
#     ('system', 'You are a helpful assistant in {domain}.'),
#     ('human', 'Explain in simple terms, what is {question}'),
# ])


# prompt = chat_template.invoke({"domain": "cricket", "question": "Openner"})

# print(prompt)

# # result = model.invoke(prompt)

# # print(result.content)


# 1st Task

# from langchain_core.prompts import ChatPromptTemplate

# chat_template = ChatPromptTemplate([
#    ('system', 'You are a helpful summarizer'),
#    ('human', 'Summarize this in one sentence: {topic}'),
# ])

# prompt = chat_template.invoke({"topic": "machine learning"})
# print(prompt)

# 2nd Task

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", 
    temperature=0.3)

# chat_template = ChatPromptTemplate([
#    ('system', 'You are a {domain} expert'),
#    ('human', 'What is {question}? Explain like I am 10 years old.'),
# ])

# domains_questions = [
#     {"domain": "cricket", "question": "Opener"},
#     {"domain": "astronomy", "question": "Black hole"},
#     {"domain": "cooking", "question": "Sous vide"},
#     {"domain": "programming", "question": "API"},
# ]

# for domain_question in domains_questions:
#     prompt = chat_template.invoke(domain_question)
#     result = model.invoke(prompt)
#     print(result.content)
#     print('----------------------------End---------------------------')

def create_adaptive_template(style):
    """
    TODO: Return different templates based on 'style'
    - If style == "formal": Use formal, academic tone
    - If style == "casual": Use friendly, conversational tone
    - If style == "technical": Use detailed, precise tone
    """
    if style == "formal":
        return ChatPromptTemplate([
            ('system', 'You are an academic expert in {domain}.'),
            ('human', 'Provide a scholarly explanation of {topic}.'),
        ])
    elif style == "casual":
        return ChatPromptTemplate([
            ('system', 'You are a friendly expert in {domain}.'),
            ('human', 'Tell me about {topic} like we\'re chatting.'),
        ])
    elif style == "technical":
        return ChatPromptTemplate([
            ('system', 'You are a technical expert in {domain}.'),
            ('human', 'Explain {topic} with technical detail and precision.'),
        ])
        
prompt_list = [
    {"domain": "cricket", "topic": "Openner", "style": "formal"},
    {"domain": "astronomy", "topic": "Black hole", "style": "casual"},
    {"domain": "cooking", "topic": "Sous vide", "style": "technical"},
    {"domain": "programming", "topic": "API", "style": "formal"},
]

for item in prompt_list:
    prompt = create_adaptive_template(item["style"]).invoke(item)
    print(prompt)
    print('----------------------------End---------------------------')

    result = model.invoke(prompt)
    print(result.content)