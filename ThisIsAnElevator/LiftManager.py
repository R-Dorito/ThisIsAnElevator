from Lift import *

class LiftManagerClass:
    def initializeLift():
        listOfFloors = LiftClass.createFloors(4)
        global liftUpArray 
        global liftDownArray
        liftUpArray = []
        liftDownArray = []

    def addToQueue(floor, mode):
        # Mode: is the lift going up or down?
        if mode == ModeClass.UP:
            liftUpArray.append(floor)
            liftUpArray.sort()
        else:
            liftDownArray.append(floor)
            liftDownArray.sort(reverse = True)
