# Import enum class 
from enum import Enum
# Class to hold all states that character may be in
class CharacterStates(Enum):
    Normal = 1
    Exploring = 2
    Fight = 3
