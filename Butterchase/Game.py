from PlayerClasses.Player import Player, Commands
from LevelClasses.Level_Test import Level_Test
from LevelClasses.Level_One import Level_One
p = Player()
# Ask for player's name
NameSet = False
CharLimit = 25
while NameSet == False:
  TempName = input("What is your character's name? ")
  if len(TempName) < CharLimit:
    p.name = TempName
    NameSet = True
  else:
    print("Please input a name less than {0} characters.".format(CharLimit))
    print()


print("type help to get a list of actions\n")
print("%s foolishly enters a dark cave, seeking adventure..." % p.name)
print("")
# If we are testing then load the test level
if p.name == "DevTest":
  p.level = Level_Test(p)
else:
  p.level = Level_One(p)
p.level.EntranceMessage()
print("")

while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print ("%s doesn't understand the suggestion." % p.name)
