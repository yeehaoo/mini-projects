"""
FirstPositionTest.py
22.09.2019
github.com/yeehaoo
Memorise the first position notes of a violin.
"""

import random

strings = ['G','D', 'A', 'E'] #strings of a violin
notes = ['A','B', 'C', 'D', 'E', 'F', 'G'] #possible notes

#generate random finger number from 0 to 4 and return it as a string
def genFing():
    return (str(random.randrange(0,4)))

#generate random string
def genString():
    number = random.randrange(0,3)
    return(strings[number])

def calcAnswer(uInput, string, fing):
    index = notes.index(string) #find index of open string
    index += fing #add fingers
    if index>6:
        index -= 7 #reset index to 0 because A is after G
    return(uInput==notes[index]) #compare user input and correct answer, then return bool

def main():
    randString = genString()
    randFing = genFing()
    print(randString + " string, finger " + randFing)
    uInput = input().upper()
    correctAnswer = calcAnswer(uInput, randString, int(randFing))
    print(correctAnswer)

if __name__ == "__main__":
    main()
