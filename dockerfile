FROM python:3.11-alpine

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

# Execute as migrações do Django
RUN /bin/sh -c " python manage.py makemigrations && python manage.py migrate"

# Comando de entrada padrão para o contêiner
CMD ["/bin/sh", "-c", " python manage.py runserver 0.0.0.0:8000"]
