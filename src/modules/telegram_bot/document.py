from telegram import Update
from telegram.ext import ContextTypes
from src.modules.telegram_bot.shared.save_files_abstract import SaveFilesAbstractController
from src.shared.enum.folders import Folders


class DocumentController(SaveFilesAbstractController):
    def __init__(self):
        super().__init__(Folders.docs.value)

    def save_doc(self, update: Update):
        document = update.message.document
        file_name = self.get_filename('doc', document.file_name)
        return self.download_and_save_file(update, document.file_id, file_name)

    def get_filename(self, text: str, file_name: str) -> str:
        return f"{text}_{self.get_string_date()}_{file_name}"


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await DocumentController().save_doc(update)
