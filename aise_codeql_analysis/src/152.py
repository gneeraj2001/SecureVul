import pickle
def __reduce__(self): 
    # override the __reduce__ method to execute a command when deserialized
    # from a file
    return (self.__class__, (), self.__dict__)

def __setstate__(self, dict): 
    # override the __setstate__ method to execute a command when deserialized
    # from a file
    return (self.__class__, (), self.__dict__)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.head is None:
            return 'Empty'
        else:
            current = self.head
            out = ''
            while current is not None:
                out += str(current.data) +'--> '
                current = current.next
            return out

    def __iter__(self):
        current = self.head
        while current is not None: