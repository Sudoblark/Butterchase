####
# Created: 30/10/2019
# Base character class
# 
# Base class for all character in the game
# Ensures all characters have the same base properties and methods
####
# Required to calculate damage
from random import randint
# Required to hold state
from BaseClasses.CharacterStates import CharacterStates


class Character:
    # Constructor
    def __init__(self):
        self.name = ""
        self.health = 1
        self.health_max = 1
        self.minAttack = 0
        self.maxAttack = 1
        self.ineffectiveAttacks = True
        self.state = CharacterStates.Normal

    # Method to allow all characters to attack
    def do_damage(self, enemy, isTired):
        # Calculate damage
        damage = randint(self.minAttack, self.maxAttack)
        # If char is tired then half damage
        if isTired:
            damage = damage / 2
        # Calculcate enemy new health
        enemy.health = enemy.health - damage
        # Print
        self.print_damage(enemy, damage)
        # Return if dead
        return enemy.health <= 0
    # Method to print attack message
    def print_damage(self, enemy, damage):
        if damage == 0 & self.ineffectiveAttacks == True: 
            print ("%s is totally unphased by %s's attack" % (enemy.name, self.name))
        elif damage == 0: 
            print ("%s evades %s's attack." % (enemy.name, self.name))
        else: 
            print ("%s hurts %s!" %( self.name, enemy.name))
