
from flask import Flask, request, jsonify, send_file, render_template
from google import genai
from google.genai import types
import wave
import os
import io

app = Flask(__name__)

client = genai.Client(api_key="CHAVE_DA_API")  # ✅ Coloque sua chave aqui


def salvar_wave_em_memoria(pcm):
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(pcm)
    buffer.seek(0)
    return buffer


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/generate', methods=['POST'])
def gerar_audio():
    data = request.json

    if not data or 'text' not in data or 'voice' not in data:
        return jsonify({'error': 'Por favor, envie "text" e "voice" no JSON.'}), 400

    texto = data['text']
    voz = data['voice']

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=texto,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voz
                        )
                    )
                ),
            )
        )

        data_audio = response.candidates[0].content.parts[0].inline_data.data
        audio_buffer = salvar_wave_em_memoria(data_audio)

        return send_file(
            audio_buffer,
            mimetype="audio/wav",
            as_attachment=True,
            download_name="output.wav"
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    app.run(host="0.0.0.0", port=5000, debug=True)
