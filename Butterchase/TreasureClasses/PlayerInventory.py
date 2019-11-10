from PlayerClasses import Player

class PlayerInventory():
    def __init__(self, maxchar, player):
        self.maxChars = maxchar
        self.player = player
    def OutputInventory(self):
        ## Border
        HeaderBorder = list("-" * self.maxChars)
        ## Join to map
        HeaderGap = "|" + (" " * (self.maxChars - 2)) + "|"
        ## Header logic
        ## -4 to all multiplies to leave room for space + | at start and end
        Header = ("".join(HeaderBorder)) + ""
        Header += "\n"
        # Flavour text
        Flavour = "Inventory v0.1"
        Header += "| " + Flavour + (" " * (self.maxChars - len(Flavour) - 4)) + " |"
        Header += "\n"
        Flavour01 = "Your handy item management tool"
        Header += "| " + Flavour01 + (" " * (self.maxChars - len(Flavour01) - 4)) + " |"
        Header += "\n"
        Flavour02 = "for all your micromanagement needs!"
        Header += "| " + Flavour02 + (" " * (self.maxChars - len(Flavour02) - 4)) + " |"
        Header += "\n"
        Header += ("".join(HeaderBorder))
        Header += "\n"
        Header += HeaderGap
        print(Header)
    def OutputWeapons(self, weaponList):
        # sword (+1 attack)   spear (+2 attack)
        # blah (+1 attack - equipped)
        pass
    def OutputArmour(self, armourList):
        # leather armour (+1 defence)
        # cloth (+1 defence)  bed pan (+0 defence - equipped)
        pass


    #OUTPUT A TABLE WITH STATS SHOWN - USE SAME SORT OF LOGIC AS SHOWMAP
