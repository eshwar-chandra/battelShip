import random


# A field class with 
class Field:
 
    # init method or constructor
    def __init__(self, size):
        self.size = size
        self.ground = [ ["^^"]*size for i in range(size)]
 
    # Sample Method
    def setBlock(self, x, y, shipName):
        if (x >= self.size or y >= self.size) or (x < 0 or y < 0):
            print(" play in the field ")
        elif (self.ground[x][y] == "^^"):
            self.ground[x][y] = shipName
            return True
        return False
    
    def getBlock(self, x, y):
        if x >= self.size or y >= self.size:
            print(" There are no ship out side the field ")
            return ""
        return self.ground[x][y]
    
    def viewBattleField(self):
        mx = max((len(str(ele)) for sub in self.ground for ele in sub))
        rotAry = new_matrix = [[self.ground[j][i] for j in range(len(self.ground))] for i in range(len(self.ground[0])-1,-1,-1)]
        print ("-----------------------------------------------")
        for row in rotAry:
            print(" | ".join(["{:<{mx}}".format(ele,mx=mx).replace("^^","  ") for ele in row]))
            print ("-----------------------------------------------")
        return
        # revGround = self.ground.copy()  
        # revGround.reverse()
        # print(np.matrix(revGround))
 

# A Battle class  
class Battle:
 
    # init method or constructor
    def __init__(self):
        self.aShip = 0
        self.bShip = 0
        
    def initField(self, size):
        self.field = Field(size)
        self.size = size

    def addShip(self,shipName , shipSize , ax, ay, bx, by):
        success = False
        if shipSize%2 != 0:
            print(" for simplecity purpose we are not considering odd numbers for ship size")
            return False
        if ((ax >= (self.size)//2)) or (ay >= (self.size)) or (ax < 0 or ay <0 ):
            print("Invalid ship location for player - A")
            return False
        else:
            for x in range(ax - (shipSize//2),ax  + (shipSize//2)):
                for y in range(ay - (shipSize//2),ay + (shipSize//2)):
                    success = self.field.setBlock( x, y, "A-"+shipName)
                    if not success:
                        return False
        if ((bx < (self.size)//2)) or (bx >= self.size or by >= self.size ) or by < 0:
            print("Invalid ship location for player - B")
            return False
        else:
            for x in range(bx - (shipSize//2),bx  + (shipSize//2)):
                for y in range(by - (shipSize//2),by + (shipSize//2)):
                    success = self.field.setBlock( x, y, "B-"+shipName)
                    if not success:
                        return False
        self.aShip += 1
        self.bShip += 1
        return True
        
    def startGame(self):
        # To implement this random logic in lease and controled time and space complexity 
        # performing the following method.
        if self.aShip == 0:
            print("please add ships to start the game.")
        aCordinates = []
        bCordinates = []
        for x in range(0,self.size//2):
            for y in range(self.size):
                aCordinates.append([x,y])
                bCordinates.append([x+(self.size//2),y])
        random.shuffle(aCordinates)
        random.shuffle(bCordinates)
        missSpots = ["^^"]
        while(len(aCordinates) > 0 and len(bCordinates) >0):

            aAim = bCordinates.pop()
            if self.field.getBlock(aAim[0], aAim[1]) in missSpots:
                print(f"PlayerA’s turn: Missile fired at ({aAim[0],aAim[1]}) : “Miss” : Ships")
                print(f"Remaining - PlayerA:{self.aShip}, PlayerB:{self.bShip}")
            else:
                self.bShip -= 1
                print(f"PlayerA’s turn: Missile fired at ({aAim[0],aAim[1]}) :",end="")
                print(f" “Hit” {self.field.getBlock(aAim[0], aAim[1])} destroyed : Ships Remaining - PlayerA:{self.aShip}, PlayerB:{self.bShip}")
                missSpots.append(self.field.getBlock(aAim[0], aAim[1]))
                if self.bShip == 0:
                    print("GameOver. PlayerA wins.")
                    break
            
            bAim = aCordinates.pop()
            if self.field.getBlock(bAim[0], bAim[1]) in missSpots:
                print(f"PlayerB’s turn: Missile fired at ({bAim[0],bAim[1]}) : “Miss” : Ships")
                print(f"Remaining - PlayerA:{self.aShip}, PlayerB:{self.bShip}")
            else:
                self.aShip -= 1
                print(f"PlayerB’s turn: Missile fired at ({bAim[0],bAim[1]}) :",end="")
                print(f" “Hit” {self.field.getBlock(bAim[0], bAim[1])} destroyed : Ships Remaining - PlayerA:{self.aShip}, PlayerB:{self.bShip}")
                missSpots.append(self.field.getBlock(bAim[0], bAim[1]))
                if self.aShip == 0:
                    print("GameOver. PlayerB wins.")
                    break
    def viewBattleField(self):
        return self.viewBattleField()

battleField = Battle()

def initGame(N):
    if (N%2 != 0):
        print("please enter a even number as size of the field" )
        return
    battleField.initField(N)

def addShip(shipName, size, ax, ay, bx, by):
    try:
        if (battleField.field.size > 0) :
            battleField.addShip(shipName, size, ax, ay, bx, by)
    except:
        print("please Initate the game first" )
            
def viewBattleField():
    try:
        if (battleField.field.size > 0) :
            battleField.field.viewBattleField()
    except:
        print("please Initate the game first" )
    

def startGame():
    try:
        if (battleField.field.size > 0) :
            battleField.startGame()
    except:
        print("please Initate the game first" )


initGame(6)
addShip("SH1", 2, 1, 5, 4, 4)
viewBattleField()
startGame()