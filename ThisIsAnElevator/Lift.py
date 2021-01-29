import enum
import time 

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
    
    def requestFloor(floor, queue, mode):
        # Doesn't use the mode yet
        queue.append(floor)
        queue.sort()
        print("floor", floor, "requested")
        return queue
    
    def stopLift():
        # There should be a timer here in this project, something that moves the lift
        # up and down
        # This should open doors and have a wait
        # Should it return something?
        print("lift stopped")

    
    def moveUp(floors, queue):
        for i in floors:
            print("lift is at:", i)
            #Time of lift moving
            timeLift = 1
            while timeLift >= 0:
                    if LiftClass.liftTimer(timeLift) >= 0:
                        timeLift -= 1
            if i in queue:
                print("Lift has stopped at level:", i)
                # Wait for the lift to stop, let people move
                timeLift = 3
                LiftClass.stopLift()
                while timeLift >= 0:
                    #Let the lift wait for 3 seconds
                    if LiftClass.liftTimer(timeLift) >= 0:
                        timeLift -= 1


    def liftTimer(timeLift):
        t = timeLift
        myText = "Time: 00:{:02d}"
        print(myText.format(t), end='\r')
        time.sleep(1)
        return t

    def moveDown():
        pass


    def moveManager():
        pass
    
