from abc import ABC
import os
from datetime import datetime
from telegram import Update
from src.shared.utils.general import download_file
from src.shared.enum.folders import Folders


class SaveFilesAbstractController(ABC):
    def __init__(self, folder=Folders.general.value):
        self.folder = folder

    async def download_and_save_file(self, update: Update, file_id: str, file_name: str) -> str:
        bot = update.get_bot()
        file = await bot.get_file(file_id)
        file_url = file.file_path

        file_path = os.path.join(self.folder, file_name)
        print('Saving:', file_path)

        path = download_file(file_url, file_path)
        await update.message.reply_text('Saved!')
        return path

    @staticmethod
    def get_string_date() -> str:
        today = datetime.now()
        return f"{today.year}_{today.month}_{today.day}"
