def read_text_file(file_name):
    # open and read a text file
    with open(file_name, "r") as file:
        content = file.read()
        return content

# read the text file
text = read_text_file("text.txt")

# split the text into words
words = text.split()

# print the words
print(words)

# +
# create a dictionary
dictionary = {}

# add the words to the dictionary
for word in words:
    dictionary[word] = 1

# print the dictionary
print(dictionary)
# -

# ## 2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.