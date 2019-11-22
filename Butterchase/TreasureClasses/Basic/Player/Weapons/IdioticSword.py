# Import base
from TreasureClasses.Treasure import Treasure, TreasureTypes

class IdioticSword(Treasure):
    def __init__(self):
        Treasure.__init__(self, TreasureTypes.Weapon,3,0,"Idiotic Sword")
    def attackFlavour(self, enemy):
        msg = "{0} slices at {1}, a barely noticable scratch is the only result".format(self.player.name, enemy.name)
        msg1 = "{0}'s lower jaw is knocked slightly askew by the pummel of {1}'s {2}".format(enemy.name, self.player.name, self.name)
        msg2 = "{0} yells in anger and runs at {1} with their {2} held high. They bounce off of {1}'s {3} with no noticable affect.".format(self.player.name, enemy.name, self.name, enemy.armour.name)
        msg3 = "{1} walks into {0}'s {2}. Idiot.".format(enemy.name, self.player.name, self.name)
        msgArray = [msg, msg1, msg2, msg3]
        print(self.GetRandomMessage(msgArray))
    def executionText(self, enemy):
        msg = "{0} swears that {1} walked into their {2}. {1} walked into it 15 times... and died. Idiot.".format(self.player.name, enemy.name, self.name)
        msg1 = "{0} impales {1} on their {2}. {0} pulls their {2} out of {1}'s now lifeless body.".format(self.player.name, enemy.name, self.name)
        msg2 = "{1} attempts to grab {0}'s weapon. It's rusty, dirty, contaminated... Pathogens enter {1}'s blood stream, destroy their immune system, and cause {1} to instantly die from accute too-many-crisps syndrome.".format(self.player.name, enemy.name)
        msg3 = "{0} parry's an attack from {1}'s {2}, twirls round and slices through the {3} protecting {1}'s vital organs. {1} slumps to the floor, limp and unmoving...".format(self.player.name, enemy.name, enemy.weapon.name, enemy.armour.name)
        msgArray = [msg, msg1, msg2, msg3]
        print(self.GetRandomMessage(msgArray))
