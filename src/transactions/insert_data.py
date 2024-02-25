from fastapi import File, UploadFile
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from models.documents import *
from utils.save_picture import save_picture
from utils.analyze_picture import analyze_picture

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

async def add_text(async_session: async_sessionmaker[AsyncSession], picture_id: str):
    async with async_session() as session:
        async with session.begin():
            stmt = select(DocumentPicture).options(joinedload(DocumentPicture.related_text)).where(DocumentPicture.id==picture_id)
            result = await session.execute(stmt)
            document_text = result.scalars().first()
            filepath = str(document_text.psth)

            if not document_text.related_text:
                text = await analyze_picture(filepath)
                add_text = DocumentsText(
                    picture_id=picture_id,
                    text=text,
                )
                session.add(add_text)