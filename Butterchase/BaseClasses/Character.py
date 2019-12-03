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
        self.baseAttack = [0, 10]
        self.adjustedAttack = [0, 10]
        self.baseDefence = 0
        self.adjustedDefence = 0
        self.ineffectiveAttacks = True
        self.state = CharacterStates.Normal
        self.evadeAttack = [0,100]
        # equip random items
        self.weapon = None
        self.armour = None

    # Method to allow all characters to attack
    def do_damage(self, enemy, isTired):
        # Calculate damage and subtract chars defence
        damage = randint(self.adjustedAttack[0], self.adjustedAttack[1]) - enemy.adjustedDefence
        # See if enemy evades
        if randint(enemy.evadeAttack[0],enemy.evadeAttack[1]) == 1:
            damage = 0
            evaded = True
        else:
            evaded = False
        # If char is tired,enemy has not evaded, and damage is greater than one
        if (isTired) & (evaded == False) & (damage > 1):
            damage = damage // 2
        # Calculcate enemy new health if enemy did not evade and damage was dealt
        if (evaded == False)  & (damage > 0):
            enemy.health = enemy.health - damage
        # Print results
        self.print_damage(enemy, damage, evaded)
        # Return if dead
        return enemy.health <= 0
    # Method to print attack message
    def print_damage(self, enemy, damage, enemyEvaded):
        # If enemy evaded
        if enemyEvaded == True:
            print("%s evades %s's attack." % (enemy.name, self.name))
        #If no damage done
        elif damage <= 0:
            enemy.armour.defenceFlavour(self)
        # Else
        elif damage >= 1:
            self.weapon.attackFlavour(enemy)
