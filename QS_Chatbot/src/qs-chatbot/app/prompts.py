import vertexai
from vertexai.generative_models import GenerativeModel
from config import generation_config, safety_settings, textsi_1, textsi_2, textsi_3

def inicializar_modelo(prompt_inicial):
    vertexai.init(project="sz-academia-digital-feat", location="us-central1")
    model = GenerativeModel(model_name="gemini-1.5-flash-001", system_instruction=[prompt_inicial])
    return model

def gerar_prompt_1(prompt_1_data):
    model = inicializar_modelo(textsi_1)
    response = model.generate_content([prompt_1_data], generation_config=generation_config, safety_settings=safety_settings, stream=True)
    return "".join([response.text if hasattr(response, 'text') else str(response) for response in response])

def pegahipotes_prompt_1(prompt_1_text):
    for linha in prompt_1_text.split('\n'):
        if "Hipótese de Solução:" in linha:
            return linha
    return "Hipótese não encontrada."

def gerar_prompt_2(hipotese):
    model = inicializar_modelo(textsi_2)
    response = model.generate_content([hipotese], generation_config=generation_config, safety_settings=safety_settings, stream=True)
    return "".join([response.text if hasattr(response, 'text') else str(response) for response in response])

def gerar_prompt_3(hipotese):
    model = inicializar_modelo(textsi_3)
    response = model.generate_content([hipotese], generation_config=generation_config, safety_settings=safety_settings, stream=True)
    return "".join([response.text if hasattr(response, 'text') else str(response) for response in response])

def generate(prompt_1_data):
    prompt_1_text = gerar_prompt_1(prompt_1_data)
    hipotese = pegahipotes_prompt_1(prompt_1_text)
    prompt_2_text = gerar_prompt_2(hipotese)
    prompt_3_text = gerar_prompt_3(hipotese)
    return prompt_1_text, prompt_2_text, prompt_3_text
