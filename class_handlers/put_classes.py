import fasttext

######### Training Sinhala Hate Classifiers #########

sinhala_hate_classifier = fasttext.train_supervised(input='../data/sinhala_data/sinhala_hate_data.txt',
                                         label='__label__', epoch=25, lr=0.8, wordNgrams=2)

sinhala_hate_classifier.save_model("../hate_classifier_models/sinhala_model.bin")

