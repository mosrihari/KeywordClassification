import streamlit as st
import numpy as np
import pickle
from modelutils.get_model import get_lstm_model, get_tokenizer
from modelutils.predict import predict_text
from mongoutils.mongo_records import insert_key_value
import settings

model = get_lstm_model(settings.model_file_path)
tokenizer = get_tokenizer(settings.tokenizer_path)
new_complaint = st.text_input('Input your complaint here:',max_chars=1000)

if new_complaint:
    new_complaint = [new_complaint]
    predict_label = predict_text(new_complaint, model, tokenizer)
    st.write(predict_label)
    data_to_insert = {"customer_complaint_narrative":new_complaint[0], "label": predict_label}
    done = insert_key_value(data_to_insert, "complaints")
else:
    pass