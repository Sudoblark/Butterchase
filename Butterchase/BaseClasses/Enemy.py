from random import randint
from BaseClasses.Character import Character

class Enemy(Character):
  def __init__(self, player, enemyName, minHealth, maxHealth, minattack, maxattack, 
  ineffectiveAttacks, row, column, evadeInt):
    Character.__init__(self)
    self.name = enemyName
    self.health = randint(minHealth, maxHealth)
    self.health_max = maxHealth
    self.baseAttack = [minattack, maxattack]
    self.adjustedAttack = [minattack, maxattack]
    self.ineffectiveAttacks = ineffectiveAttacks
    self.row = row
    self.column = column
    self.baseDefence = 0
    self.adjustedDefence = 0
    self.evadeAttack = [0,evadeInt]
