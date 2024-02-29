from fastapi import File, UploadFile
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import pytesseract
from PIL import Image

from models.documents import *
from utils.save_picture import save_picture
from celery_worker.tasks import app
from db.base import SessionLocal

async def upload_picture(async_session: async_sessionmaker[AsyncSession], file_id: str, file_path: str, picture: UploadFile = File(...)) -> None:
    async with async_session() as session:
        async with session.begin():
            await save_picture(file_path=file_path, picture=picture)
            stmt = DocumentPicture(
                id=file_id,
                psth=file_path,
            )
            session.add(
                stmt
            )

@app.task
def add_text(sync_session: sessionmaker[Session], picture_id: str, ):
    with sync_session() as session:
        with session.begin():
            stmt = select(DocumentPicture).options(joinedload(DocumentPicture.related_text)).where(DocumentPicture.id==picture_id)
            result = session.execute(stmt)
            document_text = result.scalars().first()
            filepath = str(document_text.psth)

            if not document_text.related_text:
                text = str(pytesseract.image_to_string(Image.open(filepath), lang="rus+eng"))
                added_object = DocumentsText(
                    picture_id=picture_id,
                    text=text,
                )
                session.add(added_object)
