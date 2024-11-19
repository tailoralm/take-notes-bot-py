import os
import shutil
from whisper import load_model


class VoiceProcessorService:
    def __init__(self):
        self.model = load_model("base")

    def transcribe_voice(self, file_path: str):
        print(f'Transcribing file: {file_path}')
        try:
            transcription = self.model.transcribe(file_path, language='pt', )
            base, _ = os.path.splitext(file_path)
            text_file_path = f"{base}_transcription.txt"
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(transcription['text'])

            print(f'Transcription saved: {text_file_path}')
            processed_folder_path = os.path.join(os.path.dirname(file_path), 'processed')
            os.makedirs(processed_folder_path, exist_ok=True)

            destination_path = os.path.join(processed_folder_path, os.path.basename(file_path))
            shutil.move(file_path, destination_path)

            print('File moved to processed folder successfully')
        except Exception as e:
            print(f'Error transcribing voice: {e}')

