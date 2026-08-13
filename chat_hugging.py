import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

# 1. Set environment variables and load token
os.environ["HF_HOME"] = 'D:/HuggingFace'
load_dotenv()

# 2. Define the raw text-generation endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    temperature=0.3,
    max_new_tokens=100,
    extra_body={"provider": "hf-inference"} # Forces usage of HF's native free tier
)

# 3. Create the prompt template TinyLlama requires

template1 = PromptTemplate.from_template({
                            "template": "write a detailed note on {topic}",
                            "input_variables": ["topic"]
                            })

template2 = PromptTemplate.from_template({
                            "template": "write a 5 line summary of the following {text}.",
                            "input_variables": ["text"]
                            })

# 4. Chain them together using LCEL

prompt1 = template1.invoke({"topic": "AI"})
result = llm.invoke({"question": prompt1})


prompt2 = template2.invoke({"text": result})
result = llm.invoke({"question": prompt2})


# 5. Invoke the chain directly (Do NOT use ChatHuggingFace)
result = llm.invoke({"question": "Who is the president of America?"})
print(result)
