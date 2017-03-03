# Tournament Scheduling
[![Build Status](https://travis-ci.org/guemues/german-game-tournament.svg?branch=master)](https://travis-ci.org/guemues/german-game-tournament) [![Coverage Status](https://coveralls.io/repos/github/guemues/german-game-tournament/badge.svg?branch=master)](https://coveralls.io/github/guemues/german-game-tournament?branch=master)

This repository created for a tournament scheduling problem.

The purpose is prevent placing same players more than once in the same group.

You can schedule your tournament in only one way with this repo. More scheduling types including round-robin may or may not added.

The algorithm works like this for 16 person tournement:
```
[0, 1, 2 ... 15]
```
For 4 player catan tournement

First Cycle: 
```
[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
```
Second Cycle: 
```
[0, 4, 8, 12]
[1, 5, 9, 13]
[2, 6, 10, 14]
[3, 7, 11, 15]
```

*Support for game_per_player (game count for players) other then 2 is not tested.
With this algorithm you need k * power(player count in one game, game count for one player) player. k must be integer bigger than 0.*


### Installing

```
pip install germantournament
```

### Usage

Example

```
from germantournament.GameTournament import GermanGameTournament
tournament = GermanGameTournament()
tournament.set_player_count(16)
scheduled_events = tournament.schedule(player_count_in_one_game=4)
print(scheduled_events)
```
```
>>>[[0, 4, 8, 12], [3, 7, 11, 15], [1, 5, 9, 13], [2, 6, 10, 14], [4, 5, 6, 7], [0, 1, 2, 3], [12, 13, 14, 15], [8, 9, 10, 11]]
```