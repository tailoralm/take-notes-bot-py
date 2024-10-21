from abc import ABC
import os
from datetime import datetime
from src.shared.utils.general import download_file
from src.shared.enum.folders import Folders


class SaveFilesAbstractController(ABC):
    def __init__(self, ctx, folder=Folders.general):
        self.ctx = ctx
        self.folder = folder

    async def download_and_save_file(self, file_id: str, file_name: str) -> str:
        file_url = await self.ctx.telegram.get_file_link(file_id)
        file_path = os.path.join(self.folder.value, file_name)
        print('Saving:', file_path)

        path = await download_file(file_url, file_path)
        await self.ctx.reply('Saved!')
        return path

    def get_string_date(self) -> str:
        today = datetime.now()
        return f"{today.year}_{today.month}_{today.day}"
