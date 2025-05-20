from openai import OpenAI

client = OpenAI(
    api_key="sk-secret",
    base_url="http://10.11.22.178/api/whisper/v1"
)

# Path to your audio file
audio_file_path = "common_voice_yue_31209989.mp3"  # Replace with your audio file path

try:
    with open(audio_file_path, "rb") as audio_file:
        # Transcribe the audio file
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="openai/whisper-large-v3"  # You can use other models if available
        )
    
    # Print the transcription text
    print("Transcription:", transcription.text)
except Exception as e:
    print(f"An error occurred: {str(e)}")