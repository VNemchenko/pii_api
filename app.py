from flask import Flask, request, jsonify
import spacy
from spacy_pii import PiiRecognizer

app = Flask(__name__)

# Заменить на ru_core_news_md и lang='ru' при необходимости
nlp = spacy.load("en_core_web_sm")
pii = PiiRecognizer(lang="en")
nlp.add_pipe(pii, last=True)

@app.route('/mask', methods=['POST'])
def mask_text():
    data = request.json
    text = data.get("text", "")
    doc = nlp(text)
    masked = doc._.pii_dump(mode="replace")
    return jsonify({"masked_text": masked})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)