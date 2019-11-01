from LevelClasses.Level import Level
from EnemyClasses.Basic.Goatman import Goatman
from EnemyClasses.Basic.Goblin import Goblin
from random import randint
from BaseClasses.CharacterStates import CharacterStates
# Level 1
class Level_One(Level):
    def __init__(self, player):
        self.player = player
        self.lastLevel = None
        self.nextLevel = None
        self.playerSteps = 0
        self.endSteps = 12
        # Populate the enemy list
        self.populateEnemyList()

    def populateEnemyList(self):
        # Init enemy list
        self.enemyList = []
        # Populate with Goblins
        GoblinCount = randint(1,10)
        for x in range(GoblinCount):
            self.enemyList.append(Goblin(self.player))
        # Populate with Goatmen
        GoatmenCount = randint(1,3)
        for x in range(GoatmenCount):
            self.enemyList.append(Goatman(self.player))

    def EntranceMessage(self):
        Message = "%s enters the cave's lobby. It's damp, dark and smelly. " % self.player.name
        Message = Message + "All around are unfamiliar faces, worn out places, worn out faces. "
        Message = Message + "%s finds it kind of funny, they find it kind of sad. " % self.player.name
        print(Message)

    def AllEnemiesDead(self):
        pass
    def GoForward(self):
        # Check if we are not currently in combat
        if self.Explore() == False:
            # Increment steps
            self.playerSteps = self.playerSteps + 1
            # See if player should be tired
            self.SetPlayerTired()
            # If player has completed the level
            if self.playerSteps >= self.endSteps:
                print("%s beltches in excitment. The game is over.")
                self.player.health = 0
    def GoBack(self):
        # Check if we are not currently in combat
        if self.Explore() == False:
            # Go back one pace
            self.playerSteps = self.playerSteps -1
            # See if player should be tired
            self.SetPlayerTired()
            # If player has reached start of level
            if self.playerSteps >= 0:
                print("%s is back at the entrance of the cave.")
    def Explore(self):
        # If no more enemies are left
        if len(self.enemyList) == 0:
            print("%s looks around. All quiet here.")
            # Return false so when we try to move we can
            return False
        # If there are enemies
        else:
            # If player is current in a fight then enemy gets free attack
            if self.player.state != CharacterStates.Normal:
                print("%s is too busy right now!" % (self.player.name))
                self.player.enemy_attacks()
            else: # We grab a random enemy from the list and present to player
                # Get a random enemy
                randomEnemy = self.enemyList[randint(0, len(self.enemyList) -1)]
                # Remove from list
                self.enemyList.remove(randomEnemy)
                # Target player
                self.player.enemy = randomEnemy
                self.player.state = CharacterStates.Fight
                print("%s encounters %s!" % (self.player.name, randomEnemy.name))
                
            # Return true so when we try to move to do not
            return True
    def Status(self):
        # Output steps
        print("01 level steps: %d/%d" % (self.playerSteps, self.endSteps))
        # Output if there are still enemies
        if len(self.enemyList) > 0:
            print("%s senses enemies nearby" % self.player.name)
        else:
            print("%s looks around the damp cave lobby and doesn't notice much out of the ordinary" % self.player.name)

    def SetPlayerTired(self):
        # one in twenty chance of player becoming tired
        if randint(0,20) == 15:
            self.player.tired()





        


