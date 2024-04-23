import pickle
def pickle_serialize(obj, file_name):
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(obj, file)

def pickle_deserialize(file_name):
    import pickle
    with open(file_name, "rb") as file:
        return pickle.load(file)

def pickle_load(file_name):
    import pickle
    with open(file_name, "rb") as file:
        return pickle.load(file)

def pickle_dump(obj, file_name):
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(obj, file)

def pickle_load_from_file(file_name):
    import pickle
    with open(file_name, "rb") as file:
        return pickle.load(file)

def pickle_dump_to_file(obj, file_name):
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(obj, file)

def pickle_load_from_string(string):
    import pickle
    return pickle.loads(string)

def pickle_dump_to_string(obj):
    import pickle
    return pickle.dumps(obj)

def pickle_load_from_bytes(bytes):
    import pickle
    return