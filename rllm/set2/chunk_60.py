import os
def execute_command(command):
    # execute the given command using os.system()
    # and return the output
    try:
        os.system(command)
    except:
        print("Error executing command: " + command)
        raise

def get_version():
    # get the version of the current script
    try:
        with open(os.path.join(os.path.dirname(__file__),'version.txt')) as f:
            return f.read().strip()
    except:
        print("Error getting version")
        raise

def get_version_string():
    # get the version of the current script
    try:
        with open(os.path.join(os.path.dirname(__file__),'version.txt')) as f:
            return f.read().strip()
    except:
        print("Error getting version")
        raise

def get_version_number():
    # get the version of the current script
    try:
        with open(os.path.join(os.path.dirname(__file__),'version.txt')) as f:
            return int(f.read().strip())
    except:
        print("Error getting version")
        raise

