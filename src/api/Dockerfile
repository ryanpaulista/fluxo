# Definição da imagem oficial do Python e versão especificada

FROM python:3.10-slim

# Variáveis de ambiente para evitar que o Python gere arquivos .pyc e que o output seja exibido em buffer
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Definição do diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências do sistema se necessário
# RUN apt-get update && apt-get install -y <dependências>
RUN apt-get update && apt-get install -y postgresql-client

# Copiar e instalar dependencias do Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia código da aplicação para o diretório de trabalho no container
COPY . . 
