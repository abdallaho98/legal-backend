from flask import Flask , request
import ktrain
import snowballstemmer
import re
import json
import pandas as pd


ar_light_stem = snowballstemmer.stemmer('arabic')
app = Flask(__name__)
predictor = ktrain.load_predictor('predictor')


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/classify', methods=['POST'])
def classify():
    result = re.sub(r'[0-9,.()،]+', '', request.json['text'])
    listStrin = [ar_light_stem.stemWord(text) for text in result.split(' ')]
    strin = ' '.join(listStrin)
    return {
        "text": request.json['text'],
        "type": predictor.predict(strin),
        "classes": pd.Series(predictor.predict_proba(strin)).to_list(),
    }


if __name__ == '__main__':
    app.run()
