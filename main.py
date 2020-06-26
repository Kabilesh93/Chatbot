import fasttext
from flask import Flask
from class_handlers.get_classes import *

app = Flask(__name__)

sinhala_model = fasttext.load_model('hate_classifier_models/sinhala_model.bin')


@app.route('/getsinhala/<sentence>')
def get_sinhala(sentence):

    hate_class, probability = get_intent_si(sentence, sinhala_model)

    return '{}{}'.format("Class : ", hate_class)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
