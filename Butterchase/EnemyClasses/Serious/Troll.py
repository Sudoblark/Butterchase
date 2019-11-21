from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Troll(Enemy):
    def __init__(self, player):
        Name = Util.ReturnName(Util.PossibleClasses.Troll)
        Enemy.__init__(self, player, Name, 30, 40, 19, 23, False, 50)
    