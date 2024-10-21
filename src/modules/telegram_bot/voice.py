from telegram import Message, Update
from telegram.ext import ContextTypes

from shared.save_files_abstract import SaveFilesAbstractController
from src.shared.enum.folders import Folders
from services.voice_processor import VoiceProcessorService
from datetime import datetime


class VoiceController(SaveFilesAbstractController):
    def __init__(self, ctx):
        super().__init__(ctx, Folders.voices)
        self.voice_processor_service = VoiceProcessorService()

    def save_voice(self):
        message = self.ctx.message  # Assuming this is an instance of telegram.Message.VoiceMessage
        voice_file_id = message.voice.file_id

        self.download_file_and_transcribe(voice_file_id, self.get_filename('voice'))

    def save_replied_voice(self):
        message = self.ctx.message  # Assuming this is an instance of telegram.Message.TextMessage
        message_replied = message.reply_to_message  # Assuming this is an instance of telegram.Message.VoiceMessage

        voice_file_id = message_replied.voice.file_id
        split_caption = message.text.split(' ')
        file_name = split_caption[1] if len(split_caption) > 1 else 'voice'

        self.download_file_and_transcribe(voice_file_id, self.get_filename(file_name))

    async def download_file_and_transcribe(self, voice_file_id: str, file_name: str):
        # Download and save the file
        path = await super().download_and_save_file(voice_file_id, file_name)
        # Process the file
        await self.voice_processor_service.upload_voice_file(path)

    def get_filename(self, text: str) -> str:
        date_iso = datetime.now().isoformat()
        return f"{text}_{date_iso.replace(':', '-')}.ogg"

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # document = update.message.document
    controller = VoiceController(context)
    controller.save_voice()
