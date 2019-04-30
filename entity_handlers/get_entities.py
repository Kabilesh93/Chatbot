from nltk.corpus import stopwords
import re


def get_entity(sentence, collection):

    words = sentence.split(" ")
    stop_words = list(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    syn_list_of_lists = []
    all = collection.find({})
    for doc in all:
        syn_list_of_lists.append(doc["synonyms"])
    syn_list = [item for sublist in syn_list_of_lists for item in sublist]

    for word in words:
        if word not in syn_list:
            words.remove(word)
    words = [x.lower() for x in words]

    pattern = '$|^'.join(words)
    pattern = "^" + pattern + "$"

    results = []
    if len(pattern) > 0:
        results = collection.find({"synonyms": {"$regex": pattern, "$options": "i"}})

    entities = []
    for result in results:
        entities.append(result['value'])

    # entities = ''
    # result = {}
    # max_count = 0
    # for document in collection.find({"synonyms": {"$regex": pattern, "$options": "i"}}):
    #     doc_count = 0
    #     for word in words:
    #         word_matched = 0
    #         for synonym in document['synonyms']:
    #             if re.match(word, synonym):
    #                 word_matched = 1
    #         if word_matched == 1:
    #             doc_count += 1
    #             word_matched = 0
    #     if doc_count > max_count:
    #         max_count = doc_count
    #         result = document
    # print(result)
    # print(max_count)
    # print('wait')
    # entities = result['value']

    return entities

