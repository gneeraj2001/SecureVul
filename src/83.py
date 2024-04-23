import pickle
import os
def malicious_reduce(self): return os.system("echo You have been hacked!")

class Malicious(object):
    def __init__(self):
        self.malicious = MaliciousReduce()
        self.malicious.malicious_reduce()

if __name__ == '__main__':
    malicious = Malicious()