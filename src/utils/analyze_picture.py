import pytesseract
from PIL import Image
import time

from celery_worker.tasks import app

@app.task
def analyze_picture(file_path: str):
    text = pytesseract.image_to_string(Image.open(file_path), lang="rus+eng")
    time.sleep(5)
    return text