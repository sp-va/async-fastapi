from uuid import uuid4
from pathlib import Path
from PIL import Image
from io import BytesIO
import aiofiles

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/documents",
    tags=["documents",]
)

# @router.post("/upload_file")
# async def documents_root(pictures: UploadFile):
#     #for pic in pictures:
#         #pic.filename = str(uuid4())
#     file_path = f'/{pictures.filename}'
#     async with await open(file_path, "wb") as file:
#         content = await pictures.file.read()
#         await file.write(content)
#             #return "Все норм"
   
@router.post("/upload_file")
async def documents_root(picture: UploadFile = File(...)):
    picture_uuid = uuid4()
    file_path = f"{Path(__file__).parent.parent}/media/{picture_uuid}.png"
    content = await picture.read()
    pic = Image.open(BytesIO(content))
    buffer = BytesIO()
    pic.save(buffer, format='JPEG')

    async with aiofiles.open(file_path, "wb") as file:
        await file.write(buffer.getbuffer())   
    return picture