from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Troll(Enemy):
    def __init__(self, player):
        Enemy.__init__(player, (Util.ReturnName(Util.PossibleClasses.Troll)), 30, 40, 19, 23, False)
    