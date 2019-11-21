# Required for sleep check and random items
from random import randint
# Required to hold states
from BaseClasses.CharacterStates import CharacterStates
from BaseClasses.Character import Character
from BaseClasses.Enemy import Enemy
from TreasureClasses.Basic import PlayerItems
from TreasureClasses.PlayerInventory import PlayerInventory



# Player class
class Player(Character):
    # Constructor
    def __init__(self):
        self.name = "Placeholder"
        self.health = 10
        self.health_max = 10
        self.enemy = None
        self.state = CharacterStates.Normal
        self.ineffectiveAttacks = False
        self.isTired = False
        self.level = None

        # Values for inventory attack
        self.baseAttack = [0, 10]
        self.adjustedAttack = [0, 10]
        # Values for inventory defence
        self.baseDefence = 0
        self.adjustedDefence = 0
        # Evade chance
        self.adjustedEvadeChance = 6
        self.evadeAttack = [0, self.adjustedEvadeChance]
        
        # equip random items
        weaponTemp = PlayerItems.PlayerWeapons[randint(0,(len(PlayerItems.PlayerWeapons)-1))]
        self.weapon = weaponTemp
        armourTemp = PlayerItems.PlayerArmour[randint(0,(len(PlayerItems.PlayerArmour) -1))]
        self.armour = armourTemp
        self.weapon.player = self
        self.armour.player = self
        self.weapon.equip()
        self.armour.equip()
        # add to new list of items for inventory purposes
        self.weaponList = [weaponTemp]
        self.armourList = [armourTemp]
        # track killed enemies
        self.killedEnemies = 0
        # track stat level
        self.statLevel = 0
        # inventory management
        self.inventoryManager = PlayerInventory(100, self)

    # Quit option
    def quit(self):
        print("%s has died of dysentery.\n" % self.name)
        self.health = 0
    # Help option
    def help(self):
        print(Commands.keys())
    # Status option
    def status(self):
        # health and tired and general stats
        print("Name: {0}".format(self.name))
        print("Health: {0}/{1}".format(self.health, self.health_max))
        print("Tired: {0}".format(self.isTired))
        print("Stat Level: {0}".format(self.statLevel))
        print("Enemies killed: {0}".format(self.killedEnemies))

        # attack and defence
        print("Attack range: {0} - {1}".format(self.adjustedAttack[0], self.adjustedAttack[1]))
        print ("Defence: {0}".format(self.adjustedDefence))
        # equipped items
        print("Equipped weapon: {0} (+{1} attack)".format(self.weapon.name, self.weapon.attack))
        print("Equipped armour: {0} (+{1} defence)".format(self.armour.name, self.armour.armour))

        self.level.Status()
    # tired option
    def tired(self):
        if self.isTired != True:
            self.isTired = True
            print("%s feels tired." %  (self.name))
    # Rest option
    def rest(self):
        if self.state != CharacterStates.Normal:
            print("%s can't rest right now!" %(self.name))
            self.enemy_attacks()
        else:
            # Rest up
            print("%s rests" % (self.name))
            # Clear tired state
            self.isTired = False
            if self.health < self.health_max:
                # If not at full health then increment by one after rest
                self.health = self.health_max
                print("%s feels refreshed." % (self.name))
    # Explore option
    def explore(self):
        self.level.Explore()
    # Run away!
    def flee(self):
        if self.state != CharacterStates.Fight:
            print("%s runs around hopelessly in circles for a while." % self.name)
            self.tired()
        else:
            # Make a dice roll to see if they escape
            diceResult = randint(1,6)
            if diceResult == 1:
                print("%s trips whilst attempting to flee." % self.name)
                self.tired()
                self.enemy_attacks()
                self.enemy_attacks()
            elif (diceResult > 1) & diceResult < 3:
                print("%s was unable to flee!" % self.name)
                self.tired()
            else:
                print("%s flee from %s" % (self.name, self.enemy.name))
                self.enemy = None
                self.state = CharacterStates.Normal
                self.tired()
    # attaaaack
    def attack(self):
        if self.state != CharacterStates.Fight:
            print("%s swats the air, without any noticable results. The cave walls offer silent judgment on their life choices." % self.name)
        else:
            if self.do_damage(self.enemy, self.isTired):
                self.weapon.executionText(self.enemy)
                self.killedEnemies += 1
                # Remove enemy from level
                self.level.RemoveItem(self.enemy.row, self.enemy.column)
                # Set player enemy to none
                self.enemy = None
                # Set fight state to normal
                self.state = CharacterStates.Normal
                if (randint(0, self.health) < 10):
                    self.health = self.health + 1
                    self.health_max = self.health_max + 1
                    self.adjustedAttack[0] += 1
                    self.adjustedAttack[1] += 1
                    self.adjustedDefence += 1
                    self.statLevel += 1

                    print("%s feels stronger!" % (self.name))
            else:
                self.enemy_attacks()
    # Enemy attack option
    def enemy_attacks(self):
        if self.enemy.do_damage(self, False):
            self.enemy.weapon.executionText(self)
    # Go forward in level option
    def levelLeft(self):
        self.level.GoLeft()
    def levelRight(self):
        self.level.GoRight()
    def levelUp(self):
        self.level.GoUp()
    def levelDown(self):
        self.level.GoDown()
    def level_map(self):
        self.level.showMap()
    def inventory(self):
        self.inventoryManager.PlayerInteraction()





Commands = {
    'quit' : Player.quit,
    'help' : Player.help,
    'status' : Player.status,
    'rest' : Player.rest,
    'explore' : Player.explore,
    'flee' : Player.flee,
    'attack' : Player.attack,
    'goRight' : Player.levelRight,
    'goLeft': Player.levelLeft,
    'goUp': Player.levelUp,
    'goDown' :  Player.levelDown,
    'showMap' : Player.level_map,
    'inventory' : Player.inventory,
}
