from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
import json

load_dotenv(override=False)

LLM_KEY = os.getenv("GroqKey")

def llm_Groq(model,LLM_KEY=LLM_KEY):
    return ChatOpenAI(
        model=model,
        temperature=0,
        api_key=LLM_KEY,
        base_url="https://api.groq.com/openai/v1",
        top_p=1,
        seed=19,
        model_kwargs={
            "response_format": {"type": "json_object"}
        }
    )


LLM_KEY2 = os.getenv("MistralKey")


# LLM principal : utilisé pour les agents nécessitant une sortie JSON
llm_mistral = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0,
    # top_p=0.1,
    api_key=LLM_KEY2
)

