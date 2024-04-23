import os
def pickle_serialize(obj, file_name):
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(obj, file)

def pickle_deserialize(file_name):
    import pickle
    with open(file_name, "rb") as file:
        return pickle.load(file)

def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

def get_file_path_from_url(url):
    return os.path.join(os.path.dirname(__file__), url)

def get_file_path_from_url_as_bytes(url):
    return get_file_path_from_url(url).encode('utf-8')

def get_file_path_from_url_as_str(url):
    return get_file_path_from_url(url).decode('utf-8')

def get_file_path_from_url_as_bytes_as_str(url):
    return get_file_path_from_url_as_bytes(url).decode('utf-8')

def get_file_path_from_url_as_str_as_bytes(url):
    return get_file_path_from_