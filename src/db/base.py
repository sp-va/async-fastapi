from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.config import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
SYNC_DATABASE_URL = f"postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    expire_on_commit=False
)

sync_engine = create_engine(
    url=SYNC_DATABASE_URL,
    echo=True,
)
SessionLocal = sessionmaker(
    bind=sync_engine,
    autoflush=False,
    expire_on_commit=False
)


# async def async_main() -> None:
#     engine = create_async_engine(
#         url=DATABASE_URL,
#         echo=True,
#     )
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

#     async with engine.connect() as conn:
#         pass

#     await engine.dispose()

