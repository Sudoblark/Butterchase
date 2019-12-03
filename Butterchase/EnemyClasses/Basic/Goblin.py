from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util
from TreasureClasses.Basic.Goblin.Items import Weapons, Armour
from random import randint

class Goblin(Enemy):
    def __init__(self, player, row, column):
        Name = Util.ReturnName(Util.PossibleClasses.Goblin)
        Enemy.__init__(self, player, Name, 1, 10, 1, 5, True, row, column, 3)

        # equip random items
        self.weapon = Weapons[randint(0,(len(Weapons)-1))]
        self.armour = Armour[randint(0,(len(Armour) -1))]
        self.weapon.player = self
        self.armour.player = self
        self.weapon.equip()
        self.armour.equip()
    