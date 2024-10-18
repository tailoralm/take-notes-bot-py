import os
import requests
from datetime import datetime


def download_file(file_url: str, file_path: str) -> str:
    response = requests.get(file_url, stream=True)

    unique_path = generate_unique_filename(file_path)

    ensure_directory_existence(unique_path)

    with open(unique_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return unique_path


def generate_unique_filename(filename: str) -> str:
    base_name = os.path.basename(filename).rsplit('.', 1)[0]
    extension = os.path.splitext(filename)[1]
    dirname = os.path.dirname(filename)
    unique_filename = filename
    counter = 1

    while os.path.exists(unique_filename):
        unique_filename = f"{dirname}/{base_name} ({counter}){extension}"
        counter += 1

    return unique_filename


def ensure_directory_existence(file_path: str):
    dirname = os.path.dirname(file_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def format_full_date_time(date: datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M:%S")


def append_notes_file(file_name: str, log_entry: str):
    try:
        with open(file_name, 'a') as f:
            f.write(log_entry + "\n")
    except Exception as e:
        print(f"Error logging message: {e}")
