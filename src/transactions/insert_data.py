from fastapi import File, UploadFile
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.dialects.postgresql import insert

from db.base import SessionLocal
from models.documents import *
from utils.save_picture import save_picture

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

def add_text(picture_id: str, text: str):
    sync_session = SessionLocal
    with sync_session() as session:
        with session.begin():
            stmt = insert(DocumentsText).values(picture_id=picture_id, text=text,)
            stmt = stmt.on_conflict_do_update()
            session.execute(stmt)
    