def get_file_id(photos: list) -> str:
    if not photos:
        return None

    # Find the photo with the largest file_size
    largest_photo = max(photos, key=lambda photo: photo.get('file_size', 0))

    return largest_photo.get('file_id')