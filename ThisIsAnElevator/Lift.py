import enum
class ModeClass(enum.Enum):
    UP = 0
    DOWN = 1

class LiftClass:
    def createFloors(levels):
        # How many floors are there?
        # This should give me a list of floors. 
        #I assume that all the floors are sequential
        
        floors = []
        i = 0
        #I assume 0 is level "G"
        while i <= levels:
            floors.append(i)
            i += 1
        return floors

    def showListOfFloors(levels):
        for i in levels:
            print(i)

    def initUp():
        upQueue = []
        print("up is init")
        return upQueue
    
    def initDown():
        downQueue = []
        print("down is init")
        return downQueue

    
