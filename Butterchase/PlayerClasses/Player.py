# Required for sleep check
from random import randint
# Required to hold states
from BaseClasses.CharacterStates import CharacterStates
from BaseClasses.Character import Character
from BaseClasses.Enemy import Enemy



# Player class
class Player(Character):
    # Constructor
    def __init__(self):
        self.state = "normal"
        self.health = 10
        self.health_max = 10
        self.minAttack = 0
        self.maxAttack = 10
        self.enemy = None
        self.state = CharacterStates.Normal
        self.ineffectiveAttacks = False
    # Quit option
    def quit(self):
        print("%s has died of dysentery.\n" % self.name)
        self.health = 0
    # Help option
    def help(self):
        print(Commands.keys())
    # Status option
    def status(self):
        print("%s's health: %d/%d" % (self.name, self.health, self.health_max))
    # tired option
    def tired(self):
        print("%s feels tired." %  (self.name))
    # Rest option
    def rest(self):
        if self.state != CharacterStates.Normal:
            print("%s can't rest right now!" %(self.name))
            self.enemy_attacks()
        else:
            print("%s rests" % (self.name))
            if self.health < self.health_max:
                # If not at full health then increment by one after rest
                self.health = self.health + 1
                print("%s feels a little healthier now." % (self.name))
    # Explore option
    def explore(self):
        if self.state != CharacterStates.Normal:
            print("%s is too busy right now!" % (self.name))
            # Enemy attacks when char tried to explore during a fight
            self.enemy_attacks()
        else:
            # logic to explore stuff
            if randint(0,1):
                self.enemy = Enemy(self, "Steve the test goblin",2,10,1,5,False)
                self.state = CharacterStates.Fight
                print("%s encounters %s!" % (self.name, self.enemy.name))
            else:
                if randint(0,1):
                    self.tired()
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
                print("%s feels from %s" % (self.name, self.enemy.name))
                self.enemy = None
                self.state = CharacterStates.Normal
                self.tired()
    # attaaaack
    def attack(self):
        if self.state != CharacterStates.Fight:
            print("%s swats the air, without any noticable results. The cave walls offer silent judgment on their life choices." % self.name)
        else:
            if self.do_damage(self.enemy):
                print("%s executes %s!" % (self.name, self.enemy.name))
                self.enemy = None
                self.state = CharacterStates.Normal
                if (randint(0, self.health) < 10):
                    self.health = self.health + 1
                    self.health_max = self.health_max +1
                    print("%s feels stronger!" % (self.name))
            else:
                self.enemy_attacks()
    


    # Enemy attack option
    def enemy_attacks(self):
        if self.enemy.do_damage(self):
            print("%s was slaughtered by %s!!" % (self.name, self.enemy.name))





Commands = {
    'quit' : Player.quit,
    'help' : Player.help,
    'status' : Player.status,
    'rest' : Player.rest,
    'explore' : Player.explore,
    'flee' : Player.flee,
    'attack' : Player.attack,
}
