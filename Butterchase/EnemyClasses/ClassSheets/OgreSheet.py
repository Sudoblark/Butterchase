from random import randint

# Name schema: Dumb sounding cavemen
FirstNames = [
    "Gunk","Dong","Slurg","Bleb","Henk","Poob","Weng","Ag","Bu","Thod"
    ]

LastNames = [
    ]

def ReturnName():
    return FirstNames[randint(0,len(FirstNames)-1)]

def ReturnStats():
    pass
    
    
