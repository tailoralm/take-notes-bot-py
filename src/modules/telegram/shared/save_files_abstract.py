from abc import ABC, abstractmethod
import os
from datetime import datetime
from src.shared.utils.general import download_file
from src.shared.enum.folders import EFolders


class SaveFilesAbstractController(ABC):
    def __init__(self, ctx, folder=EFolders.general):
        self.ctx = ctx
        self.folder = folder

    async def download_and_save_file(self, file_id: str, file_name: str) -> str:
        file_url = await self.ctx.telegram.get_file_link(file_id)
        file_path = os.path.join(self.folder.value, file_name)  # Ensure to get the value of the enum
        print('Saving:', file_path)

        path = await download_file(file_url, file_path)
        await self.ctx.reply('Saved!')
        return path

    def get_string_date(self) -> str:
        today = datetime.now()
        return f"{today.year}_{today.month}_{today.day}"

    def get_filename(self, text: str, file_id: str) -> str:
        split_caption = text.split(' ')
        file_name = split_caption[1] if len(split_caption) > 1 else 'undefined'
        return f"{file_name}_{self.get_string_date()}_{file_id}"
