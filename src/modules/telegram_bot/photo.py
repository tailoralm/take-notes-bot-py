from telegram import Update
from telegram.ext import ContextTypes

from src.shared.utils import photo as photo_utils
from shared.save_files_abstract import SaveFilesAbstractController
from src.shared.enum.folders import Folders


class PhotoController(SaveFilesAbstractController):
    def __init__(self, ctx, folder=Folders.photos):
        super().__init__(ctx, folder)

    async def save_photo(self):
        # Assuming ctx.message contains a PhotoMessage object
        message = self.ctx.message

        # Extract the file ID using a utility function
        file_id = photo_utils.get_file_id(message.photo)

        # Generate a filename (assumes caption exists or defaults to 'photo')
        file_name = self.get_filename(message.caption or 'photo')

        # Call the parent method to download and save the file
        await super().download_and_save_file(file_id, file_name)

    async def save_replied_photo(self):
        # Extract the current message and the replied message (which contains the photo)
        message = self.ctx.message
        message_replied = message.reply_to_message

        # Extract the file ID from the replied photo message
        file_id = photo_utils.get_file_id(message_replied.photo)

        # Split the caption text and generate the filename
        split_caption = message.text.split(' ')
        file_name = split_caption[1] if len(split_caption) > 1 else 'photo'

        # Download and save the replied photo
        await super().download_and_save_file(file_id, self.get_filename(file_name))

    def get_filename(self, text: str) -> str:
        return f"{text}_{self.get_string_date()}.jpg"


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # document = update.message.photo
    controller = PhotoController(context)
    await controller.save_photo()