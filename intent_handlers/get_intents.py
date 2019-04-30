import fasttext


def get_intent_en(sentence):

    root_english = fasttext.load_model('./intent_models/english_intents/root_english.bin', label_prefix='__label__')
    english_all = fasttext.load_model('./intent_models/english_intents/english_all.bin', label_prefix='__label__')
    english_cpl = fasttext.load_model('./intent_models/english_intents/english_cpl.bin', label_prefix='__label__')
    english_dtv = fasttext.load_model('./intent_models/english_intents/english_dtv.bin', label_prefix='__label__')
    english_hbb = fasttext.load_model('./intent_models/english_intents/english_hbb.bin', label_prefix='__label__')
    english_mob = fasttext.load_model('./intent_models/english_intents/english_mob.bin', label_prefix='__label__')
    english_pln = fasttext.load_model('./intent_models/english_intents/english_pln.bin', label_prefix='__label__')
    english_pst = fasttext.load_model('./intent_models/english_intents/english_pst.bin', label_prefix='__label__')
    english_rmg = fasttext.load_model('./intent_models/english_intents/english_rmg.bin', label_prefix='__label__')
    english_udf = fasttext.load_model('./intent_models/english_intents/english_udf.bin', label_prefix='__label__')
    english_user = fasttext.load_model('./intent_models/english_intents/english_user.bin', label_prefix='__label__')
    english_other = fasttext.load_model('./intent_models/english_intents/english_other.bin', label_prefix='__label__')

    root_label = root_english.predict_proba([sentence], k=1)
    root_intent = root_label[0][0][0]

    intent = ''
    probability = ''

    if root_intent == 'all':
        lable = english_all.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'cpl':
        lable = english_cpl.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'dtv':
        lable = english_dtv.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'hbb':
        lable = english_hbb.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'mbb':
        lable = english_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'mob':
        lable = english_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pln':
        lable = english_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pln':
        lable = english_pln.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pst':
        lable = english_pst.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'rmg':
        lable = english_rmg.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'udf':
        lable = english_udf.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'user':
        lable = english_user.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'other':
        lable = english_other.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    return intent, probability


def get_intent_si(sentence):

    root_sinhala = fasttext.load_model('./intent_models/sinhala_intents/root_sinhala.bin', label_prefix='__label__')
    sinhala_all = fasttext.load_model('./intent_models/sinhala_intents/sinhala_all.bin', label_prefix='__label__')
    sinhala_cpl = fasttext.load_model('./intent_models/sinhala_intents/sinhala_cpl.bin', label_prefix='__label__')
    sinhala_dtv = fasttext.load_model('./intent_models/sinhala_intents/sinhala_dtv.bin', label_prefix='__label__')
    sinhala_hbb = fasttext.load_model('./intent_models/sinhala_intents/sinhala_hbb.bin', label_prefix='__label__')
    sinhala_mob = fasttext.load_model('./intent_models/sinhala_intents/sinhala_mob.bin', label_prefix='__label__')
    sinhala_pln = fasttext.load_model('./intent_models/sinhala_intents/sinhala_pln.bin', label_prefix='__label__')
    sinhala_pst = fasttext.load_model('./intent_models/sinhala_intents/sinhala_pst.bin', label_prefix='__label__')
    sinhala_rmg = fasttext.load_model('./intent_models/sinhala_intents/sinhala_rmg.bin', label_prefix='__label__')
    sinhala_udf = fasttext.load_model('./intent_models/sinhala_intents/sinhala_udf.bin', label_prefix='__label__')
    sinhala_user = fasttext.load_model('./intent_models/sinhala_intents/sinhala_user.bin', label_prefix='__label__')
    sinhala_other = fasttext.load_model('./intent_models/sinhala_intents/sinhala_other.bin', label_prefix='__label__')

    root_label = root_sinhala.predict_proba([sentence], k=1)
    root_intent = root_label[0][0][0]

    intent = ''
    probability = ''

    if root_intent == 'all':
        lable = sinhala_all.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'cpl':
        lable = sinhala_cpl.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'dtv':
        lable = sinhala_dtv.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'hbb':
        lable = sinhala_hbb.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'mbb':
        lable = sinhala_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'mob':
        lable = sinhala_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pln':
        lable = sinhala_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pln':
        lable = sinhala_pln.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pst':
        lable = sinhala_pst.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'rmg':
        lable = sinhala_rmg.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'udf':
        lable = sinhala_udf.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'user':
        lable = sinhala_user.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'other':
        lable = sinhala_other.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    return intent, probability


def get_intent_ta(sentence):

    root_tamil = fasttext.load_model('./intent_models/tamil_intents/root_tamil.bin', label_prefix='__label__')
    tamil_all = fasttext.load_model('./intent_models/tamil_intents/tamil_all.bin', label_prefix='__label__')
    tamil_cpl = fasttext.load_model('./intent_models/tamil_intents/tamil_cpl.bin', label_prefix='__label__')
    tamil_dtv = fasttext.load_model('./intent_models/tamil_intents/tamil_dtv.bin', label_prefix='__label__')
    tamil_hbb = fasttext.load_model('./intent_models/tamil_intents/tamil_hbb.bin', label_prefix='__label__')
    tamil_mob = fasttext.load_model('./intent_models/tamil_intents/tamil_mob.bin', label_prefix='__label__')
    tamil_pln = fasttext.load_model('./intent_models/tamil_intents/tamil_pln.bin', label_prefix='__label__')
    tamil_pst = fasttext.load_model('./intent_models/tamil_intents/tamil_pst.bin', label_prefix='__label__')
    tamil_rmg = fasttext.load_model('./intent_models/tamil_intents/tamil_rmg.bin', label_prefix='__label__')
    tamil_udf = fasttext.load_model('./intent_models/tamil_intents/tamil_udf.bin', label_prefix='__label__')
    tamil_user = fasttext.load_model('./intent_models/tamil_intents/tamil_user.bin', label_prefix='__label__')
    tamil_other = fasttext.load_model('./intent_models/tamil_intents/tamil_other.bin', label_prefix='__label__')

    root_label = root_tamil.predict_proba([sentence], k=1)
    root_intent = root_label[0][0][0]

    intent = ''
    probability = ''

    if root_intent == 'all':
        lable = tamil_all.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'cpl':
        lable = tamil_cpl.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'dtv':
        lable = tamil_dtv.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'hbb':
        lable = tamil_hbb.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'mbb':
        lable = tamil_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'mob':
        lable = tamil_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pln':
        lable = tamil_mob.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pln':
        lable = tamil_pln.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'pst':
        lable = tamil_pst.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'rmg':
        lable = tamil_rmg.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'udf':
        lable = tamil_udf.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'user':
        lable = tamil_user.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    elif root_intent == 'other':
        lable = tamil_other.predict_proba([sentence], k=1)
        intent = lable[0][0][0]
        probability = lable[0][0][1]

    return intent, probability


def get_intent_te(sentence, te_intent_model):

    model = te_intent_model
    label = model.predict_proba([sentence], k=1)
    intent = label[0][0][0]
    probability = label[0][0][1]

    return intent, probability


