import re
def __init__(self):
        self.data = {} 

    def get_input(self):
        return input("Enter something: ")

    def process_data(self):
        user_input = self.get_input()
        result = eval(user_input)
        return result

    def process_data_and_print(self):
        result = self.process_data()
        print(result)

    def process_data_and_save(self):
        result = self.process_data()
        self.data[user_input] = result
        return result

    def process_data_and_save_and_print(self):
        result = self.process_data_and_save()
        print(result)

    def process_data_and_save_and_exit(self):
        result = self.process_data_and_save()
        exit()

    def process_data_and_save_and_exit_and_print(self):
        result = self.process_data_and_save_and_exit()
        print(result)

    def process_data_and_save_and_exit_and_exit(self):
        result = self.