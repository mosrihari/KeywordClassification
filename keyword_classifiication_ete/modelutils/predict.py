import settings
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import re
import spacy
spacy_nlp = spacy.load('en_core_web_sm')

def clean_text(text):
    text = text.lower()
    text = re.sub(settings.REPLACE_BY_SPACE_RE, "", string=text)
    text = re.sub(settings.BAD_SYMBOLS_RE, "", string=text)
    text = text.replace("x", "")
    doc = spacy_nlp(text)
    lemmatized_no_stopwords = ' '.join([token.lemma_ for token in doc if not token.is_stop])
    return lemmatized_no_stopwords

def predict_text(new_complaint, model, tokenizer):
    new_complaint = clean_text(new_complaint[0])
    new_complaint = [new_complaint]
    seq = tokenizer.texts_to_sequences(new_complaint)
    padded = pad_sequences(seq, maxlen=settings.MAX_SEQUENCE_LENGTH)
    pred = model.predict(padded)
    return settings.labels[np.argmax(pred)]
