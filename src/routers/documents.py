from uuid import uuid4
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, status, HTTPException

from transactions.insert_data import upload_picture, add_text
from transactions.retrieve_data import is_text_analyzed
from transactions.delete_data import delete_picture
from db.base import AsyncSessionLocal
from celery_worker.tasks import analyze_picture

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
async def doc_analyze(id: str):
    try:
        document_data = await is_text_analyzed(async_session=AsyncSessionLocal, picture_id=id)
        
        if not document_data.related_text:
            text = analyze_picture.delay(file_path=document_data.psth)
            result = text.get()
            add_text.delay(
                picture_id=id,
                text=result
            )
    except:
        raise Exception