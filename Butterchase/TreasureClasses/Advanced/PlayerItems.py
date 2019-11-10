# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes
from random import randint

def GetRandomMessage(Array):
    return Array[randint(0, len(Array) -1)]

#region Weapons
class Pike(Treasure):
        def __init__(self):
            Treasure.__init__(self, TreasureTypes.Weapon, 10, 0, "Pike")
        def attackFlavour(self, enemy):
            msg = "{0} is reeled by a brutal uppercut by {1}".format(enemy.name, self.player.name)
            msg1 = "{0} sidesteps {1} and delivers a body shot".format(self.player.name, enemy.name)
            msg2 = "{1} lunges forward, {0} ducks and headbutts their genitalia".format(enemy.name, self.player.name)
            msg3 = "{0} lands a jab on {1}".format(self.player.name, enemy.name)
            msgArray = [msg, msg1, msg2, msg3]
            print(GetRandomMessage(msgArray))
        def executionText(self, enemy):
            msg  = "{0} delivers a precise strike to the {1}'s juggular. {1} immediately tries to grasp their throat, but forgets to drop their weapon, their {2} damages their throat beyond all repair and they choke to death".format(self.player.name, enemy.name, enemy.weapon.name)
            msg1 = "{0} bursts through {1}'s chest cavity, pulls out their heart and eats it in front of them. Needless to say, {1} is dead.".format(self.player.name, enemy.name)
            msg2 = "{0} drops down dead. Don't ask how; writting new, creative, content is hard.".format(enemy.name)
            msg3 = "{0} charges at {1}, trips, and runs headfirst into the nearest Cave wall. Their head now resembles a half-eaten kinder egg".format(enemy.name, self.player.name)
            msgArray = [msg, msg1, msg2, msg3]
            print(GetRandomMessage(msgArray))
#endregion

#region armour
class Chainmail(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 10, "Chainmail")
    def defenceFlavour(self, enemy):
        print("{0}'s {1} fails to piece's {2}'s {3}".format(enemy.name, enemy.weapon.name, self.player.name, self.name)

#endregion   
# Item arrays that get reference
PlayerWeapons = [Pike()]
PlayerArmour = [Chainmail()]

