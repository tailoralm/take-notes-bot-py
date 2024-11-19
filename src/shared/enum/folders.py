import os
from enum import Enum

DEFAULT_PATH = os.environ.get('DATA_DIR', 'DATA_DIR/bot-documents/')


class Folders(Enum):
    docs = os.path.join(DEFAULT_PATH, 'docs')
    receipts = os.path.join(DEFAULT_PATH, 'docs', 'receipts')
    photos = os.path.join(DEFAULT_PATH, 'album')
    videos = os.path.join(DEFAULT_PATH, 'album')
    random = os.path.join(DEFAULT_PATH, 'random')
    notes = DEFAULT_PATH
    voices = os.path.join(DEFAULT_PATH, 'voices')
    processedVoices = os.path.join(DEFAULT_PATH, 'voices', 'processed')
    general = os.path.join(DEFAULT_PATH, 'files')
