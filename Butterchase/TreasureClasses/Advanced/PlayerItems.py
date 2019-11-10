# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes
from random import randint

def GetRandomMessage(Array):
    return Array[randint(0, len(Array) -1)]

##### GRACEO-ROMAN STYLE

#region Weapons
class Gladius(Treasure):
    pass
class Pila(Treasure):
    pass
class Hoplite(Treasure):
    pass
class Sarius(Treasure):
    pass
class Flax(Treasure):
    pass
#endregion

#region armour
class MailShirt(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 10, "Chainmail")
    def defenceFlavour(self, enemy):
        print("{0}'s {1} fails to piece's {2}'s {3}".format(enemy.name, enemy.weapon.name, self.player.name, self.name))
class LoricaHamata(Treasure):
    pass
class LoricaSquamata(Treasure):
    pass
class LinenShirt(Treasure):
    pass
class BreastPlate(Treasure):
    pass

#endregion   
# Item arrays that get reference
PlayerWeapons = [Gladius(), Pila(), Hoplite(), Sarius(), Flax()]
PlayerArmour = [MailShirt(), LoricaHamata(), LoricaSquamata(), LinenShirt(), BreastPlate()]

