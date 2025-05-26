
# Imagem base
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta
EXPOSE 5000

# Comando para rodar
CMD ["python", "app.py"]
