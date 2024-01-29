FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

COPY chatbot.py .

CMD ["python", "chatbot.py"]
