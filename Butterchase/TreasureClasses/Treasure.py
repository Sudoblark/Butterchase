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
        self.currentEquipped = False

    # Equip action
    def equip(self):
        self.player.adjustedAttack[0] += self.attack
        self.player.adjustedAttack[1] += self.attack
        self.player.adjustedDefence += self.armour
        self.currentEquipped = True
    # Unequip action
    def unequip(self):
        self.player.adjustedAttack[0] -= self.attack
        self.player.adjustedAttack[1] -= self.attack
        self.player.adjustedDefence -= self.armour
        self.currentEquipped = False
    # Placeholder attack method, to be overwritten by instances of class
    def attackFlavour(self, enemy):
        pass
    # Placeholder defence method, to be overwritten by instances of class
    def defenceFlavour(self, enemy):
        pass
    # Placeholder execution method, to be overwritten by instances of class
    def executionText(self, enemy):
        pass


