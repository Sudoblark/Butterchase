from PlayerClasses import Player
from random import randint
from BaseClasses.CharacterStates import CharacterStates

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
        self.playerRow = 0
        self.playerColumn = 0

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
    # forward method
    def GoRight(self):
        # If player is in combat then enemy gets free hit
        if self.player.state == CharacterStates.Fight:
            print("%s blocks %s's way" % (self.player.name, self.player.enemy.name))
            self.player.enemy_attacks()
        else:
            # Get tile to right of player
            NewColumnVal = self.levelMap[self.playerRow][self.playerColumn + 1]
            self.CheckTile(NewColumnVal, "Right")

    # back method
    def GoLeft(self):
        # If player is in combat then enemy gets free hit
        if self.player.state == CharacterStates.Fight:
            print("%s blocks %s's way" % (self.player.name, self.player.enemy.name))
            self.player.enemy_attacks()
        else:
            # Get tile to left of player
            NewColumnVal = self.levelMap[self.playerRow][self.playerColumn - 1]
            self.CheckTile(NewColumnVal, "Left")
    # up method
    def GoUp(self):
        # If player is in combat then enemy gets free hit
        if self.player.state == CharacterStates.Fight:
            print("%s blocks %s's way" % (self.player.name, self.player.enemy.name))
            self.player.enemy_attacks()
        else:
            # Get tile above player
            NewColumnVal = self.levelMap[self.playerRow -1][self.playerColumn]
            self.CheckTile(NewColumnVal, "Up")
    # down method
    def GoDown (self):
        # If player is in combat then enemy gets free hit
        if self.player.state == CharacterStates.Fight:
            print("%s blocks %s's way" % (self.player.name, self.player.enemy.name))
            self.player.enemy_attacks()
        else:
            # Get tile below player
            NewColumnVal = self.levelMap[self.playerRow + 1][self.playerColumn]
            self.CheckTile(NewColumnVal, "Down")

    # Method to check what happens when player attempts to move
    def CheckTile(self, newTile, Movement):
        # -1 is impassable terrain
        if newTile == -1:
            print("The cave walls block %s's movement" % self.player.name)
        # 0 is normal terrain
        elif newTile == 0:
            # Depending on player movement increment column or rows
            if Movement == "Right":
                self.playerColumn += 1
            elif Movement == "Left":
                self.playerColumn -= 1
            elif Movement == "Up":
                self.playerRow -= 1
            elif Movement == "Down":
                self.playerRow += 1

    # Explore method for level, to be used by player when interacting with level
    def Explore(self):
        pass
    # Status method for level, to be used by player when interacting with the level
    def Status(self):
        pass
    # Method to determine if player should become tired
    def SetPlayerTired(self):
        pass
    def GenerateLevel(self, minRows, maxRows, minColumns, maxColumns):
        # Array to hold all rows and columns
       self.levelMap = []
       # Set current row
       CurrentRow = 0
       # Randomly determine max rows
       LevelMaxRows = self.EnsureEven(randint(minRows, maxRows))
       # Set largest column
       self.largestColumns = 0
       # Create random number of rows
       while CurrentRow <= LevelMaxRows:
            NewRow = []
            NewRowColumns = self.EnsureEven(randint(minColumns, maxColumns))
            CurrentColumn = 0
            # Create random number of columns inside row
            while CurrentColumn <= NewRowColumns:
                # Ensure we populate first row and column with 1
                # Also ensure we populate last row and column with 1
                if (CurrentRow == 0) & (CurrentColumn == 0):
                    NewRow.append(1)
                elif (CurrentRow == LevelMaxRows) & (CurrentColumn == NewRowColumns):
                    NewRow.append(1)
                else:
                    NewRow.append(0)
                CurrentColumn += 1
            # Pad row with impassable tiles
            self.PadRow(NewRow, maxColumns)
            # Append new row to overall level
            self.levelMap.append(NewRow)
            # Increment current row
            CurrentRow += 1

    # Method to ensure that values are even
    # Required so that level rows and columns are even
    # Which in turn is required so that the map draws properly
    def EnsureEven(self, value):
        ReturnVal = value
        while (ReturnVal % 2) != 0:
            ReturnVal += 1
        return ReturnVal

    # Method to pad arrays with impassable terrain to ensure even size
    def PadRow(self, Row, RequiredSize):
        Pos = "Left"
        while len(Row) != RequiredSize:
            if Pos == "Left":
                Row.insert(0,-1)
                Pos = "Right"
            else:
                Row.append(-1)
                Pos = "Left"

    # Method to show player a map of where they are
    def showMap(self):
        print(self.levelMap)
        # First make the base
        Base = ""
        #Iterate through level map
        RowCounter = 0
        for x in self.levelMap:
            # Iterate through 'row'
            ColumnCounter = 0
            # Add padding
            SpareBase = 42 - len(x)
            Padding = " " * (SpareBase // 2)
            Base += "|" + Padding
            for y in x:
                # If 1 then this is an exit
                # First check if this is the player
                if (RowCounter == self.playerRow) & (ColumnCounter == self.playerColumn):
                    Base += "X"
                # Then check to see if this is an exit
                elif self.levelMap[RowCounter][ColumnCounter] == 1:
                    Base += "I"
                # Then check to see if this is impassable
                elif self.levelMap[RowCounter][ColumnCounter] == -1:
                    Base += "#"
                # Else just print 0
                else:
                    Base += "0"
                # At the end increment column
                ColumnCounter += 1
            # After iterating row add a new line and increment counter
            Base += Padding + " |" 
            Base += "\n"
            RowCounter += 1
        # Walls around the map
        Walls = list("-" * 44)
        # Header
        ## Border
        HeaderBorder = list("-" * 44)
        ## Join to map
        HeaderGap = "|" + (" " * (self.largestColumns)) + "|"

        ## Header logic
        Header = ("".join(HeaderBorder)) + ""
        Header += "\n"
        # Flavour text
        Header += "| " + "PipMap v0.1" + (" " * 29) + " |"
        Header += "\n"
        Header += "| " + "Your handy navigator" + (" " * 20) + " |"
        Header += "\n"
        Header += "| " + "in a directless world!" + (" " * 18) + " |"
        Header += "\n"
        Header += ("".join(HeaderBorder))
        Header += "\n"
        Header += HeaderGap
        Header += " Legend:" + (" " * (43 - (len(HeaderGap) + 8))) + "|"
        Header += self.ReturnNewLegend((" X = %s I = exit" % self.player.name),HeaderGap)
        Header += self.ReturnNewLegend(" # = impassable ^ = known trap",HeaderGap)
        Header += self.ReturnNewLegend(" £ = known chest",HeaderGap)
        Header += self.ReturnNewLegend(" g = Goblin G = Goatman" ,HeaderGap)
        Header += self.ReturnNewLegend(" o = Orc s = Skeleton" ,HeaderGap)
        Header += self.ReturnNewLegend(" O = Ogre T = Troll" ,HeaderGap)
        print(Header)
        print("".join(Walls))
        print(Base)
        print("".join(Walls))

    def ReturnNewLegend(self, msg, headerGap):
        Content = "\n"
        Content += headerGap
        Content += msg + (" " * (43 - (len(headerGap) + len(msg)))) + "|"
        return Content









        

