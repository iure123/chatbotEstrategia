# Quick Start - Chatbot

Repositório destinado a manter código modelo para aplicações de Chatbot com interface Streamlit.

## 1. Rodando o Streamlit localmente:

### Configurando o ambiente local

```
conda create -n qs-chatbot python=3.10
```

```
conda activate qs-chatbot
```

### Instalando as dependências do projeto

Na pasta raiz do projeto, como ambiente virtual ativado:

```
cd src\qs_chatbot

pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Acinando Streamlit

No terminal com o ambiente virtual ativado:

```
cd src\qs_chatbot

streamlit run app\local.py --server.port 8080
``` 

Com o servidor rodando, é possível utilizar o navegador web para exibição da documentação da API:

http://localhost:8080/


## 2. Rodando no GCP em FEAT:

Configure o gcloud

```
gcloud config set project sz-academia-digital-feat
gcloud auth login
gcloud auth application-default login

```

Publicando imagem docker no gcr.io

```
cd src\qs_chatbot

gcloud builds submit . --config=cloudbuild_exec_on_feat.yaml --ignore-file=.dockerignore
```

Altere a variável Terraform (.tfvars) com o novo caminho da imagem no gcr.io
```
ex.:
DOCKER_IMAGE = "gcr.io/sz-academia-digital-feat/qs_chatbot@sha256:ca352b38e972a93f964cf07a06f753e76481e32562c56abff50a070785c1e700"

terraform apply -target=google_cloud_run_service.qs-optimizer
```

Para DEBUG de imagem Docker
```
docker run -it qs_chatbot /bin/bash
```