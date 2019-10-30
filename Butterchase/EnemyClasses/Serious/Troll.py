from BaseClasses.Enemy import Enemy

class Troll(Enemy):
    def __init__(self, player, enemyName):
        Enemy.__init__(player, (enemyName + " the Troll"), 30, 40, 19, 23, False)
    