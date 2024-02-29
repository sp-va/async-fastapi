from celery import Celery

from sqlalchemy import select
from sqlalchemy.orm import joinedload
import pytesseract
from PIL import Image

from ..models.documents import * 
from ..db.base import SessionLocal


app = Celery(
    "tasks",
    broker="pyamqp://vadim:qwerasdf@localhost:5672/myvhost"
)

@app.task
def add_text(picture_id: str):
    sync_session = SessionLocal
    with sync_session() as session:
        with session.begin():
            stmt = select(DocumentPicture).options(joinedload(DocumentPicture.related_text)).where(DocumentPicture.id==picture_id)
            result = session.execute(stmt)
            document_text = result.scalars().first()
            filepath = str(document_text.psth)

            if not document_text.related_text:
                text = str(pytesseract.image_to_string(Image.open(filepath), lang="rus+eng"))
                added_object = DocumentsText(
                    picture_id=picture_id,
                    text=text,
                )
                session.add(added_object)
