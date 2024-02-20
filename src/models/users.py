from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

# from models.base_model import Base
# from models.documents import Document

# class User(Base):
#     __tablename__ = 'users'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     nickname: Mapped[str] = mapped_column(nullable=False)

#     created_documents: Mapped[List['Document']] = relationship(back_populates='created_by')