from TrapClasses.Trap import Trap

class Hole(Trap):
    def __init__(self):
        Trap.__init__(self, 1,1, 6, 12, True, "Hole")
    # Method to be called if player is hurt by trap
    def PlayerHurt(self, player):
        msg = "{0} falls into a giant hole in the ground and makes quite a load 'argg' noise. They could see the hole, why did they walk into it...".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player is killed by trap
    def PlayerKilled(self, player):
        msg = "{0} falls to their death down a sinkhole. Such a shame".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player avoids trap
    def PlayerAvoided(self, player):
        msg = "{0} steps around the giant hole in the ground. I don't know how; I thought I hardcoded this to be impossible".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player triggers trap but is not damage
    def PlayerBlocked(self, player):
        msg = "{0} tumbles down the giant hole, but luckily their {1} ensures only superificial damage is done".format(player.name, player.armour.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
