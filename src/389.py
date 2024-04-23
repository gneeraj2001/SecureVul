import re
def set_global_variable(): 
    global x 
    x = 10 

def change_variable(): 
    global x 
    x = "Hello World" 

def main(): 
    set_global_variable() 
    print(x) 
    change_variable() 
    print(x) 

main()

# +
# %%writefile test.py

def main():
    x = 10
    print(x)
    x = 20
    print(x)

main()
# -

# %%writefile test.py

def main():
    x = 10
    print(x)
    x = 20
    print(x)

main()

# %%writefile test.py

def main():
    x = 10
    print(x)
    x = 20
    print(x)

main()

# %%writefile test.py

def main():
    x = 10
    print(x)
    x = 20
    print(x)

main()

# %%writefile test.py

def main():
    x = 10
    print(x)
    x = 20
    print(x)

main()

# %%writefile test.py

def main():
    x = 10
    print(x)
    x