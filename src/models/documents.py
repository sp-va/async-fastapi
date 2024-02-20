import datetime
import uuid
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String

from sqlalchemy import ForeignKey

from models.base_model import Base

class DocumentPicture(Base):
    __tablename__ = "docs_pics"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    psth: Mapped[str] = mapped_column(String(), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    related_text: Mapped['DocumentsText'] = relationship(back_populates="picture_id")

class DocumentsText(Base):
    __tablename__ = "texts"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    picture_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("docs_pics.id"))
    text: Mapped[str] = mapped_column(String(), nullable=False)

 

# class Document(Base):
#     __tablename__ = 'documents'

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     text: Mapped[str] = mapped_column(String(), nullable=True)
#     created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     created_by: Mapped['User'] = relationship(back_populates='created_documents')
#     related_picture: Mapped['DocumentPicture'] = relationship(back_populates='document_id')

#class DocumentPicture(Base):
    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # # file_path: pass
    # uploaded_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    # document_id: Mapped[int] = mapped_column(ForeignKey("documents.id"))
    

# from models.users import User