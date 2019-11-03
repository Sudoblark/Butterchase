from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Goblin(Enemy):
    def __init__(self, player, row, column):
        Name = Util.ReturnName(Util.PossibleClasses.Goblin)
        Enemy.__init__(self, player, Name, 1, 10, 1, 5, True, row, column)
    