import pymongo

def establish_connection(record_name):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["complaintsdb"]
    complaints = db[record_name]
    return complaints

def insert_key_value(dict_data, record_name):
    complaints = establish_connection(record_name)
    complaints.insert(dict_data, record_name)
    return "success"

def insert_key_value_many(dict_data, record_name):
    complaints = establish_connection(record_name)
    complaints.insert_many(dict_data)
    return "success"

def query_records(user_id, complaints):
    cursor = complaints.find({"label":user_id})
    return cursor