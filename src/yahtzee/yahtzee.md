<h1>Yahtzee Game</h1>

[Yahtzee website](https://www.dicegamedepot.com/yahtzee-rules/)

## Object
The object of Yahtzee is for each player to roll dice and fill out their score card over the course of a series of rounds, trying to obtain the best rolls they can in 13 different combinations. The player with the highest score at the end of the game wins.

## Number of Players
2 or more

## How to PlayYahtzee
* Choose a starting player by player order
* player will take turns one at a time
* The game consists of thirteen rounds
* who has the greatest score wins.

```mermaid
graph TB
A(roll 5 dices)
B([loop for 2])
C{Try again?}
D[choose dices to keep<br>roll others]
E{Try Twice?}
F[score and end]

A-->B-->C
C--True-->D-->E
E--False-->B
E--True-->F
```
## class design
```mermaid
classDiagram

class Dice{
    number
    roll()
}
class Player{
    name:string
    roll()
    addScore()
    keep()
    getScore()
    addRecords()
}
class Game{
    playerList:list
    dices:Dice
    score()
}

Game *-- Player
Player *-- Dice
```

```mermaid
graph TB

A(Lower Section)
B{Yahtzee?}
C{Large Straight?}
D{Small Straight?}
E{Four kind?}
F{Full House?}
G{Three kind}
H[Others]

I[50 points]
J[40 points]
K[30 points]
L[25 points]
M[adds up]

A-->B
B--True-->I
B--False-->C
C--True-->J
C--False-->D
D--True-->K
D--False-->E
E--True-->M
E--False-->F
F--True-->L
F--False-->G
G--True-->M
G--False-->H
H-->M
```