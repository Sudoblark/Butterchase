from PlayerClasses.Player import Player, Commands
from LevelClasses.Level_Test import Level_Test
p = Player()
p.name = input("What is your character's name? ")
print("type help to get a list of actions\n")
print("%s foolishly enters a dark cave, seeking adventure..." % p.name)
print("")
# If we are testing then load the test level
if p.name == "DevTest":
  p.level = Level_Test(p)
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
