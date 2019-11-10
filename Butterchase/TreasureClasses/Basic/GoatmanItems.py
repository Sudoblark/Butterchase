# Import base
from Treasure import Treasure, TreasureTypes


#region weapons
class Claws(Treasure):
    pass
class Horns(Treasure):
    pass
class Teeth(Treasure):
    pass
class Hands(Treasure):
    pass
class Legs(Treasure):
    pass
#endregion weapons

#region armour
class Cuteness(Treasure):
    pass
class Fur(Treasure):
    pass
class Harness(Treasure):
    pass
class Collar(Treasure):
    pass
class Growl(Treasure):
    pass
#endregion armour

# Item arrays that get reference
GoatmanWeapons = [Claws(), Horns(), Teeth(), Hands(), Legs()]
GoatmanArmour = [Cuteness(), Fur(), Harness(), Collar(), Growl()]
