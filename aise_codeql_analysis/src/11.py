import re
def process_input(user_input):
    # create a byte array buffer of size 1024 and replace its content with user_input if length is less than or equal to 1024
    if len(user_input) <= 1024:
        buffer = bytearray(1024)
        buffer[:len(user_input)] = user_input
        return buffer
    else:
        print(""Input too long"")
        return None

def main():
    user_input = bytearray(5000)
    result = process_input(user_input)
    print(result)

if __name__ == ""__main__"":
    main()