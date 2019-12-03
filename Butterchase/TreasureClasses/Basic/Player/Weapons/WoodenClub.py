# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes

class WoodenClub(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon, 4, 0, "Wooden Club")
    def attackFlavour(self, enemy):
        msg = "{0} wacks {1} upside the head. {0} isn't sure if the wooden thud comes from {1} or {2}".format(self.player.name, enemy.name, self.name)
        msg1 = "{1} is knock knocking knock on {0}'s head... ouch that must hurt".format(enemy.name, self.player.name)
        msg2 = "{0} ducks low, and manages to aggressively bring their {1} into contact with {2}'s left kneecap... ow".format(self.player.name, self.name, enemy.name)
        msg3 = "SNAP! That's the sound of the metacarpal bones in {0}'s hand being shattered by {1}'s {2}".format(enemy.name, self.player.name, self.name)
        msgArray = [msg, msg1, msg2, msg3]
        print(self.GetRandomMessage(msgArray))
    def executionText(self, enemy):
        msg = "{0} violently clumps {1} with {2}, turning their brain to mush".format(self.player.name, enemy.name, self.name)
        msg1 = "{0} howls in an angry bloodlust, feverishly reigning blows down upon {1}'s body until all that's left of their face is a gooey, unrecognisable, mess".format(self.player.name, enemy.name)
        msg2 = "{0} strikes {1}'s {2} with such force that it's no longer usable. Defenceless, {1} tries to grab the club but it's too late; {0} aggressively shatters their hands. {1}'s {3} holds, but their internal organs do not. They slump to the floor and do get up.".format(self.player.name, enemy.name, enemy.weapon.name, enemy.armour.name)
        msg3 = "{0} grunts 'me club {1}'. {0} clubs {1}, {0} clubs {1} 15 times until {1} stops moving".format(self.player.name, enemy.name)
        msgArray = [msg, msg1, msg2, msg3]
        print(self.GetRandomMessage(msgArray))
