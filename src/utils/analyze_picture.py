import pytesseract
from PIL import Image
from pathlib import Path

async def analyze_picture(file_path: str):
    text = pytesseract.image_to_string(Image.open(file_path), lang="rus+eng")
    return text