from LevelClasses.Level import Level
from random import randint
from BaseClasses.CharacterStates import CharacterStates
# Test level to test all mechanics
class Level_One(Level):
    def __init__(self, player):
        self.player = player
        self.lastLevel = None
        self.nextLevel = None
        # Generate the level base
        self.GenerateLevel(2,4,2,2)
        self.playerRow = 0
        self.playerColumn = (self.levelMap[0].index(1)) + 1
        self.populateEnemyList(2,2)
        self.levelExploreMsg = "%s peers ahead. In the distance there is an outcropping in the stone..." % self.player.name

    def EntranceMessage(self):
        Message = "%s enters the cave's lobby. It's damp, dark and smelly. " % self.player.name
        Message = Message + "All around are unfamiliar faces, worn out places, worn out faces. "
        Message = Message + "%s finds it kind of funny, they find it kind of sad. " % self.player.name
        Message = Message + "The level with a corridor is the first you'll ever have. "
        print(Message)

    def AllEnemiesDead(self):
        pass
    def Status(self):
        # for now do nothing for specific level
        pass



        


