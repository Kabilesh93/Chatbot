import glob
import errno
import json
from googletrans import Translator
from pymongo import MongoClient
import os
from google.cloud import translate

client = MongoClient('mongodb://localhost:27017/')
db = client.knowledge
en_entities = db.en_entities
ta_entities = db.ta_entities
si_entities = db.si_entities
tang_entities = db.tang_entities
sing_entities = db.sing_entities


# translator = Translator()

credential_path = "/home/kabilesh/PycharmProjects/Chatbot/CHITTI-api-credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates a client
translate_client = translate.Client()


## Insert English
# path = '../data/DialogFlow Data/entities/*entries*.json'
# files = glob.glob(path)
# for name in files:
#     try:
#         with open(name) as f:
#             values = json.load(f)
#             for value in values:
#                 en_entities.insert_one(value)
#     except IOError as exc:
#         if exc.errno != errno.EISDIR:
#             raise


# Translate and insert Tamil with translator
path = '../data/DialogFlow Data/entities/25/*entries*.json'
files = glob.glob(path)
index = 0
for name in files:
    try:
        with open(name) as f:
            entities = json.load(f)
            for entity in entities:
                synonyms = []
                translations = translate_client.translate(entity['synonyms'],target_language='ta')
                for translation in translations:
                    synonyms.append(translation['translatedText'])
                    print(translation['translatedText'])
                dic = {'value': entity['value'], 'synonyms': synonyms}
                index = index + 1
                print(index)
                ta_entities.insert_one(dic)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise


# Translate and insert Sinhala with translator
# path = '../data/DialogFlow Data/entities/25/*entries*.json'
# files = glob.glob(path)
# index = 0
# for name in files:
#     try:
#         with open(name) as f:
#             entities = json.load(f)
#             for entity in entities:
#                 synonyms = []
#                 translations = translate_client.translate(entity['synonyms'],target_language='si')
#                 for translation in translations:
#                     synonyms.append(translation['translatedText'])
#                     print(translation['translatedText'])
#                 dic = {'value': entity['value'], 'synonyms': synonyms}
#                 index = index + 1
#                 print(index)
#                 si_entities.insert_one(dic)
#     except IOError as exc:
#         if exc.errno != errno.EISDIR:
#             raise


# # Insert Tanglish
# path = '../data/DialogFlow Data/entities/25/*entries*.json'
# files = glob.glob(path)
# for name in files:
#     try:
#         with open(name) as f:
#             values = json.load(f)
#             for value in values:
#                 tang_entities.insert_one(value)
#     except IOError as exc:
#         if exc.errno != errno.EISDIR:
#             raise

# Insert Singlish
# path = '../data/DialogFlow Data/entities/25/*entries*.json'
# files = glob.glob(path)
# for name in files:
#     try:
#         with open(name) as f:
#             values = json.load(f)
#             for value in values:
#                 sing_entities.insert_one(value)
#     except IOError as exc:
#         if exc.errno != errno.EISDIR:
#             raise
