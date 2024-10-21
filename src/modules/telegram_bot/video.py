from telegram import Update
from telegram.ext import ContextTypes

from shared.save_files_abstract import SaveFilesAbstractController
from src.shared.enum.folders import Folders


class VideoController(SaveFilesAbstractController):
    def __init__(self, ctx, folder=Folders.videos.value):
        super().__init__(ctx, folder)

    def save_video(self):
        message = self.ctx.message
        file_id = message.video.file_id

        file_name = self.get_filename(
            message.caption if message.caption else 'video',
            message.video.file_name if message.video.file_name else ''
        )
        return super().download_and_save_file(file_id, file_name)

    def save_replied_video(self):
        message = self.ctx.message
        message_replied = message.reply_to_message

        file_id = message_replied.video.file_id
        split_caption = message.text.split(' ')
        file_name = split_caption[1] if len(split_caption) > 1 else 'video'

        super().download_and_save_file(file_id, self.get_filename(file_name, ''))

    def get_filename(self, text: str, file_name: str) -> str:
        if file_name:
            file_name = file_name + '_'
        return f"{text}_{file_name}{self.get_string_date()}.mp4"


async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # document = update.message.photo
    controller = VideoController(context)
    await controller.save_video()