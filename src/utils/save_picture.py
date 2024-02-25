import aiofiles
from fastapi import File, UploadFile
from PIL import Image
from io import BytesIO
from typing import Optional

# Функция для сохранения загруженной юзером картинки, чтобы это сохранение происходило внутри транзакции по добавлению записи об этой картинки в БД
async def save_picture(file_path: str, picture: UploadFile = File(...)):
    content = await picture.read()
    pic = Image.open(BytesIO(content))
    buffer = BytesIO()
    pic.save(buffer, format='PNG')

    async with aiofiles.open(file_path, "wb") as file:
        try:
            await file.write(buffer.getbuffer())
        except:
            raise Exception
    