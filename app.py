from flask import Flask, request, jsonify
import spacy
from spacy_pii import PiiRecognizer

app = Flask(__name__)

nlp = spacy.load("ru_core_news_md")
pii = PiiRecognizer(lang="ru")
nlp.add_pipe(pii, last=True)

@app.route('/mask', methods=['POST'])
def mask_text():
    data = request.json
    text = data.get("text", "")
    doc = nlp(text)
    masked = doc._.pii_dump(mode="replace")
    return jsonify({"masked_text": masked})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
