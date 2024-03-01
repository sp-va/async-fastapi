from celery import Celery

import pytesseract
from PIL import Image
from datetime import time

app = Celery(
    "tasks",
    broker="pyamqp://vadim:qwerasdf@localhost:5672/myvhost",
)

@app.task
def analyze_picture(file_path: str):
    text = pytesseract.image_to_string(Image.open(file_path), lang="rus+eng")
    time.sleep(5)
    return text

