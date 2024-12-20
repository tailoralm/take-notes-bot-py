from dotenv import load_dotenv
load_dotenv()

from src.shared.enum.folders import Folders
from src.shared.utils.general import ensure_directory_existence
from src.modules.telegram_bot.router import Router


for folder in Folders:
    ensure_directory_existence(f"{folder.value}/any.jpg")

Router()
