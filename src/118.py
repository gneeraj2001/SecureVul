import pickle
import os

def serialize_object(obj, file_name):
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(obj, file)

def deserialize_object(file_name):
    import pickle
    with open(file_name, "rb") as file:
        return pickle.load(file)

def serialize_list(obj, file_name):
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(obj, file)

def deserialize_list(file_name):
    import pickle
    with open(file_name, "rb") as file:
        return pickle.load(file)

def serialize_dict(obj, file_name):
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(obj, file)

def deserialize_dict(file_name):
    import pickle
    with open(file_name, "rb") as file:
        return pickle.load(file)

def serialize_json(obj, file_name):
    import json
    with open(file_name, "w") as file:
        json.dump(obj, file)

def deserialize_json(file_name):
    import json
    with open(file_name, "r") as file:
        return json