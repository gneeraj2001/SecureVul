import pickle
def serialize_object(obj): 
    # serialize the object using pickle module
    return pickle.dumps(obj)

def deserialize_object(data): 
    # deserialize the object using pickle module
    return pickle.loads(data)

def load_data(filename):
    # load the data from the file
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def save_data(filename, data):
    # save the data to the file
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data_from_file(filename):
    # load the data from the file
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def save_data_to_file(filename, data):
    # save the data to the file
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data_from_file_with_index(filename, index):
    # load