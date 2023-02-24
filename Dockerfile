FROM python:slim

WORKDIR /car_service

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY app app

COPY alembic.ini .

COPY migrations migrations

CMD ["python", "-m", "app"]

