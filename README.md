
# Gemini TTS Web App

A simple Flask web application that converts text into speech (Text-to-Speech) using the Google AI Gemini API.

## ✨ Features

- 🗣️ Convert text to speech (TTS) with natural voices.
- 🌐 Intuitive web interface.
- 🔗 REST API for automation and integrations.
- 🎧 Audio output in WAV format.
- 📦 Simple frontend with HTML (index.html inside `templates/`).
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

### ✅ Using Environment Variables (Recommended)

1. Create a file named `.env` in the root of the project.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

2. The application automatically loads this `.env` file using `python-dotenv`.

If not installed, run:

```bash
pip install python-dotenv
```

---

## 📦 Project Structure

```
GeminiTTSWebApp/
├── app.py                 # Flask backend with API and web interface
├── templates/
│   └── index.html         # Web interface
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image
├── docker-compose.yml     # Docker orchestration
├── README.md              # English documentation
├── README_pt-BR.md        # Portuguese documentation
```

---

## 🚀 Running the Application

### ▶️ Using Python (Recommended)

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

### ▶️ Using Conda

```bash
conda create -n geminitts python=3.10
conda activate geminitts
pip install -r requirements.txt
python app.py
```

---

## 🐳 Running with Docker

### Using Docker Compose

```bash
docker-compose up --build
```

### Or manually:

```bash
docker build -t geminitts .
docker run -p 5000:5000 -e GEMINI_API_KEY=YOUR_API_KEY geminitts
```

---

## 🌐 Web Interface Usage

1. Open:

```
http://localhost:5000
```

2. Enter the text you want to convert.
3. Select the voice (e.g., `Zephyr`, `CloudNarrator`, etc.).
4. Click **"Generate Audio"**.
5. Download and listen to the generated `.wav` file.

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

### 📤 Response

- Returns a `.wav` audio file.

### 🧪 Curl Example

```bash
curl -X POST http://127.0.0.1:5000/api/generate -H "Content-Type: application/json" -d '{"text":"Hello, welcome to Gemini TTS Web App","voice":"Zephyr"}' --output output.wav
```

---

## ⚠️ Notes

- ✅ Voices availability depends on your Gemini model and permissions.
- ⚙️ The web app and API will not work without configuring your API key in `.env`.

---

## 📜 License

MIT License
