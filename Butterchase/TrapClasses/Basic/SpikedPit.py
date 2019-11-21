from TrapClasses.Trap import Trap

class SpikedPit(Trap):
    def __init__(self):
        Trap.__init__(self, 0, 12, 2, 6, False, "Spiked Pit")
    # Method to be called if player is hurt by trap
    def PlayerHurt(self, player):
        msg = "The ground gives way to reveal a 5 foot drop, and a pit filled with vicious spikes. Spikes and {0}'s face do not make for good bedfellows".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player is killed by trap
    def PlayerKilled(self, player):
        msg = "The ground gives way to reveal a 5 foot drop, and a pit filled with vicious spikes. {0} falls, one of the spikes impales them and they lie there... bleeding out... not a fun way to go".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player avoids trap
    def PlayerAvoided(self, player):
        msg = "{0} hesitates as they put their foot forward. They reach out with their {1} and poke the ground ahead, it's loose and hollow. One large rock later and {0} is staring at a 5 foot drop with vicious metallic spikes at the bottom. Lucky they avoided it.".format(player.name, player.weapon.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player triggers trap but is not damage
    def PlayerBlocked(self, player):
        msg = "The ground gives way to reveal a 5 foot drop, and a pit filled with vicious spikes. {0} falls, but luckily their {1} blocks any harm that the spikes might do. They climb out the pit, the only injury a slight embarassment.".format(player.name, player.armour.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
