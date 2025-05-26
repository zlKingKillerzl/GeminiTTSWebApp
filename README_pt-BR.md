
# Gemini TTS Web App

Uma aplicação simples com Flask que permite converter texto em fala (Text-to-Speech) utilizando a API do Google AI Gemini.

## ✨ Funcionalidades

- 🗣️ Conversão de texto para fala (TTS) com vozes naturais.
- 🌐 Interface web intuitiva.
- 🔗 API REST para automação e integrações.
- 💾 Retorno de áudio em formato WAV.
- 🐳 Suporte a Docker.

---

## 🔑 Como Obter Sua Chave de API

1. Acesse o [Google AI Studio](https://aistudio.google.com/apikey).
2. Faça login na sua conta Google.
3. Clique em **"Create API Key"**.
4. Copie sua chave gerada — ela será algo como:

```
AIza...
```

---

## 🔐 Como Configurar a Chave no Projeto

### ✅ Opção 1 — Diretamente no Código (Simples)

Abra o arquivo `app.py` e substitua:

```python
client = genai.Client(api_key="CHAVE_DA_API")
```

Por:

```python
client = genai.Client(api_key="SUA_CHAVE_AQUI")
```

---

### ✅ Opção 2 — Usando Variável de Ambiente (Recomendado)

No `app.py`, substitua:

```python
client = genai.Client(api_key="CHAVE_DA_API")
```

Por:

```python
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
```

Depois, crie um arquivo `.env` na raiz do projeto:

```
GOOGLE_API_KEY=SUA_CHAVE_AQUI
```

E adicione no início do `app.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

Instale a biblioteca se ainda não tiver:

```bash
pip install python-dotenv
```

---

## 📦 Estrutura do Projeto

```
GeminiTTSWebApp/
├── app.py                 # Backend Flask
├── templates/
│   └── index.html         # Interface Web
├── requirements.txt       # Dependências Python
├── Dockerfile             # Imagem Docker
├── docker-compose.yml     # Orquestração Docker
```

---

## 🚀 Como Instalar e Executar

### ✅ Pré-requisitos

- Python 3.8 ou superior
- pip
- (Opcional) Conda
- (Opcional) Docker e Docker Compose

---

### ▶️ Usando Python com `venv`

```bash
cd GeminiTTSWebApp

python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

Acesse:

```
http://127.0.0.1:5000
```

---

### ▶️ Usando Conda

```bash
conda create -n geminitts python=3.10
conda activate geminitts
pip install -r requirements.txt
python app.py
```

---

## 🐳 Como Executar com Docker

### 🔧 Usando Docker Compose

```bash
docker-compose up --build
```

### 🐳 Docker Manual

```bash
docker build -t geminitts .
docker run -p 5000:5000 -e GOOGLE_API_KEY=SUA_CHAVE_AQUI geminitts
```

Acesse:

```
http://localhost:5000
```

---

## 🌐 Como Usar a Interface Web

1. Acesse:

```
http://localhost:5000
```

2. Digite o texto que deseja converter.
3. Escolha a voz (ex.: `Zephyr`).
4. Clique em **"Gerar Áudio"**.
5. Baixe ou escute o áudio gerado.

---

## 🔗 API REST

### 📮 Endpoint

```
POST /api/generate
```

### 📥 Corpo da Requisição

```json
{
  "text": "Seu texto aqui",
  "voice": "Zephyr"
}
```

- `text`: (obrigatório) Texto a ser convertido.
- `voice`: (obrigatório) Nome da voz. Exemplo de vozes: `Zephyr`, `CloudNarrator`, etc.

### 📤 Resposta

- Retorna um arquivo `.wav` com o áudio gerado.

### 🧪 Exemplo com curl

```bash
curl -X POST http://127.0.0.1:5000/api/generate \
-H "Content-Type: application/json" \
-d '{"text":"Olá, bem-vindo ao Gemini TTS Web App","voice":"Zephyr"}' --output output.wav
```

---

## ⚠️ Observações Importantes

- ✅ As vozes disponíveis dependem do modelo Gemini e das permissões da API.
- ⚙️ Configure corretamente sua chave API no Google AI Studio ([https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)).

---

## 📜 Licença

MIT License
