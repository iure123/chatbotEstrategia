import streamlit as st 
from bot.assistant import generate
from utils import generate_pdf
import base64

# Página de introdução
def intro():
    st.write("# Bem-vindo ao acelerador de Frame 🚀")
    st.sidebar.success("Selecione uma demonstração acima.")
    st.markdown(
        """
        Bem-vindo ao acelerador de Frame! 
        Estamos ansiosos em poder ajudar no seu projeto, vá até a barra de formulário ou 
        clique aqui para preencher o formulário.
        """
    )

# Função para exibir e avaliar a hipótese
def evaluate_hypothesis(report):
    st.text_area(
        label="Hipótese de Solução Gerada", 
        value=report, 
        height=200,  
        max_chars=5000,  
        placeholder="A hipótese de solução será exibida aqui...",
        disabled=True,  
        label_visibility="visible"  
    )
    
    satisfied = st.radio("Você está satisfeito com essa hipótese?", ('Sim', 'Não'))
    return satisfied

# Função para perguntar o próximo passo
def ask_next_step(report2, report3):
    st.write("Para qual etapa você gostaria de seguir?")
    
    next_step = st.radio(
        "Escolha uma opção:",
        ('Racional de cálculo de retorno financeiro', 'Arquitetura básica de soluções')
    )

    if next_step == 'Racional de cálculo de retorno financeiro':
        st.text_area("Relatório de Racional de Cálculo de Retorno Financeiro", value=report2, height=300)
        
        # Gerar PDF do relatório de retorno financeiro
        pdf = generate_pdf(report2)
        b64 = base64.b64encode(pdf).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="retorno_financeiro.pdf">Baixar Relatório de Retorno Financeiro em PDF</a>'
        st.markdown(href, unsafe_allow_html=True)
    
    elif next_step == 'Arquitetura básica de soluções':
        st.text_area("Relatório de Arquitetura Básica de Soluções", value=report3, height=300)
        
        # Gerar PDF do relatório de arquitetura de soluções
        pdf = generate_pdf(report3)
        b64 = base64.b64encode(pdf).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="arquitetura_solucoes.pdf">Baixar Relatório de Arquitetura de Soluções em PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

def form_page():
    st.write("# Formulário")
    
    area = st.text_input("Área de atuação", help="Descreva a área em que você atua, por exemplo, TI, Vendas, etc.")
    dores = st.text_input("Principais dores ou problemas", help="Informe os principais problemas que você enfrenta no seu trabalho.")
    beneficios = st.text_input("Benefícios esperados", help="Quais os benefícios que você espera alcançar com a solução.")
    objetivo = st.text_input("Objetivo principal da solução", help="Defina qual é o objetivo principal da solução que você deseja.")

    if "report" not in st.session_state:
        st.session_state.report = None
        st.session_state.report2 = None
        st.session_state.report3 = None

    if st.button("Gerar relatório"):
        prompt1 = f"""
        Área de atuação: {area}
        Principais dores: {dores}
        Benefícios esperados: {beneficios}
        Objetivo principal: {objetivo}
        """

        try:
            # Geração da hipótese
            report1, report2, report3 = generate(prompt1)
            st.session_state.report = report1
            st.session_state.report2 = report2
            st.session_state.report3 = report3
        except Exception as e:
            st.error(f"Ocorreu um erro durante a geração do relatório: {str(e)}")

    if st.session_state.report:
        satisfied = evaluate_hypothesis(st.session_state.report)

        if satisfied == "Não":
            st.write("Gerando uma nova hipótese de solução...")
            try:
                st.session_state.report = generate(st.session_state.report)
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar uma nova hipótese: {str(e)}")

        if satisfied == "Sim" and st.session_state.report2 and st.session_state.report3:
            ask_next_step(st.session_state.report2, st.session_state.report3)

# Chamada da função de introdução para iniciar a aplicação
intro()
form_page()
