FROM python:3.13.1-slim-bullseye

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos do projeto
COPY . .

# Instalar dependências de produção (certifique-se de que o arquivo requirements/prod.txt existe)
RUN pip3 install --no-cache-dir -r requirements/prod.txt

# Expor a porta 8000
EXPOSE 8000

# Comando para rodar o Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
