FROM python:3.9-slim
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache  # Clean up pip cache

EXPOSE 9567

CMD ["python3", "backend.py"]