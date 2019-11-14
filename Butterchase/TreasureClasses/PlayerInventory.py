from PlayerClasses import Player

class PlayerInventory():
    def __init__(self, maxchar, player):
        self.maxChars = maxchar
        self.player = player

    def PlayerInteraction(self):
        # Method to interact with player
        self.OutputInventory()
        self.promptInput()
        self.readInput()

    def promptInput(self):
        print("Enter equip to equip an item, and exit to leave your inventory")
        print("Note: You cannot have more than one armour/weapon piece equipped at a time.")
        print("")

    def readInput(self):
        line = input("Inventory > ")
        inputFound = False
        if line == "exit":
            inputFound = True
            print("Leaving inventory system...")
        elif line == "equip":
            # If we equipped an item then exit inventory
            inputFound = True
            self.equip()     
        if not inputFound:
            print ("%s stares as his inventory dumbfounded (try another command)." % self.player.name)
            return False 

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
            if weaponList[Counter].currentEquipped == True:
                ItemLine += " - equipped) "
            else:
                ItemLine += ") "
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

    def equip(self):
        print("Please enter the item you wish to equip")
        line = input("Inventory > Equip > ")
        # first check weapons
        ItemFound = False
        for i in self.player.weaponList:
            # if item is a match
            if i.name == line:
                ItemFound = True
                # check if already equipped
                if i.currentEquipped == True:
                    msg = "{0} looks down, he's already holding {1} in his hands".format(self.player.name, i.name)
                    print(msg)
                # if player already has a weapon equipped
                elif self.player.weapon != None:
                    previousWeapon = self.player.weapon.name
                    # equip current weapon
                    self.player.weapon.unequip()
                    # equip new weapon
                    i.player = self.player
                    i.equip()
                    self.player.weapon = i
                    msg = "{0} swaps {1} for {2}".format(self.player.name, previousWeapon, i.name)
                    print(msg)
                    return True
                else:
                    i.equip()
                    self.player.weapon = i
                    msg = "{0} equips {1}".format(self.player.name, i.name)
                    print(msg)
                    return True
        # then check armour
        for i in self.player.armourList:
            # if item is a match
            if i.name == line:
                ItemFound = True
                # check if already equipped
                if i.currentEquipped == True:
                    msg = "{0} is already wearing the fashionable {1}".format(self.player.name, i.name)
                    print(msg)
                # if player already has a weapon equipped
                elif self.player.armour != None:
                    previousArmour = self.player.armour.name
                    # equip current weapon
                    self.player.armour.unequip()
                    # equip new weapon
                    i.equip()
                    self.player.armour = i
                    msg = "{0} swaps {1} for {2}".format(self.player.name, previousArmour, i.name)
                    print(msg)
                    return True
                else:
                    i.equip()
                    self.player.armour = i
                    msg = "{0} equips {1}".format(self.player.name, i.name)
                    print(msg)
                    return True
        # Return false is unable to equip an item
        # Also output an error
        if ItemFound == False:
            msg = "{0} can't find {1} in his inventory".format(self.player.name, line)
            print(msg)
        return False
