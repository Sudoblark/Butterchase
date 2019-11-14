# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes
from random import randint

def GetRandomMessage(Array):
    return Array[randint(0, len(Array) -1)]

##### Anglo Saxon style items
#region Weapons
class Hands(Treasure):
        def __init__(self):
            Treasure.__init__(self, TreasureTypes.Weapon, 1, 0, "Bare Hands")
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
            msg3 = "{0} charges at {1}, trips, and lands headfirst into the nearest Cave wall. Their head now resembles a half-eaten kinder egg".format(enemy.name, self.player.name)
            msgArray = [msg, msg1, msg2, msg3]
            print(GetRandomMessage(msgArray))
class IdioticSword(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon,3,0,"Idiotic Sword")
    def attackFlavour(self, enemy):
        msg = "{0} slices at {1}, a barely noticable scratch is the only result".format(self.player.name, enemy.name)
        msg1 = "{0}'s lower jaw is knocked slightly askew by the pummel of {1}'s {2}".format(enemy.name, self.player.name, self.name)
        msg2 = "{0} yells in anger and runs at {1} with their {2} held high. They bounce off of {1}'s {3} with no noticable affect.".format(self.player.name, enemy.name, self.name, enemy.armour.name)
        msg3 = "{1} walks into {0}'s {2}. Idiot.".format(enemy.name, self.player.name, self.name)
        msgArray = [msg, msg1, msg2, msg3]
        print(GetRandomMessage(msgArray))
    def executionText(self, enemy):
        msg = "{0} swears that {1} walked into their {2}. {1} walked into it 15 times... and died. Idiot.".format(self.player.name, enemy.name, self.name)
        msg1 = "{0} impales {1} on their {2}. {0} pulls their {2} out of {1}'s now lifeless body.".format(self.player.name, enemy.name, self.name)
        msg2 = "{1} attempts to grab {0}'s weapon. It's rusty, dirty, contaminated... Pathogens enter {1}'s blood stream, destroy their immune system, and cause {1} to instantly die from accute too-many-crisps syndrome.".format(self.player.name, enemy.name)
        msg3 = "{0} parry's an attack from {1}'s {2}, twirls round and slices through the {3} protecting {1}'s vital organs. {1} slumps to the floor, limp and unmoving...".format(self.player.name, enemy.name, enemy.weapon.name, enemy.armour.name)
        msgArray = [msg, msg1, msg2]
        print(GetRandomMessage(msgArray))
class WoodenClub(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon, 4, 0, "Wooden Club")
    def attackFlavour(self, enemy):
        msg = "{0} wacks {1} upside the head. {0} isn't sure if the woodemn thud comes from {1} or {2}".format(self.player.name, enemy.name, self.name)
        print(msg)
    def executionText(self, enemy):
        msg = "{0} clumps {1} with {2}, turning their brain to mush".format(self.player.name, enemy.name, self.name)
        print(msg)
class Seax(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon, 5, 0, "Seax")
class Spear(Treasure):
    pass
#endregion

#region armour
class IdioticArmour(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 1, "Loin Cloth")
    def defenceFlavour(self, enemy):
        print("%s recoils in disgust, %s's %s is far too revealing" % (enemy.name, self.player.name, self.name))
class BasicShield(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 3, "Scutum")
    def defenceFlavour(self,enemy):
        pass
class LeatherArmour(Treasure):
    pass
class StuddedLeatherArmour(Treasure):
    pass
class Doublet(Treasure):
    pass

#endregion
# Item arrays that get reference
PlayerWeapons = [Hands(), IdioticSword(), WoodenClub()]
PlayerArmour = [IdioticArmour()]

