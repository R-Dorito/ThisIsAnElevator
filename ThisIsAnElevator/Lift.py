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


