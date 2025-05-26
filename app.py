from flask import Flask, request, jsonify, send_file, render_template
from google import genai
from google.genai import types
import wave
import os
import io
from dotenv import load_dotenv # Importa load_dotenv para carregar variáveis de ambiente

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__, template_folder='templates') # Define a pasta 'templates' para o HTML

# Carrega a chave da API da variável de ambiente
# É crucial definir GEMINI_API_KEY no seu ambiente ou no arquivo .env
API_KEY = os.getenv("GEMINI_API_KEY") 

# Verifica se a chave da API foi carregada
if not API_KEY:
    print("ERRO: A variável de ambiente GEMINI_API_KEY não está definida.")
    print("Por favor, defina-a antes de executar a aplicação.")
    # Em um ambiente de produção, você pode querer sair ou lançar uma exceção.
    # Para desenvolvimento, continuaremos, mas as chamadas à API falharão.

client = genai.Client(api_key=API_KEY) # Usa a chave carregada

def salvar_wave_em_memoria(pcm):
    """Salva dados PCM em um buffer de memória no formato WAV."""
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
    """Rota principal que serve o arquivo index.html."""
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def gerar_audio():
    """
    Endpoint para gerar áudio a partir de texto usando a API Gemini TTS.
    Recebe 'text' e 'voice' no corpo da requisição JSON.
    """
    data = request.json

    # Validação básica dos dados de entrada
    if not data or 'text' not in data or 'voice' not in data:
        return jsonify({'error': 'Por favor, envie "text" e "voice" no JSON.'}), 400

    texto = data['text']
    voz = data['voice']

    try:
        # Chama a API Gemini para gerar conteúdo de áudio
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts", # Modelo de Text-to-Speech
            contents=texto,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"], # Solicita uma resposta de áudio
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voz # Usa a voz selecionada pelo usuário
                        )
                    )
                ),
            )
        )

        # Extrai os dados de áudio da resposta
        data_audio = response.candidates[0].content.parts[0].inline_data.data
        audio_buffer = salvar_wave_em_memoria(data_audio)

        # Retorna o arquivo de áudio como um anexo WAV
        return send_file(
            audio_buffer,
            mimetype="audio/wav",
            as_attachment=True,
            download_name="output.wav"
        )

    except Exception as e:
        # Captura e retorna erros da API ou do processo de geração
        print(f"Erro ao gerar áudio: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    # Cria a pasta 'templates' se não existir (para o index.html)
    if not os.path.exists("templates"):
        os.makedirs("templates")
    
    # Executa a aplicação Flask
    # host="0.0.0.0" torna a aplicação acessível de qualquer IP (útil em Docker)
    # port=5000 é a porta padrão
    # debug=True habilita o modo de depuração (recarregamento automático, etc.)
    app.run(host="0.0.0.0", port=5000, debug=True)
