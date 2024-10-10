from pages import obter_dados_usuario  # Importando a função que coleta os dados do formulário
from bot.assistant import generate  # Importando a função que gera os relatórios
import streamlit as st
import base64
from utils import generate_pdf  # Certifique-se de que a função generate_pdf está importada

def main():
    # Obtendo os dados do formulário
    st.title("Gerar Solução com Base em Dados Coletados")
    prompt_1_data = obter_dados_usuario()

    if prompt_1_data:
        # Gerando os prompts com base nos dados coletados
        prompt_1_text, prompt_2_text, prompt_3_text = generate(prompt_1_data)

        # Concatenando os relatórios em uma única string
        relatorio_completo = f"{prompt_1_text}\n\n{prompt_2_text}\n\n{prompt_3_text}"

        # Exibindo o relatório completo
        st.subheader("Relatório Completo:")
        st.text_area("Relatório Completo", value=relatorio_completo, height=500)

        # Gerando o PDF do relatório completo
        pdf = generate_pdf(relatorio_completo)
        b64 = base64.b64encode(pdf).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="relatorio_completo.pdf">Baixar Relatório Completo em PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
