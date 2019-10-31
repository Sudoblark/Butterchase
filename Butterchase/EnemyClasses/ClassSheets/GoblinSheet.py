from random import randint

# Name schema: Typical bloke names
FirstNames = [
    "Terry","Darren","Mick","Tracey","Lee","Garry","Barry","Dom","Reggie","Steve",
    "Big John","Clive","Gregg","Larry", "Noel"
    ]

LastNames = [
    "Punching","Tornado","Hilary","Dramatic", "Smith", "Clark",

]

def ReturnName():
    return FirstNames[randint(0,len(FirstNames)-1)]

def ReturnStats():
    pass
    
    
