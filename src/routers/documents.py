from uuid import uuid4
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, status, HTTPException

from transactions.insert_data import upload_picture
from transactions.delete_data import delete_picture
from db.base import AsyncSessionLocal
from celery_worker.tasks import add_text

router = APIRouter(
    prefix="/documents",
    tags=["documents",]
)
   
@router.post("/upload_file", status_code=status.HTTP_201_CREATED)
async def upload_file(picture: UploadFile = File(...)):
    picture_uuid = uuid4()
    file_path = f"{Path(__file__).parent.parent}/media/{picture_uuid}.png"

    try:
        await upload_picture(
            async_session=AsyncSessionLocal,
            file_id=picture_uuid,
            file_path=file_path,
            picture=picture
        )
    except:
        raise HTTPException(status_code=400, detail="Возникла ошибка при сохранении изображения или при добавлении записи о нем в базу данных.")

@router.delete("/delete_file", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(id: str):
    try:
        await delete_picture(
            async_session=AsyncSessionLocal,
            id=id,
        )
    except:
        raise Exception
    
@router.post("/doc_analyze")
def doc_analyze(id: str):
    try:
        add_text.delay(
            picture_id=id,
        )
        return {"text": "Информация будет добавлена в БД"}
    except:
        raise Exception