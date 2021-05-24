# Mermaid Diagram in Markdown Document
- [Mermaid Diagram in Markdown Document](#mermaid-diagram-in-markdown-document)
  - [Links](#links)
  - [Cardinality](#cardinality)
  - [Class Diagram](#class-diagram)
  - [Graph Diagram](#graph-diagram)
  - [Entity Relational Diagram](#entity-relational-diagram)
  - [Sequence Diagram](#sequence-diagram)
  - [State Diagram](#state-diagram)
  - [Project management diagram](#project-management-diagram)
  - [Pie chart](#pie-chart)
  - [Git Flow](#git-flow)

## Links
<|-- - Inheritance

*-- - Composition

o-- - Aggregation

--> - Association

-- - Link (Solid)

..> - Dependency

..|> - Realization

.. - Link (Dashed)

## Cardinality
0..1 - Zero or one

0..n - Zero to n (where n > 1)

0..* - Zero or more

1 - Only one

1..n - One to n (where n > 1)

1..* - One or more

* - Many

n..n - {where n>1}


## Class Diagram
```mermaid
classDiagram
class Card{
    face:str
    suit:str
}
class Deck{
    cards: Card[]
    shuffle()
    getCard()
}
class Player{
    name:str
    hand: Card[]
    hit()
    getValue()
}
Player <|-- Dealer:Dealer is a player
Deck o-- Card
Dealer o-- Deck
```
## Graph Diagram
* graph (Left-Right)
    ```mermaid
    graph LR;
    A--> B & C & D;
    B--> A & E;
    C--> A & E;
    D--> A & E;
    E--> B & C & D;
    ```
* Flowchart (Top-Bottom)
```mermaid
graph TB
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    B --> G[/Another/]
    C ==>|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]

    subgraph section
        C
        D
        E
        F
        G
    end
```

```mermaid
graph TB

  SubGraph1 --> SubGraph1Flow
  subgraph "SubGraph 1 Flow"
  SubGraph1Flow{SubNode 1}
  SubGraph1Flow -- Choice1 --> DoChoice1
  SubGraph1Flow -- Choice2 --> DoChoice2
  end

  subgraph "Main Graph"
  Node1[Node 1] --> Node2[Node 2]
  Node2 --> SubGraph1[Jump to SubGraph1]
  SubGraph1 --> FinalThing[Final Thing]
  end
```
## Entity Relational Diagram
```mermaid
  erDiagram

    CUSTOMER }|..|{ DELIVERY-ADDRESS : has
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ INVOICE : "liable for"
    DELIVERY-ADDRESS ||--o{ ORDER : receives
    INVOICE ||--|{ ORDER : covers
    ORDER ||--|{ ORDER-ITEM : includes
    PRODUCT-CATEGORY ||--|{ PRODUCT : contains
    PRODUCT ||--o{ ORDER-ITEM : "ordered in"
```
## Sequence Diagram
```mermaid
sequenceDiagram

    participant Client
    participant Server
    participant Database

    activate Client
    Client ->> +Server: HTTP Request
    Server ->> +Database: SQL Query
    Database -->> -Server: Result
    Server -->> -Client: HTTP Response
    deactivate Client
```
## State Diagram
```mermaid
stateDiagram-v2

        [*] --> Active

        state Active {
            [*] --> NumLockOff
            NumLockOff --> NumLockOn : EvNumLockPressed
            NumLockOn --> NumLockOff : EvNumLockPressed
            --
            [*] --> CapsLockOff
            CapsLockOff --> CapsLockOn : EvCapsLockPressed
            CapsLockOn --> CapsLockOff : EvCapsLockPressed
        }

        state SomethingElse {
          A --> B
          B --> A
        }

        Active --> SomethingElse2
        note right of SomethingElse2 : This is the note to the right.

        SomethingElse2 --> [*]
```

## Project management diagram
  * gantt
```mermaid
gantt
 title Example Gantt diagram
    dateFormat  YYYY-MM-DD
    section Team 1
    Research & requirements :done, a1, 2020-03-08, 2020-04-10
    Review & documentation : after a1, 20d
    section Team 2
    Implementation      :crit, active, 2020-03-25  , 20d
    Testing      :crit, 20d
```

## Pie chart
```mermaid
pie
"Dogs":386
"Cats":85
"Rats":15
```

## Git Flow
```mermaid
gitGraph:
options
{
    "nodeSpacing": 150,
    "nodeRadius": 10
}
end
commit
branch newbranch
checkout newbranch
commit
commit
checkout master
commit
commit
merge newbranch
```