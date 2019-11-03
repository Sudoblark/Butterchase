from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Goatman(Enemy):
    def __init__(self, player, row, column):
        Name = Util.ReturnName(Util.PossibleClasses.Goatman)
        Enemy.__init__(self, player, Name, 3, 15, 3, 7, True, row, column)
    