from random import randint

# Base class for traps
class Trap():
    def __init__(self, lowerRange, upperRange, lowerDamage, upperDamage, visible, name):
        # upper and lower ranges are used to determine if player is hit
        self.lowerRange = lowerRange
        self.upperRange = upperRange
        # These ranges are used to determine damage to the player
        self.lowerDamage = lowerDamage
        self.upperDamage = upperDamage
        # Visible determines if displayed on map
        self.visible = visible
        # Name may be used for flavour text
        self.name = name
    # Check if player is hit
    def IsPlayerHit(self, player):
        if randint(self.lowerRange, self.upperRange) == 1:
            # Calculcate damage inclusive of player's armour
            damage = randint(self.lowerDamage, self.upperDamage) - player.adjustedDefence
            # then apply damage to player
            player.health = player.health - damage
            # Check if player is dead
            if player.health <= 0:
                self.PlayerKilled()
            # Check if damage was dealt
            elif damage > 0:
                self.PlayerHurt()
            # Finally the only option left is for no damage to have been dealt
            else:
                self.PlayerBlocked()
        # If player is not hit then call avoided method
        else:
            self.PlayerAvoided()
    # Method to be called if player is hurt by trap
    def PlayerHurt(self):
        pass
    # Method to be called if player is killed by trap
    def PlayerKilled(self):
        pass
    # Method to be called if player avoids trap
    def PlayerAvoided(self):
        pass
    # Method to be called if player triggers trap but is not damage
    def PlayerBlocked(self):
        pass

