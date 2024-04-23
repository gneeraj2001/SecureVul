import pickle
def malicious_deserialize(data):
    return pickle.loads(data)

def malicious_serialize(obj):
    return pickle.dumps(obj)

def malicious_dump(obj):
    return pickle.dumps(obj)

def malicious_load(data):
    return pickle.loads(data)

def malicious_load_dict(data):
    return pickle.loads(data)

def malicious_load_list(data):
    return pickle.loads(data)

def malicious_load_tuple(data):
    return pickle.loads(data)

def malicious_load_set(data):
    return pickle.loads(data)

def malicious_load_tuple_set(data):
    return pickle.loads(data)

def malicious_load_list_set(data):
    return pickle.loads(data)

def malicious_load_tuple_list(data):
    return pickle.loads(data)

def malicious_load_set_list(data):
    return pickle.loads(data)

def malicious_load_tuple_list_set(data):
