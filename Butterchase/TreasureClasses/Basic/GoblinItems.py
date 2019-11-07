# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes

class IdioticSword(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon,4,0,"Idiotic Sword")
    def attackFlavour(self, enemy):
        print("%s somehow manages to swat %s with his bloody stupid sword" % (self.player.name, enemy.name))
    def executionText(self, enemy):
        print("Bloody hell. %s actually managed to kill %s with this %s." % (self.player.name, enemy.name, self.name))

class IdioticArmour(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Armour, 0, 5, "Loin Cloth")
    def defenceFlavour(self, enemy):
        print("%s recoils in disgust, %s's %s is far too revealing" % (enemy.name, self.player.name, self.name))

    
TestWeapon = IdioticSword()
TestArmour = IdioticArmour()    
# Item arrays that get reference
GoblinWeapons = [TestWeapon]
GoblinArmour = [TestArmour]
