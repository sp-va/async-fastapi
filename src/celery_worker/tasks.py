import pytesseract
from PIL import Image
import time
from celery import shared_task

from transactions.insert_data import add_text
from transactions.retrieve_data import get_document_picture

@shared_task
def analyze_picture(picture_id: str):
    file_path = get_document_picture(picture_id=picture_id)
    text = pytesseract.image_to_string(Image.open(file_path), lang="rus+eng")
    time.sleep(5)
    add_text(picture_id=picture_id, text=text)
    return text

