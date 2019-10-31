from random import randint

# Name schema: Random nouns and negative adjectives
FirstNames = [
    "Table","Chair","Plug","Dinner","Club","Bin","Yoghurt","Roof","Chimney","Pot",
    "Doorknob","Lemon"

]

LastNames = [
    "The unkempt", "The bad at things", "Of holed socks","The ugly","The nugget thief",
    "The fraudulent","The double dipper","The weak","The unholy","Maker of stupid noises",
    "The fatulent","The boring","The toothless","The not actually an orc"
    ]

def ReturnName():
    return FirstNames[randint(0,len(FirstNames)-1)] + " " + LastNames[randint(0,len(LastNames)-1)]

def ReturnStats():
    pass
