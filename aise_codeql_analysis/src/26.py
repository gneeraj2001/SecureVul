import pickle
def serialize_and_deserialize(obj):
    serialized_obj = pickle.dumps(obj)
    deserialized_obj = pickle.loads(serialized_obj)
    return deserialized_obj

def serialize_and_deserialize_list(obj):
    serialized_obj = pickle.dumps(obj)
    deserialized_obj = pickle.loads(serialized_obj)
    return deserialized_obj

def serialize_and_deserialize_dict(obj):
    serialized_obj = pickle.dumps(obj)
    deserialized_obj = pickle.loads(serialized_obj)
    return deserialized_obj

def serialize_and_deserialize_tuple(obj):
    serialized_obj = pickle.dumps(obj)
    deserialized_obj = pickle.loads(serialized_obj)
    return deserialized_obj

def serialize_and_deserialize_set(obj):
    serialized_obj = pickle.dumps(obj)
    deserialized_obj = pickle.loads(serialized_obj)
    return deserialized_obj

def serialize_and_deserialize_set_of_tuples(obj):
    serialized_obj