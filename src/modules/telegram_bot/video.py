from telegram import Update
from telegram.ext import ContextTypes
from .shared.save_files_abstract import SaveFilesAbstractController
from src.shared.enum.folders import Folders


class VideoController(SaveFilesAbstractController):
    def __init__(self):
        super().__init__(Folders.videos.value)

    def save_video(self, update: Update):
        message = update.message
        file_id = message.video.file_id

        file_name = self.get_filename(
            message.caption if message.caption else 'video',
            message.video.file_name if message.video.file_name else ''
        )
        return self.download_and_save_file(update, file_id, file_name)

    def get_filename(self, text: str, file_name: str) -> str:
        if file_name:
            file_name = file_name + '_'
        return f"{text}_{file_name}{self.get_string_date()}.mp4"


async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await VideoController().save_video(update)
