
# Gemini TTS Web App

A simple Flask web application that converts text into speech (Text-to-Speech) using the Google AI Gemini API.

## ✨ Features

- 🗣️ Convert text to speech (TTS) with natural voices.
- 🌐 Intuitive web interface.
- 🔗 REST API for automation and integrations.
- 💾 Audio output in WAV format.
- 🐳 Docker support.

---

## 🔑 How to Get Your API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey).
2. Log in with your Google account.
3. Click **"Create API Key"**.
4. Copy your generated API key — it will look like:

```
AIza...
```

---

## 🔐 How to Configure the API Key

### ✅ Option 1 — Directly in the Code (Simple)

Open `app.py` and replace:

```python
client = genai.Client(api_key="CHAVE_DA_API")
```

With:

```python
client = genai.Client(api_key="YOUR_API_KEY")
```

---

### ✅ Option 2 — Using Environment Variables (Recommended)

In `app.py`, replace:

```python
client = genai.Client(api_key="CHAVE_DA_API")
```

With:

```python
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
```

Then create a `.env` file in the project root with:

```
GOOGLE_API_KEY=YOUR_API_KEY
```

At the top of `app.py`, add:

```python
from dotenv import load_dotenv
load_dotenv()
```

Install the dotenv package if needed:

```bash
pip install python-dotenv
```

---

## 📦 Project Structure

```
GeminiTTSWebApp/
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Web interface
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image
├── docker-compose.yml     # Docker orchestration
```

---

## 🚀 Installation and Running

### ✅ Prerequisites

- Python 3.8+
- pip
- (Optional) Conda
- (Optional) Docker and Docker Compose

---

### ▶️ Running with Python and `venv`

```bash
cd GeminiTTSWebApp

python -m venv venv

# Windows:
venv\Scripts\ctivate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

Access:

```
http://127.0.0.1:5000
```

---

### ▶️ Running with Conda

```bash
conda create -n geminitts python=3.10
conda activate geminitts
pip install -r requirements.txt
python app.py
```

---

## 🐳 Running with Docker

### Using Docker Compose (Recommended)

```bash
docker-compose up --build
```

### Or manually with Docker

```bash
docker build -t geminitts .
docker run -p 5000:5000 -e GOOGLE_API_KEY=YOUR_API_KEY geminitts
```

Access:

```
http://localhost:5000
```

---

## 🌐 How to Use the Web Interface

1. Open:

```
http://localhost:5000
```

2. Enter the text you want to convert.
3. Select the voice (e.g., `Zephyr`).
4. Click **"Generate Audio"**.
5. Download or listen to the generated audio.

---

## 🔗 REST API Usage

### 📮 Endpoint

```
POST /api/generate
```

### 📥 Request Body

```json
{
  "text": "Your text here",
  "voice": "Zephyr"
}
```

- `text`: (required) The text to convert.
- `voice`: (required) Voice name. Example: `Zephyr`, `CloudNarrator`, etc.

### 📤 Response

- Returns a `.wav` file with the generated audio.

### 🧪 Curl Example

```bash
curl -X POST http://127.0.0.1:5000/api/generate -H "Content-Type: application/json" -d '{"text":"Hello, welcome to Gemini TTS Web App","voice":"Zephyr"}' --output output.wav
```

---

## ⚠️ Important Notes

- ✅ Available voices depend on the Gemini model and API permissions.
- ⚙️ Make sure to set up your API key properly at [Google AI Studio](https://aistudio.google.com/apikey).

---

## 📜 License

MIT License
