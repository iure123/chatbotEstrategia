FROM python:3.10

ARG PROJECT_ID
ARG SECRET_ID
ARG TOKEN_SA

COPY requirements.txt ./

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt --extra-index-url=https://oauth2accesstoken:${TOKEN_SA}@southamerica-east1-python.pkg.dev/sz-workspace-digital-prod/nucleo-digital/simple/

ENV GCP_PROJECT_ID=${PROJECT_ID}
ENV GCP_SECRET_ID=${SECRET_ID}

COPY ./app /app
COPY .streamlit/config.toml /.streamlit/config.toml

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION "python"

EXPOSE 8080

#RUN streamlit config show ##DEBUG config
CMD ["streamlit", "run", "/app/main.py", "--server.port", "8080"]