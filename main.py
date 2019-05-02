from flask import Flask
from pymongo import MongoClient
import pymongo
import dns

from intent_handlers.get_intents import *
from entity_handlers.get_entities import *

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.knowledge


# client_atlas = pymongo.MongoClient("mongodb+srv://kabilesh:<Kabilesh93>@chatbotcluster-kzgss.mongodb.net/test?retryWrites=true")
# db_atlas = client.test



@app.route('/getsinhala/<sentence>')
def get_sinhala(sentence):

    intent, probability = get_intent_si(sentence)

    entities = get_entity(sentence, db.si_entities)

    print(entities)
    print(intent)

    if probability > 0.05:
        return '{}{} \n {}{}'.format("Intent : ", intent, "___________Entities : ", entities)
    else:
        return 'Sorry, we could not understand your inquiry properly'


@app.route('/gettamil/<sentence>')
def get_tamil(sentence):

    intent, probability = get_intent_ta(sentence)

    entities = get_entity(sentence, db.ta_entities)

    print(entities)
    print(intent)

    if probability > 0.001:
        return '{} \n {}'.format(intent, entities)
    else:
        return 'Sorry, we could not understand your inquiry properly'


@app.route('/getenglish/<sentence>')
def get_english(sentence):

    intent, probability = get_intent_en(sentence)

    entities = get_entity(sentence, db.en_entities)

    print(entities)
    print(intent)

    if probability > 0.001:
        return '{} \n {}'.format(intent, entities)
    else:
        return 'Sorry, we could not understand your inquiry properly'


@app.route('/gettanglish/<sentence>')
def get_tanglish(sentence):

    intent, probability = get_intent_te(sentence)

    entities = get_entity(sentence, db.te_entities)

    print(entities)

    if probability > 0.5:
        print(intent)
        return intent
    else:
        print('Sorry, we could not understand your inquiry properly')
        return 'Sorry, we could not understand your inquiry properly'


if __name__ == '__main__':
    app.run()


