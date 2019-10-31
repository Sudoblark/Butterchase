#
# Util module to return name and stats based on provided class
from enum import Enum
import importlib
class PossibleClasses(Enum):
    Goatman = "GoatmanSheet"
    Goblin = "GoblinSheet"
    Ogre = "OgreSheet"
    Orc = "OrcSheet"
    Skeleton = "SkeletonSheet"
    Troll = "TrollSheet"

# Method to return name of char
def ReturnName(EnemyClass):
    if not isinstance(EnemyClass, PossibleClasses):
        raise TypeError("EnemyClass must be an instance of PossibleClasses Enum")
    # import file
    ClassModule = importlib.import_module("%s" % EnemyClass.value, "Butterchase.EnemyClasses.ClassSheets")
    return ClassModule.ReturnName()

# Method to return stats for char
def ReturnStats(EnemyClass):
    if not isinstance(EnemyClass, PossibleClasses):
        raise TypeError("EnemyClass must be an instance of PossibleClasses Enum")

if __name__ == "__main__":
    # Goatman Test
    print("")
    print ("Goatman random name 01: ", ReturnName(PossibleClasses.Goatman))
    print ("Goatman random name 02: ", ReturnName(PossibleClasses.Goatman))
    print ("Goatman random name 03: ", ReturnName(PossibleClasses.Goatman))
    print("")
    # Goblin Test
    print("")
    print ("Goblin random name 01: ", ReturnName(PossibleClasses.Goblin))
    print ("Goblin random name 02: ", ReturnName(PossibleClasses.Goblin))
    print ("Goblin random name 03: ", ReturnName(PossibleClasses.Goblin))
    print("")
    # Ogre Test
    print("")
    print ("Ogre random name 01: ", ReturnName(PossibleClasses.Ogre))
    print ("Ogre random name 02: ", ReturnName(PossibleClasses.Ogre))
    print ("Ogre random name 03: ", ReturnName(PossibleClasses.Ogre))
    print("")
    # Orc Test
    print("")
    print ("Orc random name 01: ", ReturnName(PossibleClasses.Orc))
    print ("Orc random name 02: ", ReturnName(PossibleClasses.Orc))
    print ("Orc random name 03: ", ReturnName(PossibleClasses.Orc))
    print("")
    # Skeleton Test
    print("")
    print ("Skeleton random name 01: ", ReturnName(PossibleClasses.Skeleton))
    print ("Skeleton random name 02: ", ReturnName(PossibleClasses.Skeleton))
    print ("Skeleton random name 03: ", ReturnName(PossibleClasses.Skeleton))
    print("")
    # Troll Test
    print("")
    print ("Troll random name 01: ", ReturnName(PossibleClasses.Troll))
    print ("Troll random name 02: ", ReturnName(PossibleClasses.Troll))
    print ("Troll random name 03: ", ReturnName(PossibleClasses.Troll))
    print("")
