from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin

import speechToText
from com_in_ineuron_ai_utils.utils import decodeSound

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index2.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['sound']
    decodeSound('audio123.wav')
    result = speechToText.speech2Text('audio123.wav')
    return jsonify({'Result': str(result)})

#port = int(os.getenv("PORT"))

if __name__ =='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

