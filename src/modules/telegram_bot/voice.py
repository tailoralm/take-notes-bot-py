from telegram import Update
from datetime import datetime
from telegram.ext import ContextTypes
from .shared.save_files_abstract import SaveFilesAbstractController
from src.shared.enum.folders import Folders
from .services.voice_processor import VoiceProcessorService


class VoiceController(SaveFilesAbstractController):
    def __init__(self):
        super().__init__(Folders.voices.value)
        self.voice_processor_service = VoiceProcessorService()

    async def save_voice(self, update: Update):
        voice_file_id = update.message.voice.file_id
        path = await self.download_and_save_file(update, voice_file_id, self.get_filename('voice'))
        return self.voice_processor_service.transcribe_voice(path)


    @staticmethod
    def get_filename(text: str) -> str:
        date_iso = datetime.now().isoformat()
        return f"{text}_{date_iso.replace(':', '-')}.ogg"


async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await VoiceController().save_voice(update)
