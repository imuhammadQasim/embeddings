import os
from typing import Dict
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
# 1. Initialize the LLM
# Ensure your OPENAI_API_KEY is set in your environment variables
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

# ---------------------------------------------------------------------
# 2. Define the Specialized Sub-Chains
# ---------------------------------------------------------------------

# Math Chain
math_prompt = ChatPromptTemplate.from_template(
    "You are an expert mathematician. Solve this math problem step-by-step:\n\n{query}"
)
math_chain = math_prompt | llm | StrOutputParser()

# Physics Chain
physics_prompt = ChatPromptTemplate.from_template(
    "You are a brilliant physicist. Explain this physics concept clearly:\n\n{query}"
)
physics_chain = physics_prompt | llm | StrOutputParser()

# General/Fallback Chain
general_prompt = ChatPromptTemplate.from_template(
    "Answer the following question politely:\n\n{query}"
)
general_chain = general_prompt | llm | StrOutputParser()


# ---------------------------------------------------------------------
# 3. Define the Router Chain (The Decision Maker)
# ---------------------------------------------------------------------

# This prompt forces the LLM to output exactly one word: 'math', 'physics', or 'general'
router_prompt = ChatPromptTemplate.from_template(
    """Given the user question below, classify it as exactly one of these categories: 'math', 'physics', or 'general'. 
Do not include any other text, punctuation, or explanation.

User Question: {query}
Category:"""
)

# The router chain extracts the classification string
router_chain = router_prompt | llm | StrOutputParser()


# ---------------------------------------------------------------------
# 4. Define the Routing Logic Function
# ---------------------------------------------------------------------

def route_destination(info: Dict) -> RunnableLambda:
    """
    Inspects the classification from the router_chain 
    and returns the appropriate sub-chain execution path.
    """
    # Clean the output to avoid whitespace issues
    decision = info["topic"].strip().lower()
    
    print(f"🤖 Router classified query as: '{decision}'\n")
    
    if "math" in decision:
        return math_chain
    elif "physics" in decision:
        return physics_chain
    else:
        return general_chain


# ---------------------------------------------------------------------
# 5. Assemble the Full Conditional Chain
# ---------------------------------------------------------------------

# We use RunnablePassthrough to carry the original query forward, 
# inject the topic classification into the dictionary, and pass it to our router function.
full_conditional_chain = (
    {"topic": router_chain, "query": RunnablePassthrough()}
    | RunnableLambda(route_destination)
)


# ---------------------------------------------------------------------
# 6. Test the Chain with Different Inputs
# ---------------------------------------------------------------------

if __name__ == "__main__":
    # Test Case 1: Math
    print("--- Test 1: Math Query ---")
    query_1 = "What is the derivative of x^2 + 3x?"
    result_1 = full_conditional_chain.invoke(query_1)
    print(f"Result:\n{result_1}\n")

    # Test Case 2: Physics
    print("--- Test 2: Physics Query ---")
    query_2 = "Why is the sky blue, and how does Rayleigh scattering work?"
    result_2 = full_conditional_chain.invoke(query_2)
    print(f"Result:\n{result_2}\n")

    # Test Case 3: General Fallback
    print("--- Test 3: General Query ---")
    query_3 = "What is a good recipe for chocolate chip cookies?"
    result_3 = full_conditional_chain.invoke(query_3)
    print(f"Result:\n{result_3}\n")
    
full_conditional_chain.get_graph().print_ascii()