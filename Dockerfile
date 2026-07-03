# Usa uma imagem oficial leve do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências de sistema necessárias para compilar pacotes
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências para o container
COPY requirements.txt .

# Instala as bibliotecas do projeto ignorando o cache para economizar espaço
RUN pip install --no-cache-dir -r requirements.txt

# Copia todas as pastas do projeto para dentro do container
COPY . .

# Expõe as portas da API (8000) e do Dashboard (8501)
EXPOSE 8000
EXPOSE 8501

# Comando padrão (por padrão, vamos deixar ele iniciar a API)
CMD ["python", "-m", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

