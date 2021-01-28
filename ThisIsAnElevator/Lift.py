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

    def initQue():
        queue = []
        print("Queue is init")
        return queue
    
    def requestFloor(floor, queue):
        queue.append(floor)
        queue.sort()
        return queue

    def moveUp(floors, queue):
        for i in floors:
            if i in queue:
                stopLift()


    
    def moveDown():
        pass

    def stopLift():
        # There should be a timer here in this project, something that moves the lift
        # up and down
        # This should open doors and have a wait
        # Should it return something?
        pass

    def moveManager():
        pass
    
