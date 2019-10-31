from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Goblin(Enemy):
    def __init__(self, player):
        Enemy.__init__(player, (Util.ReturnName(Util.PossibleClasses.Goblin)), 1, 10, 1, 5, False, True)
    