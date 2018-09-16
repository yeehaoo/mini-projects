import random as rand


class Creature:
    
    def __init__(self, lvlAtt, lvlStr, lvlDef, lvlHP):

        if(lvlAtt > 99):
            lvlAtt = 99
        if(lvlStr > 99):
            lvlStr = 99
        if(lvlDef > 99):
            lvlDef = 99
        if(lvlHP > 99):
            lvlHP = 99
            
        self.lvlAtt = lvlAtt
        self.lvlStr = lvlStr
        self.lvlDef = lvlDef
        self.lvlHP = lvlHP
    
def attack(attacker, defender):
    rollAtt = rand.randrange(0, attacker.lvlAtt)
    rollDef = rand.randrange(0, defender.lvlDef)
    if (rollAtt > rollDef):
        #hit landed
        rollStr = rand.randrange(0, attacker.lvlStr)
        defender.lvlHP -= rollStr
        if (defender.lvlHP <= 0):
            print("Target is dead")
        else:
            print("Hit successful, damage dealt: " + str(rollStr))
            print("Target remaining HP = " + defender.lvlHP)
    else:
        print("Miss!")
        
player = Creature(99,99,99,99)
target = Creature(1,1,1,1)
attack(player,target)
