import streamlit as st
import logging
from pages import intro, form_page

# Mapeamento das páginas
page_names_to_funcs = {
    "Home": intro,
    "Formulário": form_page,
}

# Função principal para exibir a página correspondente
def run():
    selected_page = st.sidebar.selectbox("Escolha a página", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()

# Configuração de logs e estado do usuário
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)

if __name__ == "__main__":    
    st.session_state.user_id = "local"
    st.session_state.user_email = "local@suzano.com"
    st.session_state.run_cloud = False

    if "messages" not in st.session_state:
        st.session_state.messages = {}
    if "chats" not in st.session_state:
        st.session_state.chats = {}

    log.info(f'# Init DashBoard - LOCAL')
    
    run()  # Chama a função para rodar a página selecionada
