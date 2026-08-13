from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import Annotated, List
from pydantic import BaseModel, Field

load_dotenv()

class Review(BaseModel):
    summary: str = Field(description="Summary of the review.")
    sentiment: List[str] = Field(description="List of sentiments detected in the review.")
    rating: float = Field(description="Rating given in the review out of 5.")
    
model = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.3
)

structured_model = model.with_structured_output(Review)

with open("./reviews.txt", "r", encoding="utf-8") as file:
    file_data = file.read() 
    
result = structured_model.invoke(file_data)

print(result.summary)
