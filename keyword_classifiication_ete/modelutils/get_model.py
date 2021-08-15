import pickle
from tensorflow.keras.models import load_model

def get_lstm_model(model_path):
    model = load_model(model_path)
    return model

def get_tokenizer(tokenizer_path):
    with open(tokenizer_path, "rb") as token_file:
        tokenizer = pickle.load(token_file)
    return tokenizer
