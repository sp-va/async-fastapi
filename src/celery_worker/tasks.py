import pytesseract
from PIL import Image
import time

from celery_config import worker


@worker.task(name="celery_worker.tasks.analyze_picture")
def analyze_picture(file_path: str):
    text = pytesseract.image_to_string(Image.open(file_path), lang="rus+eng")
    time.sleep(5)
    return text

