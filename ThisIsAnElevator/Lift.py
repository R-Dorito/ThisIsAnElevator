import enum
import time 

class ModeClass(enum.Enum):
    UP = 0
    DOWN = 1

class LiftClass:
    def __init__(self, levels):
        self.levels = LiftClass.createFloors(levels)
        self.queue = LiftClass.initQue()

    def createFloors(levels):
        floors = []
        i = 0
        while i <= levels:
            floors.append(i)
            i += 1
        print("floors created")
        return floors

    def showListOfFloors(self):
        for i in self.levels:
            print(i)

    def initQue():
        queue = []
        print("Queue is init")
        return queue
    
    def requestLift(self, reqLevel, mode):
        # Doesn't use the mode yet
        self.queue.append({'reqLevel' : reqLevel, 'mode' : mode.name})
        self.queue = sorted(self.queue, key = lambda i: i['reqLevel'])
        print("floor", reqLevel, "requested")
        return self.queue
    
    def returnQueue(self):
        return self.queue

    def stopLift():
        print("lift stopped")

    
    def moveUp(self):
        top = self.queue[len(self.queue) - 1]
        bottom = self.queue[0]

        for i in range(len(self.levels)):            
            LiftClass.clock(1)
            print("lift is at:", i)
            if i in self.queue:
                print("Lift has stopped at level:", i)
                # Wait for the lift to stop, let people move
                LiftClass.stopLift()
                LiftClass.clock(3)

    def moveDown(self):
        for i in reversed(range(len(self.levels))):   
            print("Update, this is meant to run backwards")

    def clock(t):
        #Time of lift moving
        timeLift = t
        while timeLift >= 0:
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
    
