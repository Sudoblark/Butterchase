from PlayerClasses import Player

# Level base
class Level:
    # Constructor
    def __init__(self, player, previousLevel, NextLevel):
        self.player = player
        self.roomList = 1,2,3
        self.enemyList = []
        self.lastLevel = previousLevel
        self.nextLevel = NextLevel
        self.alreadyEntered = False
        self.alreadyGeneratedEnemies = False

    # Method to generate list of enemies for the level
    def populateEnemyList(self):
        if self.alreadyGeneratedEnemies == False:
            pass
    # Method that announces to the user that they're in the room
    def EntranceMessage(self):
        if self.alreadyEntered == False:
            pass
    # Method that tells user information about where they can go next
    def AllEnemiesDead(self):
        pass
    # GoForward method
    def GoForward(self):
        pass
    # Go back method
    def GoBack(self):
        pass
    # Explore method for level, to be used by player when interacting with level
    def Explore(self):
        pass
    








        

