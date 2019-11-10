from PlayerClasses import Player

class PlayerInventory():
    def __init__(self, maxchar, player):
        self.maxChars = maxchar
        self.player = player
    def OutputInventory(self):
        FinalOutput = "\n" + self.ReturnHeader()
        FinalOutput += self.ReturnWeapons(self.player.weaponList)
        FinalOutput += self.ReturnSeperator()
        FinalOutput += self.ReturnArmour(self.player.armourList)
        FinalOutput += ("-" * self.maxChars) + "\n"
        print(FinalOutput)
    def ReturnSeperator(self):
        ## Border
        HeaderBorder = list("-" * self.maxChars)
        ## Join to map
        HeaderGap = "|" + (" " * (self.maxChars - 2)) + "|"
        Header = ("".join(HeaderBorder))
        Header += "\n"
        Header += HeaderGap
        return Header
    def ReturnWeapons(self, weaponList):
        HeaderText = "Weapons"
        Weapons = "\n| " + HeaderText + (" " * (self.maxChars - len(HeaderText) - 4)) + " |"
        Weapons += "\n| " + ("-" * len(HeaderText)) + (" " * (self.maxChars - len(HeaderText) - 4)) + " |"
        # Iterate through weapons
        Counter = 0
        MaxItems = len(weaponList)
        ItemLineStart = "\n| "
        ItemLineEnd = " |"
        ItemLineChars = 4
        NewLine = ItemLineStart
        while Counter < MaxItems:
            # get base
            ItemName = weaponList[Counter].name
            ItemAttack = weaponList[Counter].attack
            # generate line - WORKS
            ItemLine = "{0} (+{1} attack".format(ItemName, ItemAttack)
            # check if equipped
            if weaponList[Counter] == self.player.weapon:
                ItemLine += " - equipped)"
            else:
                ItemLine += ")"
            # If new line length would not be over the limit and this is not the last iteration
            if ((len(NewLine) + len(ItemLine)) < (self.maxChars -2)) & (Counter != (MaxItems -1)):
                NewLine += ItemLine
            # Otherwise we are either over the size limit of on the last iteration
            else:
                NewLine += ItemLine
                # generate final line
                FinalLine = NewLine + (" " * (self.maxChars - len(NewLine) -1)) + " |\n" 
                # append to result
                Weapons += FinalLine
                # then reset for more items
                NewLine = ItemLineStart
            # Increment counter
            Counter += 1
        return Weapons
    def ReturnArmour(self, armourList):
        HeaderText = "Armours"
        Armours = "\n| " + HeaderText + (" " * (self.maxChars - len(HeaderText) - 4)) + " |"
        Armours += "\n| " + ("-" * len(HeaderText)) + (" " * (self.maxChars - len(HeaderText) - 4)) + " |"
        # Iterate through weapons
        Counter = 0
        MaxItems = len(armourList)
        ItemLineStart = "\n| "
        ItemLineEnd = " |"
        ItemLineChars = 4
        NewLine = ItemLineStart
        while Counter < MaxItems:
            # get base
            ItemName = armourList[Counter].name
            ItemDefence = armourList[Counter].armour
            # generate line - WORKS
            ItemLine = "{0} (+{1} defence".format(ItemName, ItemDefence)
            # check if equipped
            if armourList[Counter] == self.player.armour:
                ItemLine += " - equipped)"
            else:
                ItemLine += ")"
            # If new line length would not be over the limit and this is not the last iteration
            if ((len(NewLine) + len(ItemLine)) < (self.maxChars -2)) & (Counter != (MaxItems -1)):
                NewLine += ItemLine
            # Otherwise we are either over the size limit of on the last iteration
            else:
                NewLine += ItemLine
                # generate final line
                FinalLine = NewLine + (" " * (self.maxChars - len(NewLine) -1)) + " |\n" 
                # append to result
                Armours += FinalLine
                # then reset for more items
                NewLine = ItemLineStart
            # Increment counter
            Counter += 1
        return Armours
    def ReturnHeader(self):
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
        return Header
    #OUTPUT A TABLE WITH STATS SHOWN - USE SAME SORT OF LOGIC AS SHOWMAP
