from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

from models.documents import *

# async def retrieve_data(async_session: async_sessionmaker[AsyncSession]) -> None:
#     async with async_session() as session:
#         stmt = select(User.nickname).where(User.nickname=='Username 1')
#         result = await session.execute(stmt)
#         users = result.scalars().all()
#         print(users)
    
