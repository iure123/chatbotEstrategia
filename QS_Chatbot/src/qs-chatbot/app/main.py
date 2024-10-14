import streamlit as st
import logging
from pages import intro, form_page

def setup_logging():
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    log = logging.getLogger(__name__)
    log.info(f'# Init DashBoard - LOCAL')

def setup_session_state():
    st.session_state.user_id = "local"
    st.session_state.user_email = "local@suzano.com"
    st.session_state.run_cloud = False

    if "messages" not in st.session_state:
        st.session_state.messages = {}
    if "chats" not in st.session_state:
        st.session_state.chats = {}

def main():
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Ir para", ["Introdução", "Formulário"])

    if page == "Introdução":
        intro()
    elif page == "Formulário":
        form_page()

if __name__ == "__main__":
    setup_logging()
    setup_session_state()
    main()
