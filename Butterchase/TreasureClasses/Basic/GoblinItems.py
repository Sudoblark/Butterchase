# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes


def GetRandomMessage(Array):
    return Array[randint(0, len(Array) -1)]

#region weapons
class PintGlass(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon, 2, 0, "Pint Glass")
    def attackFlavour(self, enemy):
        msg = "{0} takes a swig from his glass, beltches, then clogs {1} with their {2}".format(self.player.name, enemy.name, self.name)
        msgarray = [msg]
        print(GetRandomMessage(msgArray))
    def executionText(self, enemy):
        msg = "{0} violently shatters their {1} over {2}'s head. {2} drops to the ground and doesn't get back up".format(self.player.name, self.name, enemy.name)
        msgarray = [msg]
        print(GetRandomMessage(msgArray))


class SteelChair(Treasure):
    pass
class BrassKnuckles(Treasure):
    pass
class SnookerCue(Treasure):
    pass
class Keg(Treasure):
    pass
#endregion weapons
    
#region armour
class BinLid(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 1, "Bin Lid")
    def defenceFlavour(self, enemy):
        print("{0} parries {1}'s {2} with their {3}".format(self.player.name, enemy.name, enemy.weapon.name, self.name))
class BeerCans(Treasure):
    pass
class QuestionableHelmet(Treasure):
    pass
class PizzaBox(Treasure):
    pass
class Bio(Treasure):
    pass


#endregion armour  
# Item arrays that get reference
GoblinWeapons = [PintGlass()]
GoblinArmour = [BinLid()]
