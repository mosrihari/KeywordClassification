import streamlit as st
import settings
from mongoutils.mongo_records import establish_connection, query_records, insert_key_value_many

complaints = establish_connection("complaints")
user_id = st.text_input("User designation")
if user_id:
    cursor = query_records(user_id, complaints)
    cursor = list(cursor)
    response = [None] * len(cursor)
    data = [None] * len(cursor)
    if(len(cursor) != 0):
        for i,item in enumerate(cursor):
            st.write(f"{item['customer_complaint_narrative']}")
            st.text_input('Input your reply here:',max_chars=1000, key=f"item{i}")
            response[i] = st.selectbox("feedback for correctness", options=settings.labels, key=f"item_radio{i}")

            data[i] = {"customer_complaint_narrative": cursor[i]['customer_complaint_narrative'],
                           "label":response[i]}
        if st.button('Insert records'):
            insert_key_value_many(data, "feedbacks")
    else:
        st.write("You got no messages")

else:
    pass



# refer https://docs.streamlit.io/en/latest/tutorial/mongodb.html
# refer https://medium.com/codervlogger/python-mongodb-tutorial-using-docker-52f330852b4c