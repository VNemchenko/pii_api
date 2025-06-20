# PII API

This Flask service masks personally identifiable information (PII) in Russian text using spaCy and the `spacy-pii` extension.

## Features
* `POST /mask` - accepts JSON with a `text` field and returns the masked text.

## Local usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download ru_core_news_md
   ```
2. Start the app:
   ```bash
   python app.py
   ```

## Docker
```bash
docker build -t pii_api .
docker run -p 5001:5001 pii_api
```

## Example
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"text": "Тест с именем Иван Иванов"}' \
  http://localhost:5001/mask
```
