from random import randint
from BaseClasses.Character import Character

class Enemy(Character):
  def __init__(self, player, enemyName, minHealth, maxHealth, minattack, maxattack, 
  ineffectiveAttacks, row, column):
    Character.__init__(self)
    self.name = enemyName
    self.health = randint(minHealth, maxHealth)
    self.health_max = maxHealth
    self.minAttack = minattack
    self.maxAttack = maxattack
    self.ineffectiveAttacks = ineffectiveAttacks
    self.row = row
    self.column = column
