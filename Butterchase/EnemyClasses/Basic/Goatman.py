from BaseClasses.Enemy import Enemy

class Goatman(Enemy):
    def __init__(self, player, enemyName):
        Enemy.__init__(player, (enemyName + " the Goatman"), 3, 15, 3, 7, True)
    