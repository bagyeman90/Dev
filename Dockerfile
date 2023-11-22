FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

COPY chat.py .

CMD ["python", "chat.py"]