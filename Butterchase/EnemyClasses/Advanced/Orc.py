from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Orc(Enemy):
    def __init__(self, player):
        Name = Util.ReturnName(Util.PossibleClasses.Orc)
        Enemy.__init__(self, player, Name, 15, 25, 10, 14, False)
    