"""
Chat Message
"""
import streamlit as st
from form_Produto import FormInterface  # Importe a nova classe

from google.cloud import storage, firestore

import config
from bot.assistant import BotQS

db_storage = storage.Client(project=config.PROJECT_ID)
db_firestore = firestore.Client(project=config.PROJECT_ID).collection(config.DATABASE_NAME)

bot = BotQS(
    model_name="gemini-1.5-flash-001",
    system_prompt=open("app/context/system_prompt.txt", 'r', encoding='utf-8').read(),
    db_firestore=db_firestore
)

class DashBoard:
    """
    Armazena funções para renderizar um Dashboard e exibir o formulário no Streamlit 
    """

    def __init__(self, **kwargs):
        st.title("Acelerador de Frames")
        self.user = st.session_state.user_email

        # Exibir formulário no lugar do chat
        form = FormInterface()  # Cria e exibe o formulário


