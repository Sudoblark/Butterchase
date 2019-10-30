from BaseClasses.Enemy import Enemy

class Orc(Enemy):
    def __init__(self, enemyName):
        Enemy.__init__(self, (enemyName + " the Orc"), 15, 25,)
