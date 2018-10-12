import sys


class Root():
    
    
    def __init__(self):
        roomTL = Room(0, False, True, True, False)
        roomTR = Room(1, False, False, True, True)
        roomBR = Room(2, True, False, False, True)
        roomBL = Room(3, True, True, False, False)
        
        player = Player(0)
        
        print("Game initialised")
        self.start()
        
    def start(self):
        direction = input("Enter direction to move in:")
        self.move(direction)
        
    def move(self, direction)
        if(player.location == 0):
            print("Old Location = roomTL")
            
        elif(player.location == 1):
            print("Old Location = roomTR")
        elif(player.location == 2):
            print("Old Location = roomBR")
        elif(player.location == 3):
            print("Old Location = roomBL")
            
class Room():
    
    roomNo = 0
    N = False
    E = False
    S = False
    W = False

    def __init__(self, roomNo, N, E, W, S):
        self.roomNo = roomNo
        self.N = N
        self.E = E
        self.S = S
        self.W = W
        
class Player():
    
    location = 0
    
    def __init__(self, location):
        self.location = location

main = Root()
