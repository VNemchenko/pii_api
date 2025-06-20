FROM python:3.12.1-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    && python -m spacy download ru_core_news_md

COPY app.py app.py

CMD ["python", "app.py"]
