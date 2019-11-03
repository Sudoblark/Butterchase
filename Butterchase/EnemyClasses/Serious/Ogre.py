from BaseClasses.Enemy import Enemy
from EnemyClasses.ClassSheets import Util

class Ogre(Enemy):
    def __init__(self, player, row, column):
        Name = Util.ReturnName(Util.PossibleClasses.Ogre)
        Enemy.__init__(self, player, Name, 32, 45, 21, 25, False, row, column)
    