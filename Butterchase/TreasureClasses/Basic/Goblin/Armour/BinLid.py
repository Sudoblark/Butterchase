# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes

class BinLid(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 1, "Bin Lid")
    def defenceFlavour(self, enemy):
        print("{0} parries {1}'s {2} with their {3}".format(self.player.name, enemy.name, enemy.weapon.name, self.name))
