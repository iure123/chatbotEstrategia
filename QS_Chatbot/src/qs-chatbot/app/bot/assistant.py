import vertexai 
from vertexai.generative_models import GenerativeModel, SafetySetting

# Variáveis de configuração para o modelo
textsi_1 = """
Prompt 1: Coleta de Informações e Geração de Hipótese de Solução Digital.

Instrução do Sistema: Este prompt coleta informações essenciais do usuário, como a área de atuação, os desafios enfrentados, os benefícios esperados e o objetivo da solução. A partir dessas informações, a IA gera uma hipótese detalhada de uma solução digital que aborda o problema identificado.

A hipótese deve considerar oportunidades de geração de valor financeiro, incluindo:
1. Redução de custos operacionais (ex: diminuição do custo unitário de produção).
2. Aumento de receita, por meio de:
   a. Redução de perdas na produção.
   b. Aumento da capacidade produtiva.
   c. Maximização da margem de lucro.
3. Redução do CAPEX direcionado para manutenção, modernização de processos e renovação de equipamentos.
4. Aproveitamento de oportunidades fiscais e financeiras.

Além do valor financeiro, a hipótese deve descrever 5 alavancas de valor qualitativo:
1. Padronização e simplificação de processos.
2. Melhoria da experiência dos colaboradores e clientes.
3. Eliminação de etapas e atividades redundantes.
4. Automação para reduzir retrabalho.
5. Aumento da visibilidade e controle sobre os processos.

Exemplo de entrada:
Área de atuação: TI
Principais dores: Tempo gasto em tarefas repetitivas
Benefícios esperados: Redução do tempo gasto em tarefas repetitivas
Objetivo principal: Automatizar tarefas repetitivas para aumentar a eficiência

Exemplo de saída:
Hipótese de Solução: Implementação de um sistema de automação de tarefas que reduz o tempo gasto em tarefas repetitivas em 50%.
"""

textsi_2 = """
Prompt 2: Análise Financeira.

Instrução do Sistema: Este prompt recebe a hipótese de solução gerada no Prompt 1 e realiza uma análise financeira detalhada da solução proposta. A IA calcula o retorno financeiro com base nas oportunidades de valor identificadas.

A análise deve incluir:
1. Fórmulas de cálculo para cada oportunidade de geração de valor financeiro, com explicação da metodologia usada.
2. Informações necessárias para realizar o cálculo real (ex: custos de manutenção atuais, produção esperada, etc.).
3. Comentários explicativos sobre as abordagens adotadas em cada cálculo.

Exemplo de entrada:
Hipótese de Solução: Implementação de um sistema de automação de tarefas que reduz o tempo gasto em tarefas repetitivas em 50%.

Exemplo de saída:
Análise Financeira: A implementação do sistema de automação resultará em uma economia anual de $100,000 devido à redução do tempo gasto em tarefas repetitivas.
"""

textsi_3 = """
Prompt 3: Plano de Arquitetura Técnica.

Instrução do Sistema: Este prompt utiliza a hipótese de solução gerada no Prompt 1 para desenvolver um plano de arquitetura técnica. A IA cria um design de alto nível que descreve como a solução será implementada.

O plano deve incluir:
1. Sequência lógica da arquitetura, identificando as principais funcionalidades e como os dados devem fluir pelo sistema.
2. Dados de entrada necessários e como serão processados.
3. Camadas de tratamento de dados, incluindo filtros, validações e cruzamento de informações.
4. Uso de IA, machine learning ou algoritmos preditivos, se aplicável.
5. Principais funcionalidades da solução e como devem ser implementadas para oferecer uma experiência otimizada.

Exemplo de entrada:
Hipótese de Solução: Implementação de um sistema de automação de tarefas que reduz o tempo gasto em tarefas repetitivas em 50%.

Exemplo de saída:
Plano de Arquitetura Técnica: O sistema de automação será composto por módulos de coleta de dados, processamento de dados e execução de tarefas automatizadas. Os dados serão coletados de várias fontes, processados por algoritmos de machine learning e usados para automatizar tarefas repetitivas.
"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
    SafetySetting(category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
    # Adicione outras categorias de segurança aqui
]

def inicializar_modelo(prompt_inicial):
    vertexai.init(project="sz-academia-digital-feat", location="us-central1")
    model = GenerativeModel(model_name="gemini-1.5-flash-001", system_instruction=[prompt_inicial])
    return model

def gerar_prompt_1(prompt_1_data):
    model = inicializar_modelo(textsi_1)
    response = model.generate_content([prompt_1_data], generation_config=generation_config, safety_settings=safety_settings, stream=True)
    return "".join([response.text if hasattr(response, 'text') else str(response) for response in response])

def pegar_hipotese_prompt_1(prompt_1_text):
    hipotese = ""
    lines = prompt_1_text.split('\n')
    start_collecting = False
    for line in lines:
        if "Hipótese de Solução:" in line:
            start_collecting = True
        if start_collecting:
            hipotese += line + "\n"
    return hipotese if hipotese else "Hipótese não encontrada."
#retorno financeiro 
def gerar_prompt_2(hipotese):
    model = inicializar_modelo(textsi_2)
    response = model.generate_content([hipotese], generation_config=generation_config, safety_settings=safety_settings, stream=True)
    return "".join([response.text if hasattr(response, 'text') else str(response) for response in response])
#arquitetura 
def gerar_prompt_3(hipotese):
    model = inicializar_modelo(textsi_3)
    response = model.generate_content([hipotese], generation_config=generation_config, safety_settings=safety_settings, stream=True)
    return "".join([response.text if hasattr(response, 'text') else str(response) for response in response])

def generate(prompt_1_data):
    prompt_1_text = gerar_prompt_1(prompt_1_data)
    hipotese = pegar_hipotese_prompt_1(prompt_1_text)
    
    prompt_2_text = gerar_prompt_2(hipotese)
    prompt_3_text = gerar_prompt_3(hipotese)

    return prompt_1_text, prompt_2_text, prompt_3_text
