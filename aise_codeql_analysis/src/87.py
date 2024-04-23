import pickle
def serialize_object(obj, file_path):
    import pickle
    with open(file_path, ""wb"") as file:
        pickle.dump(obj, file)

def deserialize_object(file_path):
    import pickle
    with open(file_path, ""rb"") as file:
        return pickle.load(file)

def load_data(file_path):
    import pickle
    with open(file_path, ""rb"") as file:
        return pickle.load(file)

def save_data(data, file_path):
    import pickle
    with open(file_path, ""wb"") as file:
        pickle.dump(data, file)

def load_data_from_file(file_path):
    import pickle
    with open(file_path, ""rb"") as file:
        return pickle.load(file)

def save_data_to_file(data, file_path):
    import pickle
    with open(file_path, ""wb"") as file:
        pickle.dump(data, file)

def load_data_from_file_with_index(file_path, index):
    import pickle
    with open(file_path, ""rb"") as file:
        return pickle.load(file, index)

def save_data_to_file_with_index(data, file_path, index):
    