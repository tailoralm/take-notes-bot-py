from telegram import Update
from telegram.ext import ContextTypes

from src.modules.telegram_bot.shared.save_files_abstract import SaveFilesAbstractController
from src.shared.enum.folders import Folders


class DocumentController(SaveFilesAbstractController):
    def __init__(self, ctx, folder=Folders.docs):
        super().__init__(ctx, folder)

    def save_doc(self):
        message = self.ctx.message
        file_name = self.get_filename('doc', message.document.file_name)
        self.download_and_save_file(message.document.file_id, file_name)

    def save_replied_doc(self):
        message = self.ctx.message
        message_replied = message.reply_to_message

        split_caption = message.text.split(' ')
        file_name = split_caption[1] if len(split_caption) > 1 else 'doc'

        self.download_and_save_file(
            message_replied.document.file_id,
            self.get_filename(file_name, message_replied.document.file_name)
        )

    def get_filename(self, text: str, file_name: str) -> str:
        return f"{text}_{self.get_string_date()}_{file_name}"


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # document = update.message.document
    controller = DocumentController(context)
    controller.save_doc()
