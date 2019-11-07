from enum import Enum

# Treasure type enum
class TreasureTypes(Enum):
    Weapon = 0
    Armour = 1

# Base class for treasure
class Treasure():
    def __init__(self, ItemType, attack, defence, name):
        # check that item is of appropriate type
        if not isinstance(ItemType, TreasureTypes):
            raise TypeError("type must be an instance of the TreasureTypes Enum")
        # bind properties to class
        self.attack = attack
        self.armour = defence
        self.name = name
        # To be assigned after creation
        self.player = None

    # Equip action
    def equip(self):
        self.player.adjustedAttack += self.attack
        self.player.adjustedDefence += self.armour
    # Unequip action
    def unequip(self, player):
        self.player.adjustedAttack -= self.attack
        self.player.adjustedDefence -= self.armour
    # Placeholder attack method, to be overwritten by instances of class
    def attackFlavour(self, enemy):
        pass
    # Placeholder defence method, to be overwritten by instances of class
    def defenceFlavour(self, enemy):
        pass
    # Placeholder execution method, to be overwritten by instances of class
    def executionText(self, enemy):
        pass


