from uuid import uuid4
from pathlib import Path
from PIL import Image
from io import BytesIO
import aiofiles

from fastapi import APIRouter, UploadFile, File, status, HTTPException
from fastapi.responses import FileResponse

from transactions.insert_data import upload_picture
from db.base import AsyncSessionLocal

router = APIRouter(
    prefix="/documents",
    tags=["documents",]
)
   
@router.post("/upload_file", status_code=status.HTTP_201_CREATED)
async def documents_root(picture: UploadFile = File(...)):
    picture_uuid = uuid4()
    file_path = f"{Path(__file__).parent.parent}/media/{picture_uuid}.png"
    content = await picture.read()
    pic = Image.open(BytesIO(content))
    buffer = BytesIO()
    pic.save(buffer, format='JPEG')

    async with aiofiles.open(file_path, "wb") as file:
        try:
            await file.write(buffer.getbuffer())
            await upload_picture(
                async_session=AsyncSessionLocal,
                file_id=picture_uuid,
                file_path=file_path,
            )
        except:
            raise HTTPException(status_code=400, detail="Возникла ошибка при сохранении изображения или при добавлении записи о нем в базу данных.") 