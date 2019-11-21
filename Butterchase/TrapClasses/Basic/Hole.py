from TrapClasses.Trap import Trap

class Hole(Trap):
    def __init__(self):
        Trap.__init__(1,1, 6, 12, True, "Hole")

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
