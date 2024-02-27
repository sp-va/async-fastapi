import pytesseract
from PIL import Image
import time

async def analyze_picture(file_path: str):
    text = pytesseract.image_to_string(Image.open(file_path), lang="rus+eng")
    time.sleep(10)
    return text