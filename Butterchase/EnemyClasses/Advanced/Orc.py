from BaseClasses.Enemy import Enemy

class Orc(Enemy):
    def __init__(self, player, enemyName):
        Enemy.__init__(player, (enemyName + " the Orc"), 15, 25, 10, 14, False)
    