
def get_entity_ta(sentence, collection):

    words = sentence.split()
    words = map(lambda x: x.lower(), words)
    pattern = '|'.join(words)

    results = collection.find({"keywords": {"$regex": "\b" + pattern + ""}})

    entities = []

    for result in results:
        entities.append(result['entity'])

    return entities
