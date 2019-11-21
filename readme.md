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
- Chars can dodge
- Randomly generated levels with enemies/traps/loot

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

### ToDo

#### General
- [ ] Create a step array containing the level layout, e.g.:

[1,0,0,2,0,0,0,0,0]
[0,0,2,0,]
[0,0,0,0,0,0,0,0,0,1]

-1 = impassable
0 = blank
1 = exit
2 = Goatman
3 = Goblin
4 = Orc
5 = Skeleton
6 = Ogre
7 = Troll
8 = Trap
9 = Treasure
10 = Visible trap

- [ ] Add random map generation with options above
- [x] Add goUp and goDown options on levels to allow 2D navigation
- [x] Also add goUp and goDown as recognise commands
- [x] Add checker to base level that determines if player is on a tile with an enemy
- [x] If on tile with enemy then randomly generate one with the appropriate type


#### Error handling
- [ ] Limit len of name so menu doesn't break

#### Levels
- [ ] Add logic for if player moves to exit
- [ ] Add in some way to have different NAT1 possibilities depending on the level
- [ ] Add more dice rolls to allow bad and good things to happen more option


#### Traps
- [ ] Add checker to base level that determines if player is on tile with trap
- [ ] Each level to contain trap method that has a list of traps and dice rolls to determine if player is "hit" by said trap
- [ ] New trap base class with different types deviating from this to allow maximum future-proofing
- [ ] Traps to have "visible" property, if visible then play can see. E.G. a great big hole in the group is pretty obvious
- [x] Set traps to be visible once discovered


#### Inventory System
- [x] Add evade mechanic
- [x] Add base/adjusted attack to all characters
- [ ] Create weapons and armour for each enemy class
- [x] Have enemies equip random weapons and armour on spawn
- [x] Create player weapons and armour
- [x] Add weapons and armour to chests
- [x] Each level to have list of possible treasure and dice rolls to determine what player recieved. If on a treasure tile the player always gets an item from a randomly generated list appropriate for the level 
- [x] Use weapon and armour flavour text where appropriate
- [x] 1 in 100 chance for treasure to be cursed and spawn a new enemy type of demon
- [ ] Steal weapon from enemy
- [x] Allow equip of items

#### Companion System
- [ ] Add mechanics for followers
- [ ] Add charm option to try and convince an enemy to become your follower
- [ ] Other followers are spawned during random events

#### Shop system
- [ ] Add a cute dog that you can buy things from

#### Random events
- [ ] When exiting a level have random events that may happen, requiring player input, before moving on to next level

## Acknowledgements
- Robert Charles Levett-Millett for lending his creative writting to character names and level descriptions


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
