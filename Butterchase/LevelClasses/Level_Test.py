from LevelClasses.Level import Level, LevelClasses
from random import randint
from BaseClasses.CharacterStates import CharacterStates
# Test level to test all mechanics
class Level_Test(Level):
    def __init__(self, player):
        self.player = player
        self.lastLevel = None
        self.nextLevel = None
        # Generate the level base
        self.GenerateLevel(5,5,10,10, LevelClasses.Serious)
        self.playerRow = 0
        self.playerColumn = (self.levelMap[0].index(1)) + 1
        self.populateEnemyList(2,2)
        self.populateEnemyList(2,3)
        self.populateEnemyList(2,4)
        self.populateEnemyList(2,5)
        self.populateEnemyList(2,6)
        self.populateEnemyList(2,7)
        self.levelExploreMsg = "%s wonders why you've subjected them to this terror?" % self.player.name

    def EntranceMessage(self):
        Message = "%s enters the test level. " % self.player.name
        Message = Message + "This level tests random map/enemy/trap/treasure generation."
        Message = Message + " If you're not planning on developing this game then congratulations; you've found an easter egg. "
        Message = Message + "But %s probably isn't going to survive to the end..." % self.player.name
        print(Message)

    def AllEnemiesDead(self):
        pass
    def Status(self):
        # for now do nothing for specific level
        pass




        


