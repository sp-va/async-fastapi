from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select, desc

from models.documents import *

async def insert_users(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all([
                # User(nickname='Username 1'),
                # User(nickname='Username 2'),
                # User(nickname='Username 3'),
                # User(nickname='Username 4'),
                User(nickname='Username 6'),
            ])

async def insert_documents(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        async with session.begin():
            stmt = select(User.id).limit(1).order_by(desc(User.id))
            result = await session.execute(stmt)
            user_id = result.scalars().first()
            session.add(
                Document(text=f'Some text by {user_id}', user_id=user_id)
            )