# instead of slim, try using alpine as that might be space optimal
FROM python:3.9-slim 
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9567
CMD ["python3", "app.py"]