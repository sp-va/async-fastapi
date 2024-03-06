import time
import pathlib
import pytesseract
from PIL import Image
import celery_config

from transactions import insert_data, retrieve_data


@celery_config.worker.task
def analyze_picture(picture_id: str):
    print(pathlib.Path(__file__).parent)
    file_path = retrieve_data.get_document_picture(picture_id=picture_id)
    text = pytesseract.image_to_string(Image.open(file_path), lang="rus+eng")
    time.sleep(5)
    insert_data.add_text(picture_id=picture_id, text=text)
    return text

