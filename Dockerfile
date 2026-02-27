FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir openai python-telegram-bot

CMD ["python", "grokclaw.py"]
