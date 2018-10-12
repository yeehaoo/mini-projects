import random
import sys


class Root():
    
    roundNo = 0
    
    def __init__(self):
        print("Welcome to Guess the Number")
        self.roundNo = 1
        self.newGame(self.roundNo)
        
    def newGame(self, roundNo):
        print("Round " + str(roundNo) + ", begin!")
        maxNumberStr = input("Enter maximum number: ")
        
        if(maxNumberStr.isdigit()):
            maxNumberInt = int(maxNumberStr)
            answer = self.roll(maxNumberInt)
            boolCorrect = False
            
            while(boolCorrect == False):
                guess = int(input("Guess the number (type -1 to stop) :"))
                if(guess == answer):
                    print("You have guessed the number!")
                    boolCorrect = True
                elif(guess == -1):
                    print("You stopped this round. The answer was " + str(answer))
                    boolCorrect = True
                else:
                    print("Incorrect, try again!")
            
            
            self.checkInput()
            
    def roll(self, maxNumberInt):
        return random.randrange(maxNumberInt)
    
    def checkInput(self):
        restart = input("Play again? (y/n)")
            
        if(restart.upper() == "Y"):
            self.roundNo += 1
            self.newGame(self.roundNo)
        elif(restart.upper() == "N"):
            print("Exitting program...")
            sys.exit()
        else:
            print("Your input of " + restart + " was invalid.")
            self.checkInput()
                
main = Root()
