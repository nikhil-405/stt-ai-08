FROM python:3.9-slim
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9567

CMD ["python3", "backend.py"]