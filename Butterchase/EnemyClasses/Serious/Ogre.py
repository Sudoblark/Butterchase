from BaseClasses.Enemy import Enemy

class Ogre(Enemy):
    def __init__(self, player, enemyName):
        Enemy.__init__(player, (enemyName + " the Ogre"), 32, 45, 21, 25, False)
    