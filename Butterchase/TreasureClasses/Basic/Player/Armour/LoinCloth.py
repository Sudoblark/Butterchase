# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes

class LoinCloth(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 1, "Loin Cloth")
    def defenceFlavour(self, enemy):
        print("%s recoils in disgust, %s's %s is far too revealing" % (enemy.name, self.player.name, self.name))
class BasicShield(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 3, "Scutum")
    def defenceFlavour(self,enemy):
        msg = "{0} manages to raise their Scutum just in time, catching {1}'s {2} and deflecting the damage".format(self.player.name, enemy.name, enemy.weapon.name)
        print(msg)
