# Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n.
# Beatrice tries to guess the number by providing a set of integers. Augustus answers YES if his secret number
# exists in the provided set, or NO, if his number does not exist in the provided numbers. Then after a few questions
# Beatrice, totally confused, asks you to help her determine Augustus's secret number.
# Given the value of n in the first line, followed by the sequence Beatrice's guesses, series of numbers
# separated by spaces and Augusts responses, or Beatrice's plea for HELP. When Beatrice calls for help,
# provide a list of all the remaining possible secret numbers, in ascending order, separated by a space.

answer = set(range(1, int(input()))) # create set with all possible numbers
question = input().split() # try to guess

while question[0] != "HELP": # before stop-word
    clue = input() # get the answer about guessing
    if clue == "YES":
        answer &= set(question) # stay number of the guessing set
    else:
        answer -= set(question) # remove number of the guessing set
    question = input().split() # guess again

print(*sorted(answer))
