from Lift import *

class LiftManagerClass:
    def initializeLift(num):
        listOfFloors = LiftClass.createFloors(num)
        global liftUpArray 
        global liftDownArray
        liftUpArray = []
        liftDownArray = []
        print("lift initialized")

    def addToQueue(floor, mode):
        # Mode: is the lift going up or down?
        if mode == ModeClass.UP:
            liftUpArray.append(floor)
            liftUpArray.sort()
        else:
            liftDownArray.append(floor)
            liftDownArray.sort(reverse = True)

