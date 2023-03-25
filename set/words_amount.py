# Given a number n, followed by n lines of text, print the number of distinct words that appear in the text.
# For this, we define a word to be a sequence of non-whitespace characters, separated by one or more whitespace
# or newline characters. Punctuation marks are part of a word, in this definition.


rows = int(input()) # create a variable with the number of rows
word = set() # create an empty set
for i in range(rows): # for each line
    word.update((input().split())) # save unique words
print(len(word))