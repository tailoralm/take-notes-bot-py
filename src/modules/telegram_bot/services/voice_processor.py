import os
import shutil
import logging
from whisper import load_model


class VoiceProcessorService:
    def __init__(self):
        self.logger = self.setup_logger()
        self.model = load_model("base")

    def setup_logger(self):
        logger = logging.getLogger('VoiceProcessorService')
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    def upload_voice_file(self, file_path: str):
        # In this case, upload is not required. We can simply log the action
        self.logger.info(f'Processing voice file: {file_path}')
        self.transcribe_voice(file_path)

    def transcribe_voice(self, file_path: str):
        # Use Whisper to transcribe the voice file
        self.logger.info(f'Transcribing file: {file_path}')
        transcription = self.model.transcribe(file_path, language='pt')

        # Save the transcription to a text file
        text_file_path = self.get_transcription_file_path(file_path)
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(transcription['text'])

        self.logger.info(f'Transcription saved: {text_file_path}')

        # Move the original voice file to processed folder
        self.move_voice_file_to_processed_folder(file_path)

    def get_transcription_file_path(self, voice_file_path: str) -> str:
        base, _ = os.path.splitext(voice_file_path)
        return f"{base}_transcription.txt"

    def move_voice_file_to_processed_folder(self, file_path: str):
        try:
            processed_folder_path = os.path.join(os.path.dirname(file_path), 'processed')
            os.makedirs(processed_folder_path, exist_ok=True)

            destination_path = os.path.join(processed_folder_path, os.path.basename(file_path))
            shutil.move(file_path, destination_path)

            self.logger.info('File moved to processed folder successfully')
        except Exception as e:
            self.logger.error(f'Error moving file to processed folder: {e}')

    def process_voice_folder(self, folder_path: str):
        """Processes all voice files in a given folder."""
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and file_path.endswith('.ogg'):
                self.upload_voice_file(file_path)
