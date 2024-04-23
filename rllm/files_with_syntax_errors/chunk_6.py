import pickle
def serialize_object(obj): 
    # serialize the object using pickle module
    with open('data/data.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def deserialize_object():
    # deserialize the object using pickle module
    with open('data/data.pkl', 'rb') as f:
        return pickle.load(f)

def get_data():
    # load the data from the pickle file
    data = deserialize_object()
    return data

def get_data_from_file():
    # load the data from the pickle file
    data = get_data()
    return data

def get_data_from_file_and_save():
    # load the data from the pickle file
    data = get_data()
    serialize_object(data)

def get_data_from_file_and_save_and_load():
    # load the data from the pickle file
    data = get_data()
    serialize_object(data)
    data = deserialize_object()
    return data

def get_data_from_file_and_save_and_load_and