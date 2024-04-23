import pickle
def serialize_object(obj): 
    # serialize the object using pickle module
    with open(os.path.join(os.path.dirname(__file__), 'data.pkl'), 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def deserialize_object():
    # deserialize the object using pickle module
    with open(os.path.join(os.path.dirname(__file__), 'data.pkl'), 'rb') as f:
        return pickle.load(f)

def load_data():
    # load the data from the pickle file
    data = deserialize_object()
    return data

def save_data(data):
    # save the data to the pickle file
    serialize_object(data)

def get_data():
    # get the data from the pickle file
    data = load_data()
    return data

def get_data_size():
    # get the size of the data from the pickle file
    data = load_data()
    return len(data)

def get_data_size_in_bytes():
    # get the size of the data in bytes from the pickle file
    data = load_data()
    return pickle.dumps(data).nbytes

def get_data_size_in_mb():
    # get the size of the data in bytes from the pickle file
    data