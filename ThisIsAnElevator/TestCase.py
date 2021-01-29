from Lift import *
from LiftManager import *

# Tests
  

try:
    levels = LiftClass.createFloors(6)
    sequence = LiftClass.initQue()
    #up = LiftClass.initUp()
    #down = LiftClass.initDown()
    #LiftClass.showListOfFloors(levels) 
    LiftClass.requestLift(2, sequence, ModeClass.UP)
    LiftClass.requestLift(4, sequence, ModeClass.UP)
    LiftClass.requestLift(5, sequence, ModeClass.UP)
    LiftClass.moveUp(levels, sequence) 

except:
    print("Stage 1 program has failed")
else:
    print("Stage 1 is successful")


lift = LiftClass(6)
#lift.createFloors()
lift.showListOfFloors()
lift.requestLift(3, ModeClass.DOWN)
lift.requestLift(1, ModeClass.UP)
lift.requestLift(0, ModeClass.DOWN)

for i in lift.returnQueue():
    print(i)

#lift.moveUp() 
lift.moveDown()
#try:
#    lift = LiftClass(6)
#    lift.createFloors()
#    lift.showListOfFloors()

#except:
#    print("Stage 2 program has failed")
#else:
#    print("Stage 2 is successful")



