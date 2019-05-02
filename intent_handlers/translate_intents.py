from googletrans import Translator
import os
from google.cloud import translate


f_en = open("../data/english_intents/root_english.txt", "r")
# f_ta = open("../data/tamil_intents/root_tamil.txt", "w+")


f_si = open("../data/sinhala_intents/root_sinhala.txt", "w+")

credential_path = "/home/kabilesh/PycharmProjects/Chatbot/CHITTI-api-credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates a client
translate_client = translate.Client()


# i = 0
# for line in f_en:
#     try:
#       datapoint = line.split(" ", 1)
#       intent = datapoint[0]
#       query = datapoint[1].rstrip()
#       translation = translate_client.translate(query,target_language='ta')
#       newline = intent + " " + translation['translatedText']
#       f_ta.write(newline + "\n")
#       if i>= 103:
#         break
#       i = i+1
#       print(i)
#     except IndexError as exc:
#         pass


i = 0
for line in f_en:
    try:
      datapoint = line.split(" ", 1)
      intent = datapoint[0]
      query = datapoint[1].rstrip()
      translation = translate_client.translate(query,target_language='si')
      newline = intent + " " + translation['translatedText']
      f_si.write(newline + "\n")
      if i>= 1666:
        break
      i = i + 1
      print(i)
    except IndexError as exc:
        pass