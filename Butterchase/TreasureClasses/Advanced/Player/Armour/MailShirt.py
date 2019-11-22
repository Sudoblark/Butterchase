# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes

class MailShirt(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 10, "Chainmail")
    def defenceFlavour(self, enemy):
        print("{0}'s {1} fails to piece's {2}'s {3}".format(enemy.name, enemy.weapon.name, self.player.name, self.name))
