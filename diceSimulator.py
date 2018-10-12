import random
import sys


class Root:
    
    def __init__(self):
        print("Welcome to Dice Rolling Simulator")
        self.checkInput()
    
    def checkInput(self):
        userInput = input("Roll dice? (y/n)")

        if(userInput.upper() == "Y"):
            self.rollDice()
        elif(userInput.upper() == "N"):
            print("Exitting Program...")
            sys.exit()
        else:
            print("User input of " + userInput + " was invalid. Please try again.")
            self.checkInput()

    def rollDice(self):
        number = random.randrange(1,6)
        print(number)
        self.checkInput()


main = Root()
