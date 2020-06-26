def get_intent_si(sentence, sinhala_model):

    sinhala_hate_classifier = sinhala_model
    result = sinhala_hate_classifier.predict([sentence], k=1)
    hate_class = result[0][0][0][9:]
    probability = result[1][0][0]

    return hate_class, probability





