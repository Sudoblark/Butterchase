from TrapClasses.Trap import Trap

class SimplePit(Trap):
    def __init__(self):
        Trap.__init__(self, 0, 6, 1, 5, False, "Simple Pit")
    # Method to be called if player is hurt by trap
    def PlayerHurt(self, player):
        msg = "As {0} steps forward the ground suddenly gives way, revealing a bit that they subsequently fall face-first in to. Ouch.".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player is killed by trap
    def PlayerKilled(self, player):
        msg = "As {0} steps forward the ground suddenly gives way, below is a 30 foot drop... {0} screams but to no avail; with a muted 'crunch' their body makes contact with the compact earth and there's silence.".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player avoids trap
    def PlayerAvoided(self, player):
        msg = "As {0} steps forward the ground suddenly gives way. Just as they're about to tumble headfirst into the pit, {0} manages to steady themselves and take a step back from the precipice. Phew... close call.".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
    # Method to be called if player triggers trap but is not damage
    def PlayerBlocked(self, player):
        msg = "As {0} steps forward the ground suddenly gives way. They tumble and fall into the pit below. Luckily (or not) it appears they're not the first to sucum to this trickery; the bodies below break their fall and ensure no damage is done".format(player.name)
        msgArray = [msg]
        print(self.GetRandomMessage(msgArray))
