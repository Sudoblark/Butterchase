# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes
#region weapons
class PintGlass(Treasure):
    pass
class SteelChair(Treasure):
    pass
class BrassKnuckles(Treasure):
    pass
class SnookerCue(Treasure):
    pass
class Keg(Treasure):
    pass
#endregion weapons
    
#region armour
class BinLid(Treasure):
    pass
class BeerCans(Treasure):
    pass
class QuestionableHelmet(Treasure):
    pass
class PizzaBox(Treasure):
    pass
class Bio(Treasure):
    pass


#endregion armour  
# Item arrays that get reference
GoblinWeapons = [PintGlass(), SteelChair(), BrassKnuckles(), SnookerCue(), Keg()]
GoblinArmour = [BinLid(), BeerCans(), QuestionableHelmet(), PizzaBox(), Bio()]
