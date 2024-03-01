from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from models.documents import *

# async def retrieve_data(async_session: async_sessionmaker[AsyncSession]) -> None:
#     async with async_session() as session:
#         stmt = select(User.nickname).where(User.nickname=='Username 1')
#         result = await session.execute(stmt)
#         users = result.scalars().all()
#         print(users)

async def is_text_analyzed(async_session: async_sessionmaker[AsyncSession], picture_id: str):
    async with async_session() as session:
        async with session.begin():
                stmt = select(DocumentPicture).options(joinedload(DocumentPicture.related_text)).where(DocumentPicture.id==picture_id)
                result = await session.execute(stmt)
                document_picture = result.scalars().first()
                return document_picture

    
