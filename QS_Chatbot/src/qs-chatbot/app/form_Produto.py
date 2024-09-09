import streamlit as st
import config
from bot.assistant import BotQS
from google.cloud import firestore

# Inicializa o chatbot BotQS com os parâmetros de configuração
bot = BotQS(
    model_name="gemini-1.5-flash-001",  # Modelo de IA utilizado para gerar respostas
    system_prompt=open("app/context/system_prompt.txt", 'r', encoding='utf-8').read(),  # Prompt que define o contexto do sistema
    db_firestore=firestore.Client()  # Referência ao Firestore para persistência de dados
)

class FormInterface:
    """
    Interface para capturar as informações necessárias através de um formulário.
    Esta classe lida com a interface do usuário no Streamlit e gera uma resposta automática
    com base nas informações inseridas no formulário.
    """
    def __init__(self):
        # Exibe o título da página
        st.title("Formulário de Informações")

        # Criação do formulário para captura de informações do usuário
        with st.form(key="user_form"):
            # Campos para coletar informações do usuário sobre o problema e as soluções
            area = st.text_input("Área enfrentando dificuldades")  # Exemplo: Departamento de TI, Produção
            tipo_processos = st.text_input("Tipo de processos utilizados (ex.: manuais, não integrados)")  # Exemplo: Processos manuais
            dores = st.text_area("Descreva as dores específicas enfrentadas (ex.: falta de visibilidade, baixa eficiência)")  # Exemplo: Falta de visibilidade
            problemas_adicionais = st.text_area("Descreva problemas adicionais (ex.: falta de conhecimento, dificuldades de comunicação)")  # Exemplo: Falta de treinamento
            impacto = st.text_area("Descreva o impacto (ex.: desempenho, qualidade do trabalho)")  # Exemplo: Baixa produtividade
            objetivo = st.text_input("Objetivo principal (ex.: reduzir custos, aumentar produtividade)")  # Exemplo: Reduzir custos em 10%
            hipotese = st.text_area("Hipótese de solução digital (ex.: criar solução digital integrada, usando IoT, Machine Learning, etc.)")  # Exemplo: Solução baseada em IoT
            oportunidades = st.text_area("Oportunidades de geração de valor financeiro")  # Exemplo: Redução de custos operacionais
            submit_button = st.form_submit_button(label="Enviar")  # Botão de envio do formulário

        # Verifica se o botão de envio foi clicado
        if submit_button:
            # Processa as informações do formulário e gera uma resposta
            self.process_form(area, tipo_processos, dores, problemas_adicionais, impacto, objetivo, hipotese, oportunidades)

    def process_form(self, area, tipo_processos, dores, problemas_adicionais, impacto, objetivo, hipotese, oportunidades):
        """
        Processa as informações fornecidas no formulário e gera um prompt para o chatbot.
        """
        # Monta o prompt com base nas respostas do formulário, estruturando as informações fornecidas
        prompt = f"""
        A área {area} está enfrentando dificuldades devido à utilização de processos {tipo_processos}, 
        resultando em {dores}. Além disso, a equipe enfrenta {problemas_adicionais}, o que impacta {impacto}.
        
        O objetivo principal é {objetivo}.
        
        A hipótese de solução digital é {hipotese}.
        
        As oportunidades de geração de valor financeiro incluem {oportunidades}.
        """

        # Gera resposta usando o bot com o prompt criado
        response = bot.get_chat().send_message([prompt])
        
        # Exibe a resposta do chatbot na interface do Streamlit
        st.markdown(response.text)
    