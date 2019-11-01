# Butterchase

Butterchase is a simply text based game created in Python. The premise is simple:

- Hero enters dungeon
- Hero progresses through dungeon to end and/or dies

Just a fun little project I decided to do to keep my Python skills fresh.

I used the game here as a base: https://trinket.io/python/07c3a147aa so big shoutout to that person (was unable to find them on github) for getting me started!

## Setup Checklist
- [ ] clone repo

## Usage
The game just uses basic print commands and some default Python modules.

Usage is as simple as:

- Clone repo
```cmd
git clone https://github.com/Sudoblark/Butterchase.git

```
- Run game.py
```cmd
c:\Users\Administrator\Documents\GitHub\Butterchase>py Butterchase\Game.py
What is your character's name? Steve
type help to get a list of actions

Steve foolishly enters a dark cave, seeking adventure...
> help
dict_keys(['quit', 'help', 'status', 'rest', 'explore', 'flee', 'attack'])
> explore
Steve wanders
> explore
Steve wanders
> explore
Steve encounters Steve the test goblin!
> attack
Steve hurts Steve the test goblin!
Steve executes Steve the test goblin!
Steve feels stronger!
> status
Steve's health: 11/11
Is Steve tired: False
> flee
Steve runs around hopelessly in circles for a while.
Steve feels tired.
> quit
Steve has died of dysentery.
```

## Mechanics
- If the player is tired then they do half damage

## Tests
- Executing Butterchase\EnemyClasses\ClassSheets\Util.py will test the ReturnName function on all ClassSheets. For example:

```cmd
c:\Users\Administrator\Documents\GitHub\Butterchase>py Butterchase\EnemyClasses\ClassSheets\Util.py

Goatman random name 01:  Pebbles
Goatman random name 02:  Squiggles
Goatman random name 03:  Trixie


Goblin random name 01:  Darren
Goblin random name 02:  Reggie
Goblin random name 03:  Lee


Ogre random name 01:  Gunk
Ogre random name 02:  Slurg
Ogre random name 03:  Poob


Orc random name 01:  Bin The double dipper
Orc random name 02:  Plug Of holed socks
Orc random name 03:  Doorknob Of holed socks


Skeleton random name 01:  Meristophiles Beaumont
Skeleton random name 02:  Reginald Strudabaker
Skeleton random name 03:  Hugo Montgomery


Troll random name 01:  Ivar Fletpek
Troll random name 02:  Siggi Bjonderplerg
Troll random name 03:  Ivar Angledik


c:\Users\Administrator\Documents\GitHub\Butterchase>
```

## Dev Notes
- Ensure all levels endsteps are equal numbers

## Acknowledgements
- Robert Charles Levett-Millett for lending his creative writting to character names and level descriptions


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
