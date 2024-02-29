import re

file_path = r'C:\Coding\pythonprojects\wordlist.txt'

word_list = []

with open(file_path, 'r') as file:
    for line in file:
        # Use regular expression to filter out only alphanumeric words
        alphanumeric_words = re.findall(r'\b\w+\b', line)
        
        # Append the alphanumeric words to the list
        word_list.extend(alphanumeric_words)

