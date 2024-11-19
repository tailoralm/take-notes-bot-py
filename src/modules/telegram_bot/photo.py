from telegram import Update
from telegram.ext import ContextTypes
from .shared.save_files_abstract import SaveFilesAbstractController
from src.shared.enum.folders import Folders


class PhotoController(SaveFilesAbstractController):
    def __init__(self):
        super().__init__(Folders.photos.value)

    def save_photo(self, update: Update):
        message = update.message
        largest_photo = max(message.photo, key=lambda photo: photo.file_size)
        file_name = self.get_filename(message.caption or 'photo')
        return super().download_and_save_file(update, largest_photo.file_id, file_name)

    def get_filename(self, text: str) -> str:
        return f"{text}_{self.get_string_date()}.jpg"


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await PhotoController().save_photo(update)
