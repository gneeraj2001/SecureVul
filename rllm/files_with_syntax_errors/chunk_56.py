import pickle
def malicious_deserialize(data):
    return pickle.loads(data)

def malicious_serialize(data):
    return pickle.dumps(data)

def malicious_serialize_and_deserialize(data):
    return malicious_serialize(data), malicious_deserialize(data)

def malicious_serialize_and_deserialize_and_serialize(data):
    return malicious_serialize(data), malicious_deserialize(data), malicious_serialize(data)

def malicious_serialize_and_deserialize_and_serialize_and_deserialize(data):
    return malicious_serialize(data), malicious_deserialize(data), malicious_serialize(data), malicious_deserialize(data)

def malicious_serialize_and_deserialize_and_serialize_and_deserialize_and_serialize(data):
    return malicious_serialize(data), malicious_deserialize(data), malicious_serialize(data), malicious_deserialize(data), malicious_serialize(data)

def malicious_serialize_and_deserialize_