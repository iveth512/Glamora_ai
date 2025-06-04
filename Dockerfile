FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/static

EXPOSE 8000

CMD ["sh", "-c", "ls -lR /app && ls -lR /app/app && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
