## Language Basics

```mermaid
graph TB

PROG(Program Language)
TYPE["Data Type<br>(int,str,float)"]
OP[Operator<br>=,>=,is]
EXEC[Execution Contonl<br>if, if-else]
LOOP[Loop<br>for, while]

PROG-->TYPE & OP & EXEC & LOOP

classDef start fill:green,stroke:#0c3f10,stroke-width:2px,color:white;
classDef process fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;

class PROG start
class TYPE,OP,EXEC,LOOP process
```

## Python program

```mermaid
graph TB

START([Python Program])
A[Python Code]
C[Python function]
D[Python class]
E[Attributes]
F[Functions]

START-->A & C & D
D-->E & F

classDef html fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef js fill:yellow,stroke:#DE9E1F,stroke-width:2px;
classDef start fill:#53DE1F,stroke:#267608,stroke-width:2px;

class START start
class A,C,D html
```

## Monad


```mermaid
classDiagram

class Box{
  value:any
}
class Functor{
  value:any
  fmap(function)
}
class Applicative{
  amap(functorValue)
}
class Monad{
  bind(function)
  __rshift__(function)
}
Container<|--Functor:is box
Functor<|--Applicative: is Functor
Applicative<|--Monad: is Applicative
Monad<|--Maybe
Maybe<|--Just:is monad
Maybe<|--Nothing: is monad

<<abstract>> Maybe

```

```mermaid
classDiagram

class ClassName{
  attributes
  functions()
}
```



```mermaid
classDiagram
class Robot {
  name:str
  year:int
  energy:int
  sayHello(name):void
  doMath(x,y):tuple
  getEnergy():int
  setEnergy(int):void
}
```

```mermaid
classDiagram

class Item{
  name:str
  price:float
  quantity:int
  getTotal()
  addDiscount()
}

class Store{
  items:[]
  save()
  load()
}
```

```mermaid
classDiagram

class Student{
  name:str
  age:int
  grade:int
  courses:Course[]
}

class Course{
  name:str
  students:Student[]
}

Course o-- Student:bidirection_connection
Student o-- Course
```

```mermaid
classDiagram

class Pet{
  name:str
  age:int
  speak()
}

Pet <|-- Dog
Pet <|-- Cat
Pet <|-- Fish
```

```mermaid
classDiagram

class Point{
  x
  y
  rotate()
}

class Triangle{
  p1:Point
  p2:Point
  p3:Point
  rotate()
  draw()
}

Triangle *-- Point
```


```mermaid
classDiagram

class Animal{
  name:string
  eat()
}

class Mammal{
  walk()
}

class Bird{
  fly()
}

class Bat{
  name:string
  walk()
  fly()
}
Mammal <|-- Bat
Bird <|-- Bat
Animal <|-- Mammal
Mammal <|-- Bird
```

```mermaid
classDiagram
class Person {
  name:str
  ssn:str
  id: str
  gender:str
  age:int
  getOccupation()
}

class Employee{
  employeeID: str
  department: str
  salary:float
  jobTitle:str
}

class Engineer{
  report()
  getOccupation()
}

class Manager{
  assignJob()
}

class Teacher{
  getOccupation()
}

Person<|--Employee:is
Employee<|--Engineer:is
Employee<|--Manager:is
Person<|--Teacher:is
```

```mermaid
classDiagram

class Person {
  getOccupation():str
}

<<interface>> Person

class Teacher {
  name: str
  getOccupation()
}

class Engineer {
  name: str
  getOccupation()
}

class Student{
  name: str
  getOccupation()
}

Person<|--Teacher:Teach is Person
Person<|--Engineer:Engineer is Person
```

```mermaid
classDiagram

class Quantity{
  vale:[float, int]
  symble: str

  covert(symble)
}
```

