from random import randint

# Name schema: Scandi sounding names
FirstNames = [
    "Flurg","Ivar","Borg","Gongar","Bjon","Luber","Astrid","Bonk","Siggi","Freya"
    ]

LastNames = [
    "Gongleson","Bjonderplerg","Angledik","Lemberdorg","Fletpek","Kornertabel"
    ]

def ReturnName():
    return FirstNames[randint(0,len(FirstNames)-1)] + " " + LastNames[randint(0,len(LastNames)-1)]

def ReturnStats():
    pass
    
    
