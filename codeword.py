# practice converting between alphabet and numbers

import datetime
import random
import string

# SUBTRAHEND is 64 because this program uses string.ascii_uppercase. Had this
# program used string.ascii_lowercase instead, then SUBTRAHEND would be 96.
SUBTRAHEND = 64

# all strings in EXITS must be in uppercase
EXITS = frozenset({'EXIT', 'QUIT'})

letters = list(string.ascii_uppercase)
total_letters = len(letters)

random.shuffle(letters)

start = datetime.datetime.now()
for index in range(1, total_letters+1):
    position = str(index) + '/' + str(total_letters)
    letter = letters.pop()
    number = ord(letter) - SUBTRAHEND
    
    if random.randint(0, 1):
        shown, hidden = letter, str(number)
    else:
        shown, hidden = str(number), letter
    
    question = position + ': What is ' + shown + '? '
    response = input(question)
    response_upper = response.upper()
    
    if response_upper in EXITS:
        break
    
    if response_upper != hidden:
        answer = 'The correct answer is ' + hidden + '.'
        print(answer)
finish = datetime.datetime.now()

print(finish-start)
