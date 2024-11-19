import os
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

from src.shared.enum.folders import Folders
from src.shared.utils import general as general_utils


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    date_time = general_utils.format_full_date_time(datetime.now())
    log_entry = f"{date_time}: {message.text}\n"

    name_file = os.path.join(Folders.notes.value, "notes.log")

    try:
        with open(name_file, "a") as log_file:
            log_file.write(log_entry)
    except Exception as err:
        print(f"Error logging message: {err}")
