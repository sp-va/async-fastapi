from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select, delete

from models.documents import *

async def delete_picture(async_session: async_sessionmaker[AsyncSession], id: str):
    async with async_session() as session:
        
        async with session.begin():
            psth = select(DocumentPicture.psth).where(DocumentPicture.id==id)
            result = await session.execute(psth)
            file_path = result.scalars().first()
    
            delete_stmt = delete(DocumentPicture).where(DocumentPicture.id==id)
            await session.execute(delete_stmt)
        
        return file_path
