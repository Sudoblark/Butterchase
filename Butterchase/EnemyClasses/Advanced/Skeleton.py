from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Skeleton(Enemy):
    def __init__(self, player):
        Enemy.__init__(player, (Util.ReturnName(Util.PossibleClasses.Skeleton)), 17, 30, 12, 16, False)
    