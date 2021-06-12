# Mermaid Diagram in Markdown Document
- [Mermaid Diagram in Markdown Document](#mermaid-diagram-in-markdown-document)
  - [Links](#links)
  - [Cardinality](#cardinality)
  - [Class Diagram](#class-diagram)
  - [Graph Diagram](#graph-diagram)
    - [Font Awesome Icons](#font-awesome-icons)
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
```html
<style>
    .cssClass > rect{
        fill:#68cdfc;
        stroke:#000000;
        stroke-width:4px;
    }
</style>
```
```mermaid
classDiagram
class Card:::rect {
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
Deck "1" o-- "*" Card
Dealer o-- Deck
Student "1" --> "1..*" Course
```
## Graph Diagram
* Font Awesome icons
[fa website](https://fontawesome.com/v4.7/examples/)
[gitHub](https://github.com/FortAwesome/Font-Awesome.git)

### Font Awesome Icons
```mermaid
graph TB
A[fa:fa-twitter]
B[fa:fa-home]
C[fa:fa-camera]
D[fa:fa-book]
E[fa:fa-pencil]
F[fa:fa-cog]
G[fa:fa-check-square]
H[fa:fa-square]
I[fa:fa-spinner]
J[fa:fa-envelope]
K[fa:fa-terminal]
L["fa:fa-ban"]
M["fa:fa-trash"]
N["fa:fa-shopping-cart"]
O["fa:fa-copyright"]
P["fa:fa-cut"]

A-->B-->C-->D-->I
E-->F-->G-->H-->K
F-->L-->J-->M
N-->O-->P
```

* graph (Left-Right)
```mermaid
graph LR;
    classDef rect1 fill:#f9f,stroke:#333,stroke-width:4px;
    classDef rect2 fill:#68cdfc,stroke:#333,stroke-width:2px;
    A[fa:fa-twitter student]==> B>store] & C(teacher) & D[(fa:fa-ban parent)];
    B--> A & E[/school/];
    C--fa:fa-twitter--> A & E;
    D--fa:fa-address-book --> A & E;
    E--> B & C & D;
    F["fa:fa-address-book addressbook "]
    class A,C,D rect1
    class B,E rect2
```
* Flowchart (Top-Bottom)
```mermaid
graph TB
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    style C fill:#f3ac30,stroke:#333,stroke-width:3px
    B --> G[/Another/]
    C ==>|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F["fa:fa-car Car"]
    style D fill:#4adff6,stroke:#333,stroke-width:2px
    style E fill:#4adff6,stroke:#333,stroke-width:2px
    style F fill:#4adff6,stroke:#333,stroke-width:2px

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
  style SubGraph1Flow fill:#f3ac30,stroke:#333,stroke-width:3px
  style DoChoice1 fill:#4abff6,stroke:#333,stroke-width:3px
  style DoChoice2 fill:#4abff6,stroke:#333,stroke-width:3px

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
.
```mermaid
erDiagram
    Customer }|--|{ Address:has
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
branch dev
checkout dev
commit
commit
checkout master
commit
merge dev
```