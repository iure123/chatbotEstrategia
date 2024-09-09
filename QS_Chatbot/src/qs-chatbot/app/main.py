"""
Entrypoint
"""
import streamlit as st
import traceback
import auth
from chat import DashBoard
import logging

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)

if __name__ == "__main__":
    
    try:
        log.info(f'# Init Authenticated')
        auth.authenticated()
    except Exception as e:
        log.info(f'# Init Login Page')
        auth.login_page()
        log.info(f'# ' + str(e) + str(traceback.format_exc())) 

    if 'token' in st.session_state:
        log.info(f'# Init DashBoard')
        st.session_state.run_cloud = True

        if "messages" not in st.session_state:
            st.session_state.messages = {}
        if "chats" not in st.session_state:
            st.session_state.chats = {}
        DashBoard()