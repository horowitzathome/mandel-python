FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "mb-service.py"]