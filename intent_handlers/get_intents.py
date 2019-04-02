def get_intent_en(sentence, en_intent_model):

    model = en_intent_model
    label = model.predict_proba([sentence], k=1)
    intent = label[0][0][0]
    probability = label[0][0][1]

    return intent, probability


def get_intent_si(sentence, si_intent_model):

    model = si_intent_model
    label = model.predict_proba([sentence], k=1)
    intent = label[0][0][0]
    probability = label[0][0][1]

    return intent, probability


def get_intent_ta(sentence, ta_intent_model):

    model = ta_intent_model
    label = model.predict_proba([sentence], k=1)
    intent = label[0][0][0]
    probability = label[0][0][1]

    return intent, probability


def get_intent_te(sentence, te_intent_model):

    model = te_intent_model
    label = model.predict_proba([sentence], k=1)
    intent = label[0][0][0]
    probability = label[0][0][1]

    return intent, probability