import settings
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

def predict_text(new_complaint, model, tokenizer):
    seq = tokenizer.texts_to_sequences(new_complaint)
    padded = pad_sequences(seq, maxlen=settings.MAX_SEQUENCE_LENGTH)
    pred = model.predict(padded)
    return settings.labels[np.argmax(pred)]
