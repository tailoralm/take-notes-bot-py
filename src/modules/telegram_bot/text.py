import os
from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

from src.shared.enum.folders import Folders
from src.shared.utils import general as general_utils

class TextController:
    def __init__(self, ctx):
        self.ctx = ctx

    def log_message(self):
        message = self.ctx.message  # Assuming the message is an instance of telegram.Message
        date_time = general_utils.format_full_date_time(datetime.now())
        log_entry = f"{date_time}: {message.text}\n"

        name_file = f"{Folders.notes.value}.log"  # Get the path from the Folders enum

        try:
            with open(name_file, "a") as log_file:
                log_file.write(log_entry)
        except Exception as err:
            print(f"Error logging message: {err}")


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # document = update.message.document
    controller = TextController(context)
    controller.log_message()