```mermaid
classDiagram
class Card {
  face:str
  suit:str
  getValue()
}

class BlackjackCard{
  getValue()
}

class Deck{
  topCardIndex:int
  stackOfCards:BlackjackCard
  shuffle()
  getCard()
  nextCard()
}

class Player{
  name:str
  hand:[]
  win:int
  addCardToHand()
  cleanHand()
  getHandValue()
  getHandSize()
  hit()
  showHand()
}

class Dealer {
  deck:Deck
  shuffle()
  deal()
  hit()
  showHand()
}

class Game{
  playerList:ArrayList<Player>
  dealer:Dealer
  determineWinner()
  play(winner:function)
}

Player<|--Dealer:dealer is player
Dealer *--Deck:dealer own the deck
Card<|--BlackjackCard
Deck o--BlackjackCard:stack of Cards
Game *-- Dealer
Game *-- Player
```

```mermaid
graph TB
A([start])
INIT["init()"]
B[Deal cards]
C[Show hands]
D{hit?}
F[determine winner<br>show result]
END[end]
AGAIN{more game?}
S[Shuffule, clean hand]

A-->INIT-->B-->C-->D
D--true-->B
D--false-->F-->AGAIN
AGAIN--false-->END
AGAIN--true-->S-->B

classDef start fill:green,stroke:#DE9E1F,stroke-width:2px,color:white;
classDef end1 fill:red,stroke:#DE9E1F,stroke-width:2px,color:white;
classDef if fill:#EBCD6F,stroke:black,stroke-width:2px;

class A start
class END end1
class D,AGAIN if
```

```mermaid
graph TB
START([start])
PLAYER[player win]
DEALER[dealer win]
TIED[tied]

A{player>21}
C{dealer>21}
D{player==dealer}
E{player>dealer}

START-->A
A--false-->C
A--true-->DEALER
C--true-->PLAYER
C--false-->
D--true-->TIED
D--false-->E
E--true-->PLAYER
E--false-->DEALER

classDef if fill:#EBCD6F,stroke:black,stroke-width:2px;

class A,D,C,E if
```

```mermaid
graph TB
START([start])
C[Create Base class]
UT[unit test]
F[fix code pass test]
DONE{Done all classes}
INT[integration test]
ERROR{error or <br>improvement?}
FIX[fix issue, make better]
PROD([production])

START-->C-->UT-->F-->DONE
DONE--true-->INT-->ERROR
DONE--false, dev cycle-->C
ERROR--true-->FIX--integration cycle-->UT
ERROR--false-->PROD

classDef if fill:#EBCD6F,stroke:black,stroke-width:2px;
classDef start fill:green,stroke:#DE9E1F,stroke-width:2px,color:white;

class ERROR,DONE if
class START,PROD start
```

```mermaid
graph TB

START([start])
A{player>21}
DEALER[dealer win]
B{dealer>21}
PLAYER[player win]
C{player==dealer}
TIED[tied up]
D{player>dealer}

START-->A--true-->DEALER
A--false-->B
B--false-->C
B--true-->PLAYER
C--true-->TIED
C--false-->D
D--false-->DEALER
D--true-->PLAYER

classDef if fill:#EBCD6F,stroke:black,stroke-width:2px;
classDef db fill:#BEBDB7,stroke:black,stroke-width:2px;
classDef start fill:green,stroke:#DE9E1F,stroke-width:2px,color:white;

class START start
class A,B,C,D if
```

```mermaid
classDiagram
class Dices{
  numberOfDices:int
  roll()
}
class Player{
  name:str
  score:int
  dices:Dices
  record:[]
  roll()
  keep()
}
class Game{
  round:int
  playerList:[]

  addPlayer()
  play()
}
```

```mermaid

classDiagram

class T{
  field:str
}

class S{
  field:str
}

T<|--S
```

```mermaid
graph LR

OOP([Object Oriented Programming])
ABSTRACT[Abstraction]
INHERIT[Inheritance]
POLY[Polymorphism]
ENCAPS[Encapsulation]

OOP --> ABSTRACT & INHERIT & POLY & ENCAPS

classDef start fill:green,stroke:#DE9E1F,stroke-width:2px,color:white;

class OOP start
```


```mermaid
erDiagram
  PROJECT{
    int id
    string name
  }
  TASK{
    int id
    string name
    date start
    date end
  }
  PROJECT ||--o{ TASK : contains

```

```mermaid
erDiagram
  blackjack {
      int id
      string name
      int win
      int loose
      int tie
  }
```

