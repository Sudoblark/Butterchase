from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Goatman(Enemy):
    def __init__(self, player):
        Enemy.__init__(player, (Util.ReturnName(Util.PossibleClasses.Goatman)), 3, 15, 3, 7, True)
    