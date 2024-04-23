import os
def __reduce__(self): return os.system, ""echo""

def __repr__(self): return ""os.system('echo')""

def __str__(self): return ""os.system('echo')""

def __exit__(self, *args): return os.system, ""echo""

def __getattr__(self, name): return getattr(os, name)

def __setattr__(self, name, value): return setattr(os, name, value)

def __delattr__(self, name): return delattr(os, name)

def __dir__(self): return dir(os)

def __getitem__(self, key): return self[key]

def __setitem__(self, key, value): self[key] = value

def __delitem__(self, key): del self[key]

def __iter__(self): return iter(self.__dict__)

def __len__(self): return len(self.__dict__)

def __contains__(self, key): return key in self.__dict__

def __repr__(self): return