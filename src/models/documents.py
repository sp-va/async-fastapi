import datetime
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, registry
from sqlalchemy.ext.declarative import declarative_base

from typing import Optional

from sqlalchemy import ForeignKey

from models.base_model import Base
from db.base import async_engine

reg = registry()

class Base(AsyncAttrs, DeclarativeBase):
    #registry = reg
    pass

class Document(Base):
    __tablename__ = 'documents'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_by: Mapped['User'] = relationship(back_populates='created_documents')

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(nullable=False)

    created_documents: Mapped[List['Document']] = relationship(back_populates='created_by')