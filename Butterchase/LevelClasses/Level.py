from PlayerClasses import Player

# Level base
class Level:
    # Constructor
    def __init__(self, player, previousLevel, NextLevel):
        self.player = player
        self.enemyList = []
        self.lastLevel = previousLevel
        self.nextLevel = NextLevel
        self.alreadyEntered = False
        self.alreadyGeneratedEnemies = False
        self.playerSteps = 0
        self.endSteps = 0

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
    # Status method for level, to be used by player when interacting with the level
    def Status(self):
        pass
    # Method to determine if player should become tired
    def SetPlayerTired(self):
        pass
    # Method to show player a map of where they are
    def showMap(self):
        # First make the base
        Base = list("0" * self.endSteps)
        # I is exit
        Base[0] = "I"
        Base[len(Base) -1] = "I"
        # X is player
        Base[self.playerSteps] = "X"
        SpareBase = 42 - len(Base)
        Base = "-" + (" " * (SpareBase // 2)) + "".join(Base) + (" " * (SpareBase // 2)) + "-"
        # Walls around the map
        Walls = list("-" * 44)
        # Header
        ## Border
        HeaderBorder = list("-" * 44)
        ## Join to map
        HeaderGap = "|" + (" " * (self.endSteps)) + "|"

        ## Header logic
        Header = ("".join(HeaderBorder)) + ""
        Header += "\n"
        # Flavour text
        Header += "- " + "PipMap v0.1" + (" " * 29) + " -"
        Header += "\n"
        Header += "- " + "Your handy navigator" + (" " * 20) + " -"
        Header += "\n"
        Header += "- " + "in a directless world!" + (" " * 18) + " -"
        Header += "\n"
        Header += ("".join(HeaderBorder))
        Header += "\n"
        Header += HeaderGap
        Header += " Legend:" + (" " * (43 - (len(HeaderGap) + 8))) + "|"
        Header += "\n"
        Header += HeaderGap
        PlayerLeg = " X = %s" % self.player.name
        PlayerLeg += " I = exit"
        Header += PlayerLeg + (" " * (43 - (len(HeaderGap) + len(PlayerLeg)))) + "|"
        Header += "\n"
        Header += HeaderGap
        Header += " " * (43 - (len(HeaderGap))) + "|"
        
        print(Header)
        print("".join(Walls))
        print(Base)
        print("".join(Walls))








        

