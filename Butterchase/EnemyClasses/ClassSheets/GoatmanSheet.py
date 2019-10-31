from random import randint

# Name schema: Cute Pet Names
FirstNames = [
    "Squiggles","Fluffy","Sparkles","Rover","Skip","Dots","Mittens","Trixie","Bubbles",
    "Giggles","Floof"
    ]

LastNames = [

]

def ReturnName():
    return FirstNames[randint(0,len(FirstNames)-1)]

def ReturnStats():
    pass
    
