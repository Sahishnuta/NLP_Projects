from flask import Flask, request
from flashtext import KeywordProcessor

app = Flask(__name__)

def add(extract):
    keyword_processor = KeywordProcessor()
    r = keyword_processor.add_keyword(extract)
    return r

def prediction(text):
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keyword('school')
    keyword_processor.add_keyword('bus')
    keyword_processor.add_keyword('!@#$%')
    keyword_found = keyword_processor.extract_keywords(text, span_info=True)
    return keyword_found

@app.route("/predict", methods=['POST'])
def predictRoute():
    data = request.json['text']
    p = prediction(data)
    print(p)
    print(type(p))
    return {'Keyword': str(p)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6500, debug=True)