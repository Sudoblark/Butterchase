from random import randint

# Name schema: Classy
FirstNames = [
    "Ponsomby","Reginald","Horacio","Hortensia","Persephone","Baldrigar",
    "Cornelius","Meristophiles","Hugo"
    ]

LastNames = [
    "Beaumont","Plantagenate","Of Sussex","Strudabaker","Montgomery","Shrewsbury"

]

def ReturnName():
    return FirstNames[randint(0,len(FirstNames)-1)] + " " + LastNames[randint(0,len(LastNames)-1)]

def ReturnStats():
    pass
    
    
