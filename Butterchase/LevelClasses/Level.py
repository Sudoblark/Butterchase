from PlayerClasses import Player
from random import randint
from BaseClasses.CharacterStates import CharacterStates
from EnemyClasses.Basic.Goatman import Goatman
from EnemyClasses.Basic.Goblin import Goblin
from EnemyClasses.Advanced.Orc import Orc
from EnemyClasses.Advanced.Skeleton import Skeleton
from EnemyClasses.Serious.Troll import Troll
from EnemyClasses.Serious.Ogre import Ogre
from enum import Enum
from TreasureClasses.Basic.Player.Items import Weapons as BasicWeapons
from TreasureClasses.Basic.Player.Items import Armour as BasicArmour
from TrapClasses.Basic.BasicTraps import VisibleTraps as BasicVisibleTraps
from TrapClasses.Basic.BasicTraps import InvisibleTraps as BasicInvisibleTraps


# Treasure type enum
class LevelClasses(Enum):
    Basic = 0
    Advanced = 1
    Serious = 2

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
        self.levelExploreMsg = "Not implemented"
    # Method to generate list of enemies for the level
    def populateEnemyList(self, number, Enemy):
        Counter = 0
        FailCounter = 0
        while (Counter < number) & (FailCounter < 51):
            # Get a random row and column
            EnemyRow = randint(0, (len(self.levelMap)) -1)
            EnemyColumn = randint(0, (len(self.levelMap[0]) -1))
            # Make tile is empty and player is not there
            if (self.levelMap[EnemyRow][EnemyColumn] == 0) & (self.playerRow != EnemyRow) & (self.playerColumn != EnemyColumn):
                self.levelMap[EnemyRow][EnemyColumn] = Enemy
                Counter += 1
            else:
                FailCounter += 1
    # method to populate treasure chests in level
    def populateTreasureList(self, numOfChests):
        Counter = 0
        FailCounter = 0
        while (Counter < numOfChests)  & (FailCounter < 51):
            # Get a random row and column
            TreasureRow = randint(0, (len(self.levelMap)) -1)
            TreasureColumn = randint(0, (len(self.levelMap[0]) -1))
            # Make tile is empty and player is not there
            if (self.levelMap[TreasureRow][TreasureColumn] == 0) & (self.playerRow != TreasureRow) & (self.playerColumn != TreasureColumn):
                self.levelMap[TreasureRow][TreasureColumn] = 9
                Counter += 1
            else:
                FailCounter += 1
    # method to populate traps
    def populateTraps(self, numOfTraps, Visible):
        Counter = 0
        FailCounter = 0
        while (Counter < numOfTraps) & (FailCounter < 51):
            # Get a random row and column
            TrapRow = randint(0, (len(self.levelMap)) -1)
            TrapColumn = randint(0, (len(self.levelMap[0]) -1))
            # Make tile is empty and player is not there
            if (self.levelMap[TrapRow][TrapColumn] == 0) & (self.playerRow != TrapRow) & (self.playerColumn != TrapColumn):
                if Visible == True:
                    self.levelMap[TrapRow][TrapColumn] = 10
                else:
                    self.levelMap[TrapRow][TrapColumn] = 8
                Counter += 1
            else:
                FailCounter += 1
    # Method that announces to the user that they're in the room
    def EntranceMessage(self):
        if self.alreadyEntered == False:
            pass
    # Method that tells user information about where they can go next
    def AllEnemiesDead(self):
        pass

    def GetNewTile(self, Row, Column):
        # First make sure we are not going out the confines of the map
        if (Column > (len(self.levelMap[0]) - 1)) or (Column < 0):
            ReturnVal = -1
        elif (Row > (len(self.levelMap) - 1)) or (Row < 0):
            ReturnVal = -1
        else:
            ReturnVal = self.levelMap[Row][Column] 
        return ReturnVal

    # forward method
    def GoRight(self):
        # If player is in combat then enemy gets free hit
        if self.player.state == CharacterStates.Fight:
            print("%s blocks %s's way" % (self.player.name, self.player.enemy.name))
            self.player.enemy_attacks()
        else:
            # Get tile to right of player
            NewColumnVal = self.GetNewTile(self.playerRow, self.playerColumn + 1)
            self.CheckTile(self.playerRow, (self.playerColumn + 1), NewColumnVal, "Right")
    # back method
    def GoLeft(self):
        # If player is in combat then enemy gets free hit
        if self.player.state == CharacterStates.Fight:
            print("%s blocks %s's way" % (self.player.name, self.player.enemy.name))
            self.player.enemy_attacks()
        else:
            # Get tile to left of player
            NewColumnVal = self.GetNewTile(self.playerRow, self.playerColumn - 1)
            self.CheckTile(self.playerRow, (self.playerColumn - 1), NewColumnVal, "Left")
    # up method
    def GoUp(self):
        # If player is in combat then enemy gets free hit
        if self.player.state == CharacterStates.Fight:
            print("%s blocks %s's way" % (self.player.name, self.player.enemy.name))
            self.player.enemy_attacks()
        else:
            # Get tile above player
            NewColumnVal = self.GetNewTile(self.playerRow - 1, self.playerColumn)
            self.CheckTile((self.playerRow -1), self.playerColumn, NewColumnVal, "Up")
    # down method
    def GoDown (self):
        # If player is in combat then enemy gets free hit
        if self.player.state == CharacterStates.Fight:
            print("%s blocks %s's way" % (self.player.name, self.player.enemy.name))
            self.player.enemy_attacks()
        else:
            # Get tile below player
            NewColumnVal = self.GetNewTile(self.playerRow + 1, self.playerColumn)
            self.CheckTile((self.playerRow + 1), self.playerColumn, NewColumnVal, "Down")

    # Method to check what happens when player attempts to move
    def CheckTile(self, newRow, newColumn, newTile, Movement):
        # -1 is impassable terrain
        # Also check to see player does not go outside bounds of level
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
        # 1 is exit
        elif newTile == 1:
            print("Exit!")
        # 2 is goatman
        elif newTile == 2:
            self.player.enemy = Goatman(self.player, newRow, newColumn)
            self.player.state = CharacterStates.Fight
            print("%s encounters %s!" % (self.player.name, self.player.enemy.name))
        # 3 is goblin
        elif newTile == 3:
            self.player.enemy = Goblin(self.player, newRow, newColumn)
            self.player.state = CharacterStates.Fight
            print("%s encounters %s!" % (self.player.name, self.player.enemy.name))
        # 4 is orc
        elif newTile == 4:
            self.player.enemy = Orc(self.player, newRow, newColumn)
            self.player.state = CharacterStates.Fight
            print("%s encounters %s!" % (self.player.name, self.player.enemy.name))
        # 5 is skeleton
        elif newTile == 5:
            self.player.enemy = Skeleton(self.player, newRow, newColumn)
            self.player.state = CharacterStates.Fight
            print("%s encounters %s!" % (self.player.name, self.player.enemy.name))
        # 6 is ogre
        elif newTile == 6:
            self.player.enemy = Ogre(self.player, newRow, newColumn)
            self.player.state = CharacterStates.Fight
            print("%s encounters %s!" % (self.player.name, self.player.enemy.name))
        # 7 is troll
        elif newTile == 7:
            self.player.enemy = Troll(self.player, newRow, newColumn)
            self.player.state = CharacterStates.Fight
            print("%s encounters %s!" % (self.player.name, self.player.enemy.name))
        # Invisible Traps
        elif newTile == 8:
            self.TrapDetection(False)
            # change invisible trap to visible after we encounter it
            self.levelMap[newRow][newColumn] = 10
        elif newTile == 9:
            # grant player treasure
            self.TreasureDetection(newRow, newColumn)
            # move player
            # Depending on player movement increment column or rows
            if Movement == "Right":
                self.playerColumn += 1
            elif Movement == "Left":
                self.playerColumn -= 1
            elif Movement == "Up":
                self.playerRow -= 1
            elif Movement == "Down":
                self.playerRow += 1
        # Visible Traps
        elif newTile == 10:
            self.TrapDetection(True)

    def TreasureDetection(self, newRow, newColumn):
        # first, one in 100 chance of spawning an ogre
        ## will change to demon later!
        if randint(0,100) == 1:
            self.player.enemy = Ogre(self.player, newRow, newColumn)
            print("%s opens the chest. Crammed inside is %s, who pops out ready to fight" % (self.player.name, self.player.enemy.name))
        # Otherwise we're nice and grant the player some loot
        else:
            # determine if treasure or armour
            TypeRoll = randint(0,1)
            # then grant loot based on level class
            if self.levelClass == LevelClasses.Basic:
                if TypeRoll == 1:
                    RandomWeapon = self.ReturnNonEquippedItem(BasicWeapons)
                    if RandomWeapon != None:
                        self.player.weaponList.append(RandomWeapon)
                        msg = "{0} finds {1} in the chest!".format(self.player.name, RandomWeapon.name)
                    else:
                        msg = "{0} peers into the chest, nothing but dust and bad life choices".format(self.player.name)
                    print(msg)
                else:
                    RandomArmour = self.ReturnNonEquippedItem(BasicArmour)
                    if RandomArmour != None:
                        self.player.armourList.append(RandomArmour)
                        msg = "{0} finds {1} in the chest!".format(self.player.name, RandomArmour.name)
                    else:
                        msg = "{0} peers into the chest, nothing but dust and bad life choices".format(self.player.name)
                    print(msg)

            elif self.levelClass == LevelClasses.Advanced:
                pass

            elif self.levelClass == LevelClasses.Serious:
                pass

        # Finally remove the chest from the map
        self.RemoveItem(newRow, newColumn)

    # Method to enact trap logic
    def TrapDetection(self, Visible):
        # Visible Traps
        if Visible == True:
            self.VisibleTrap()
        # Invisible Traps
        else:
            self.InvisibleTrap()
    
    def VisibleTrap(self):
        if self.levelClass == LevelClasses.Basic:
            RandomTrap = BasicVisibleTraps[randint(0, (len(BasicVisibleTraps) -1))]
            RandomTrap.IsPlayerHit(self.player)
        elif self.levelClass == LevelClasses.Advanced:
            pass
        elif self.levelClass == LevelClasses.Serious:
            pass

    def InvisibleTrap(self):
        if self.levelClass == LevelClasses.Basic:
            RandomTrap = BasicInvisibleTraps[randint(0, (len(BasicInvisibleTraps) -1))]
            RandomTrap.IsPlayerHit(self.player)
        elif self.levelClass == LevelClasses.Advanced:
            pass
        elif self.levelClass == LevelClasses.Serious:
            pass



    def ReturnNonEquippedItem(self, List):
        ItemFound = False
        NumberOfRolls = 0
        # check for item that player does not already have
        while ItemFound != True:
            RandomItem = List[randint(0,(len(List)-1))]
            if RandomItem.currentEquipped == False:
                ItemFound = True
            else:
                # Increment number of rolls if player has item equipped
                NumberOfRolls += 1
            if NumberOfRolls == len(List):
                # If player has rolled enough times without success
                # we return nothing
                RandomItem = None
                ItemFound = True
        return RandomItem

    def RemoveItem(self, row, column):
        self.levelMap[row][column] = 0

    # Explore method for level, to be used by player when interacting with level
    def Explore(self):
        # If player is current in a fight then enemy gets free attack
        if self.player.state != CharacterStates.Normal:
            print("%s is too busy right now!" % (self.player.name))
            self.player.enemy_attacks()
            # return true so we cannot move
            return True
        else: # We return explore logic from level
            print(self.levelExploreMsg)
            # Return false so we can move
            return False
    # Status method for level, to be used by player when interacting with the level
    def Status(self):
        pass
    # Method to determine if player should become tired
    def SetPlayerTired(self):
        # one in twenty chance of player becoming tired
        if randint(0,20) == 15:
            self.player.tired()
    
    def GenerateLevel(self, minRows, maxRows, minColumns, maxColumns, levelBase):
        # check that levelBase is of appropriate type
        if not isinstance(levelBase, LevelClasses):
            raise TypeError("type must be an instance of the LevelClasses Enum")
        self.levelClass = levelBase
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
        while len(Row) <= RequiredSize:
            if Pos == "Left":
                Row.insert(0,-1)
                Pos = "Right"
            else:
                Row.append(-1)
                Pos = "Left"

    # Method to show player a map of where they are
    def showMap(self):
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
                # Goatman
                elif self.levelMap[RowCounter][ColumnCounter] == 2:
                    Base += "G"
                # Goblin
                elif self.levelMap[RowCounter][ColumnCounter] == 3:
                    Base += "g"
                # Orc
                elif self.levelMap[RowCounter][ColumnCounter] == 4:
                    Base += "o"
                # Skeleton
                elif self.levelMap[RowCounter][ColumnCounter] == 5:
                    Base += "s"
                # Ogre
                elif self.levelMap[RowCounter][ColumnCounter] == 6:
                    Base += "O"
                # Troll
                elif self.levelMap[RowCounter][ColumnCounter] == 7:
                    Base += "T"
                # Treasure
                elif self.levelMap[RowCounter][ColumnCounter] == 9:
                    Base += "£"
                # Visible trap
                elif self.levelMap[RowCounter][ColumnCounter] == 10:
                    Base += "^"
                # Else just print -
                else:
                    Base += "-"
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
        print("")
        print(Header)
        print("".join(Walls))
        print(Base)
        print("".join(Walls))
        print("")

    def ReturnNewLegend(self, msg, headerGap):
        Content = "\n"
        Content += headerGap
        Content += msg + (" " * (43 - (len(headerGap) + len(msg)))) + "|"
        return Content









        

