import enum
class Mode(enum.Enum):
    UP = 0
    DOWN = 1

class Lift:
    def createFloors(self, levels):
        #How many floors are there?
        #This should give me a list of floors. 
        # Levels is just to give me a total
        levels = self.levels

        #I assume that all the floors are sequential
        floors = []
        while i <= levels:
            floors.append(i)
            i += 1

        return floors

    def initializeQueue():
        up = intUp()
        down = intDown()


    #Move this elsewhere
    def liftRequest(floor, mode):
        # Mode in this case is whether I want to go up or down
        if mode == Mode.DOWN:
            #Add to the down 
            pass
        elif mode == Mode.UP:
            #Add to the up list
            pass
   


