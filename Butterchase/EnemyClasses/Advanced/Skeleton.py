from BaseClasses.Enemy import Enemy

class Skeleton(Enemy):
    def __init__(self, player, enemyName):
        Enemy.__init__(player, (enemyName + " the Skeleton"), 17, 30, 12, 16, False)
    