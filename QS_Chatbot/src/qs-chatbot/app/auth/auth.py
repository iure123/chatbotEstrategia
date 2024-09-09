"""
Autenticacao
"""
import asyncio
import webbrowser
import streamlit as st
from httpx_oauth.clients.google import GoogleOAuth2
import json
from google.cloud import secretmanager
import logging

import config

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)

async def get_authorization_url(client,
                                  redirect_uri):
    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url

async def get_access_token(client,
                             redirect_uri,
                             code):
    access_token = await client.get_access_token(code, redirect_uri)
    return access_token

async def refresh_token(client,
                    token):
    access_token = await client.refresh_token(token)
    return access_token

async def get_id_email(client,
                    token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email

def get_secret(project, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project}/secrets/{secret_id}/versions/latest"
    
    response = client.access_secret_version(request={"name":name})
    payload = response.payload.data.decode("UTF-8")
    
    return payload

def get_client():
    project = config.PROJECT_ID
    secret_id = config.SECRET_ID
    redirect_uri = config.APP_URL

    client_json = json.loads(get_secret(project, secret_id))
    client_id = client_json['web']['client_id']
    client_secret = client_json['web']['client_secret']

    client = GoogleOAuth2(client_id, client_secret)

    return client, redirect_uri

def login_page():
    print("................:REDIRECIONA PARA LOGIN")
    client, redirect_uri = get_client()
    authorization_url = asyncio.run(get_authorization_url(client, redirect_uri))
    st.title("Bem-vindo a Academia Digital\n\n")
    login = st.empty()
    login.write(f'''
        <a target="_self" href="{authorization_url}">
            <button>
                Login via Google
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )  

def authenticated():

    client, redirect_uri = get_client()

    if 'token' not in st.session_state:
        log.info("................:BUSCA CODE")
        code = st.query_params.get_all("code")[0]
        log.info("................:GERA TOKEN")
        token = asyncio.run(get_access_token(client=client,
                    redirect_uri=redirect_uri,
                    code=code))
        st.session_state.token = token
        user_id, user_email = asyncio.run(get_id_email(client=client, token=token['access_token']))
        st.session_state.user_id = user_id
        st.session_state.user_email = user_email

    else:
        log.info("................:LE TOKEN")
        token = st.session_state.token
        try:
            log.info("................:CHECK TOKEN")
            user_id, user_email = asyncio.run(get_id_email(client=client, token=token['access_token']))
            st.session_state.user_id = user_id
            st.session_state.user_email = user_email
        except:
            log.info("................:REFRESH TOKEN")
            token = asyncio.run(refresh_token(token))

    return