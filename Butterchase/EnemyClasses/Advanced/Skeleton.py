from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Skeleton(Enemy):
    def __init__(self, player):
        Name = Util.ReturnName(Util.PossibleClasses.Skeleton)
        Enemy.__init__(self, player, Name, 17, 30, 12, 16, False)
    