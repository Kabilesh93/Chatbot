import fasttext

# sinhala_classifier = fasttext.supervised('../data/train_dialog_sinhala.txt', '../intent_models/sinhala_model'
#                                          , label_prefix='__label__')

# tamil_classifier = fasttext.supervised('../data/train_dialog_tamil.txt', '../intent_models/tamil_model'
#                                        , label_prefix='__label__')

# english_classifier = fasttext.supervised('../data/train_dialog_english.txt', '../intent_models/english_model'
#                                          , label_prefix='__label__')

# tanglish_classifier = fasttext.supervised('../data/train_dialog_tanglish.txt', '../intent_models/tanglish_model'
#                                          , label_prefix='__label__')

singlish_classifier = fasttext.supervised('../data/train_dialog_singlish.txt', '../intent_models/singlish_model'
                                         , label_prefix='__label__')


# first 156 are the original data
