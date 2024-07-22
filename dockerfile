FROM python:3.11-alpine

# Instalar dependências do sistema necessárias para compilar psycopg2
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Defina o diretório de trabalho
WORKDIR /ibarber

# Copie o arquivo de requisitos
COPY requirements.txt .

# Instale as dependências no ambiente virtual
RUN pip install --upgrade pip && \
    pip install -r requirements.txt 

# Copie o restante do código-fonte do workspace
COPY . .

# Exponha a porta que o Django vai rodar em localhost
EXPOSE 8000

# Comando de entrada padrão para o contêiner
CMD ["/bin/sh", "-c", " python manage.py runserver 0.0.0.0:8000"]
