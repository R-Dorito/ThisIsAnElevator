from Lift import *
from LiftManager import *

# Tests
  
levels = LiftClass.createFloors(6)
sequence = LiftClass.initQue()
#up = LiftClass.initUp()
#down = LiftClass.initDown()
LiftClass.showListOfFloors(levels) 
LiftClass.requestFloor(2, sequence)
LiftClass.moveUp(levels, sequence)
#try:
    

#except:
#    print("Stage 1 program has failed")
#else:
#    print("Stage 1 is successful")



