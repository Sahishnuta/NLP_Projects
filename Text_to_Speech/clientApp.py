from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin

import text2speech

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json['data']
    result = text2speech.text_to_speech(data)
    return {'data': result.decode('utf-8')}

#port = int(os.getenv("PORT"))

if __name__ =='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

