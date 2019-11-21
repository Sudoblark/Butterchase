from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util
from TreasureClasses.Basic import GoblinItems
from random import randint

class Goblin(Enemy):
    def __init__(self, player, row, column):
        Name = Util.ReturnName(Util.PossibleClasses.Goblin)
        Enemy.__init__(self, player, Name, 1, 10, 1, 5, True, row, column, 3)

        # equip random items
        self.weapon = GoblinItems.GoblinWeapons[randint(0,(len(GoblinItems.GoblinWeapons)-1))]
        self.armour = GoblinItems.GoblinArmour[randint(0,(len(GoblinItems.GoblinArmour) -1))]
        self.weapon.player = self
        self.armour.player = self
        self.weapon.equip()
        self.armour.equip()
    