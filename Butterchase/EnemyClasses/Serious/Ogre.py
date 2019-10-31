from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Ogre(Enemy):
    def __init__(self, player):
        Enemy.__init__(player, (Util.ReturnName(Util.PossibleClasses.Ogre)), 32, 45, 21, 25, False)
    