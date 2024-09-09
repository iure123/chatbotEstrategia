"""
Configuracoes de Ambiente
"""
import os
import vertexai.preview.generative_models as generative_models
import streamlit as st

APP_NAME=os.environ.get("APP_NAME", "Acelerador de Frames")

APP_URL=os.environ.get("APP_URL", "https://qs-chatbot-lplljendwa-rj.a.run.app/")
PROJECT_ID=os.environ.get("PROJECT_ID", "sz-academia-digital-feat")
SECRET_ID=os.environ.get("SECRET_ID", "academia_dig_client_id")
REGION_ID=os.environ.get("REGION_ID", "southamerica-east1")

DATABASE_NAME=os.environ.get("DATABASE_NAME", "qs-chatbot")

STORAGE_BUCKET_NAME = os.environ.get("STORAGE_BUCKET_NAME", "storage-qs-chatbot-feat")

CHAT_MSG_INIT = "Olá, eu sou seu Assistente de Soluções, pronto para ajudar a desenvolver ideias e otimizar processos. Como posso auxiliar hoje?"
CHAT_GENAI_CONFIG = {
    "max_output_tokens": 8192,
    "temperature": 0,
    "top_p": 0.95
}
CHAT_GENAI_SAFE = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: \
        generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: \
        generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: \
        generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: \
        generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}
CHAT_VECTOR_CONFIG = {
    "model": "textembedding-gecko@003"
}

PROMPT_WITH_RAG = f"""
Responda o questionamento abaixo:
__QUERY__
Considerando apenas a base de conhecimento abaixo:
__RAG__
"""

