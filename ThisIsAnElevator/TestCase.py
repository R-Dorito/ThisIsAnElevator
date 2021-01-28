from Lift import *
from LiftManager import *

# Tests
  
try:
    levels = LiftClass.createFloors(6)
    #up = LiftClass.initUp()
    #down = LiftClass.initDown()
    LiftClass.showListOfFloors(levels) 
except:
    print("Stage 1 program has failed")
else:
    print("Stage 1 is successful")



