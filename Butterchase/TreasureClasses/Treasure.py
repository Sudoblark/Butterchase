from enum import Enum

# Treasure type enum
class TreasureTypes(Enum):
    Weapon = 0
    Armour = 1


# Base class for treasure
class Treasure():
    def __init__(self, ItemType, attack, defence, attackFlavourText, defenceFlavourText):
        # check that item is of appropriate type
        if not isinstance(ItemType, TreasureTypes):
            raise TypeError("type must be an instance of the TreasureTypes Enum")
        # bind properties to class
        self.attack = attack
        self.armour = defence
        self.attackFlavour = attackFlavourText
        self.defenceFlavour = defenceFlavourText

    def equip(self, player):
        player.adjustedAttack += self.attack
        player.adjustedDefence += self.armour
        if self.attack != 0:
            player.attackFlavour = self.attackFlavour
        if self.armour != 0:
            player.defenceFlavour = self.defenceFlavour


    def unequip(self, player):
        player.adjustedAttack -= self.attack
        player.adjustedDefence -= self.armour




