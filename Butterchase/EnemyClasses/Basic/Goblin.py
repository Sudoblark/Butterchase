from BaseClasses.Enemy import Enemy

class Goblin(Enemy):
    def __init__(self, player, enemyName):
        Enemy.__init__(player, (enemyName + " the Goblin"), 1, 10, 1, 5, False, True)
    