# Pac-man Game

<img width="300" height="300" src='./figures/window.png' alt='Pac-man'/>

This is a Pac-man game coded in python, which provides ai using reinforcement learning and greedy methods.

The user opeartions api are also in the plan.

The game map consists of 25*23 grids.

## Table of Contents

* [Rule](#rule)
* [Target](#target)
  * [Pac-man](#pac-man)
  * [Ghosts](#ghosts)
* [Implementation](#implementation)   
  * [Methods For Shorest Path Query](#methods-for-shortest-path-query)
  * [Strategy For Pac-man & Ghost](#strategy-for-pac-man--ghost)
    * [Only One Ghost](#only-one-ghost)
    * [Two Ghost](#two-ghost)

## Rule

* The Pac-man Game has one Pac-man and some Ghosts. In this game we set two target for Pac-man, escaping or eating all dots.
* Whether the boundary can be crossed can be set in setting.py.

## Target

> The target can be set in settings.py.

#### Pac-man

<img width="80" height="80" src='./figures/Pacman_left.png' alt='Pac-man'/>

* Escape from Ghosts
* Eat all the beans (TODO)

#### Ghosts

<img width="80" height="80" src='./figures/red_left.png' alt='Ghost'/>
<img width="80" height="80" src='./figures/pink_left.png' alt='Ghost'/>
<img width="80" height="80" src='./figures/yellow_left.png' alt='Ghost'/>
<img width="80" height="80" src='./figures/blue_left.png' alt='Ghost'/>

* Catch Pac-man

## Implementation

### Methods For Shortest Path Query

The method for shortest path query can be set in settings.py.
* Breadth First Search
* Depth First Search
* Dijkstra (TODO)

### Strategy For Pac-man & Ghost

#### Only One Ghost

* Greedy: Take the action to shorten/lengthen the distance between Pac-man and Ghost.
* Reinforcement learning (TODO)

#### Two Ghost

* TODO