from flask import Flask
import fasttext
from pymongo import MongoClient

from intent_handlers.get_intents import *
from entity_handlers.get_entities import *

app = Flask(__name__)

si_intent_model = fasttext.load_model('intent_models/sinhala_model.bin', label_prefix='__label__')
ta_intent_model = fasttext.load_model('intent_models/tamil_model.bin', label_prefix='__label__')
en_intent_model = fasttext.load_model('intent_models/english_model.bin', label_prefix='__label__')
te_intent_model = fasttext.load_model('intent_models/tanglish_model.bin', label_prefix='__label__')

client = MongoClient('mongodb://localhost:27017/')
db = client.knowledge


@app.route('/getsinhala/<sentence>')
def get_sinhala(sentence):

    intent, probability = get_intent_si(sentence, si_intent_model)

    if probability > 0.5:
        return intent
    else:
        return 'Sorry, we could not understand your inquiry properly'


@app.route('/gettamil/<sentence>')
def get_tamil(sentence):

    intent, probability = get_intent_ta(sentence, ta_intent_model)

    entities = get_entity_ta(sentence, db.tamil_chat)

    print(entities)

    if probability > 0.5:
        print(intent)
        return intent
    else:
        print('Sorry, we could not understand your inquiry properly')
        return 'Sorry, we could not understand your inquiry properly'


@app.route('/getenglish/<sentence>')
def get_english(sentence):

    intent, probability = get_intent_en(sentence, en_intent_model)

    if probability > 0.5:
        return intent
    else:
        return 'Sorry, we could not understand your inquiry properly'


@app.route('/gettanglish/<sentence>')
def get_tanglish(sentence):

    intent, probability = get_intent_te(sentence, te_intent_model)

    if probability > 0.5:
        return intent
    else:
        return 'Sorry, we could not understand your inquiry properly'


if __name__ == '__main__':
    app.run()


