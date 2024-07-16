FROM python:3.11-alpine

WORKDIR /ibarber

COPY requirements.txt .

RUN pip install -r requirements.txt

# isso é para copiar o restante do código-fonte do Workspace
COPY . .

# porta que o django vai rodar em localhost
EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate




