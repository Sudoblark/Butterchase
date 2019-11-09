# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes
from random import randint

def GetRandomMessage(Array):
    return Array[randint(0, len(Array) -1)]

#region Weapons
class Hands(Treasure):
        def __init__(self):
            Treasure.__init__(self, TreasureTypes.Weapon, 1, 0, "Bare Hands")
        def attackFlavour(self, enemy):
            msg = "{1} is reeled by a brutal uppercut by {2}".format(enemy.name, self.player.name)
            msg1 = "{0} sidesteps {1} and delivers a body shot".format(self.player.name, enemy.name)
            msg2 = "{1} lunges forward, {2} ducks and headbutts their genitalia".format(enemy.name, self.player.name)
            msg3 = "{0} lands a jab on {2}".format(self.player.name, enemy.name)
            msgArray = [msg, msg1, msg2, msg3]
            print(GetRandomMessage(msgArray))
        def executionText(self, enemy):
            msg  = "{0} delivers a precise strike to the {1}'s juggular. {1} immediately tries to grasp their throat, but forgets to drop their weapon, their {2} damages their throat beyond all repair and they choke to death".format(self.player.name, enemy.name, enemy.weapon.name)
            msg1 = "{0} bursts through {1}'s chest cavity, pulls out their heart and eats it in front of them. Needless to say, {1} is dead.".format(self.player.name, enemy.name)
            msg2 = "{0} drops down dead. Don't ask how; writting new, creative, content is hard.".format(enemy.name)
            msg3 = "{0} charges at {1}, trips, and runs headfirst into the nearest Cave wall. Their head now resembles a half-eaten kinder egg".format(enemy.name, self.player.name)
            msgArray = [msg, msg1, msg2, msg3]
            print(GetRandomMessage(msgArray))
class IdioticSword(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon,2,0,"Idiotic Sword")
    def attackFlavour(self, enemy):
        msg = "{0} slices at {1}, a barely noticable scratch is the only result".format(self.player.name, enemy.name)
        msg1 = "{0}'s lower jaw is knocked slightly askew by the pummel of {1}'s {2}".format(enemy.name, self.player.name, self.name)
        msg2 = "{0} yells in anger and runs at {1} with their {2} held high. They bounce off of {1}'s {3} with no noticable affect.".format(self.player.name, enemy.name, self.name, enemy.armour.name)
        msg3 = "{1} walks into {0}'s {2}. Idiot.".format(enemy.name, self.player.name, self.name)
        msgArray = [msg, msg1, msg2, msg3]
        print(GetRandomMessage(msgArray))
    def executionText(self, enemy):
        msg = "{0} swears that {1} walked into their {2}. {1} walked into it 15 times... and dies. Idiot.".format(self.player.name, enemy.name, self.name)
        msg1 = "{0} impales {1} on their {2}. {0} pulls their {2} out of {1}'s limb body.".format(self.player.name, enemy.name, self.name)
        msg2 = "{1} attempts to grab {0}'s weapon. It's rusty, dirty, contaminated... Pathogens enter {1}'s blood stream, destroy their immune system, and cause {1} to instantly die from accute too-many-crisps syndrome.".format(self.player.name, enemy.name)
        msgArray = [msg, msg1, msg2]
        print(GetRandomMessage(msgArray))
class WoodenClub(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon, 3, 0, "Wooden Club")
    def attackFlavour(self, enemy):
        msg = "{0} wacks {1} upside the head. {0} isn't sure if the woodemn thud comes from {1} or {2}".format(self.player.name, enemy.name, self.name)
        print(msg)
    def executionText(self, enemy):
        msg = "{0} brings the {1} crashing down upon the skull of {2}. A dull grunt escapes {2}'s lips, ".format(self.player.name, self.name, enemy.name)
        msg = msg + "the sort of noise you'd expect from a distressed potato. {0} follows up; a couple of wacks later ".format(self.player.name)
        msg = msg + "and all that remains of {0} may be said to resemble mashed potato with ketchup.".format(enemy.name)
        print(msg)

#endregion

#region armour
class IdioticArmour(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 1, "Loin Cloth")
    def defenceFlavour(self, enemy):
        print("%s recoils in disgust, %s's %s is far too revealing" % (enemy.name, self.player.name, self.name))

#endregion
PlayerHands = Hands()
PlayerIdioticSword = IdioticSword()
PlayerWoodenClub = WoodenClub()

    

TestArmour = IdioticArmour()    
# Item arrays that get reference
PlayerWeapons = [Hands(), IdioticSword(), WoodenClub()]
PlayerArmour = [TestArmour]

