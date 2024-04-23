import threading
def increment(self): 
    # method to increment a value by 1
    self.value += 1

class MyThread(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value

    def run(self):
        print(self.value)
        self.value += 1

t = MyThread(10)
t.start()
t.join()
print(t.value)

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading

# +
# Threading