
# Gemini TTS Web App

Uma aplicação simples com Flask que permite converter texto em fala (Text-to-Speech) utilizando a API do Google AI Gemini.

## ✨ Funcionalidades

- 🗣️ Conversão de texto para fala (TTS) com vozes naturais.
- 🌐 Interface web intuitiva.
- 🔗 API REST para automação e integrações.
- 🎧 Geração de áudio no formato WAV.
- 📦 Frontend simples em HTML (`index.html` dentro da pasta `templates/`).
- 🐳 Suporte a Docker.

---

## 🔑 Como Obter Sua Chave de API

1. Acesse o [Google AI Studio](https://aistudio.google.com/apikey).
2. Faça login com sua conta Google.
3. Clique em **"Create API Key"**.
4. Copie sua chave gerada — ela será algo como:

```
AIza...
```

---

## 🔐 Como Configurar a Chave no Projeto

### ✅ Usando Variável de Ambiente (Recomendado)

1. Crie um arquivo chamado `.env` na raiz do projeto.

```env
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

2. A aplicação carrega automaticamente esse `.env` usando `python-dotenv`.

Se não tiver instalado, rode:

```bash
pip install python-dotenv
```

---

## 📦 Estrutura do Projeto

```
GeminiTTSWebApp/
├── app.py                 # Backend Flask com API e interface web
├── templates/
│   └── index.html         # Interface web
├── requirements.txt       # Dependências Python
├── Dockerfile             # Imagem Docker
├── docker-compose.yml     # Orquestração Docker
├── README.md              # Documentação em inglês
├── README_pt-BR.md        # Documentação em português
```

---

## 🚀 Como Executar a Aplicação

### ▶️ Usando Python (Recomendado)

```bash
cd GeminiTTSWebApp

python -m venv venv
# Windows:
venv\Scriptsctivate
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

## 🐳 Executando com Docker

### Com Docker Compose

```bash
docker-compose up --build
```

### Ou manualmente:

```bash
docker build -t geminitts .
docker run -p 5000:5000 -e GEMINI_API_KEY=SUA_CHAVE_AQUI geminitts
```

---

## 🌐 Como Usar a Interface Web

1. Acesse:

```
http://localhost:5000
```

2. Digite o texto que deseja converter.
3. Escolha a voz (ex.: `Zephyr`, `CloudNarrator`, etc.).
4. Clique em **"Gerar Áudio"**.
5. Baixe e escute o áudio gerado (`.wav`).

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

### 📤 Resposta

- Retorna um arquivo `.wav` com o áudio gerado.

### 🧪 Exemplo com curl

```bash
curl -X POST http://127.0.0.1:5000/api/generate -H "Content-Type: application/json" -d '{"text":"Olá, bem-vindo ao Gemini TTS Web App","voice":"Zephyr"}' --output output.wav
```

---

## ⚠️ Observações

- ✅ A disponibilidade das vozes depende do modelo Gemini e das permissões da API.
- ⚙️ A aplicação web e API não funcionarão sem configurar sua chave de API no `.env`.

---

## 📜 Licença

MIT License
