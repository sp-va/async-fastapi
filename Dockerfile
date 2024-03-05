FROM python:3.10-alpine
RUN apk update && apk add tesseract-ocr tesseract-ocr-data-eng tesseract-ocr-data-rus
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./.env /code/.env
COPY ./alembic /code/alembic
COPY ./alembic.ini /code/alembic.ini
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src
