# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes

class PintGlass(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon, 2, 0, "Pint Glass")
    def attackFlavour(self, enemy):
        msg = "{0} takes a swig from his glass, beltches, then clogs {1} with their {2}".format(self.player.name, enemy.name, self.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    def executionText(self, enemy):
        msg = "{0} violently shatters their {1} over {2}'s head. {2} drops to the ground and doesn't get back up".format(self.player.name, self.name, enemy.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
