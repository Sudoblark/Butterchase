from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Orc(Enemy):
    def __init__(self, player):
        Enemy.__init__(player, (Util.ReturnName(Util.PossibleClasses.Orc)), 15, 25, 10, 14, False)
    