import base64
import requests, io
from PIL import Image
import matplotlib.pyplot as plt

# graph = """
# graph LR;
#     A--> B & C & D;
#     B--> A & E;
#     C--> A & E;
#     D--> A & E;
#     E--> B & C & D;
# """

graph = """
classDiagram
class Card{;
    face:str;
    suit:str;
}
class Deck{;
    cards: Card[];
    shuffle();
    getCard();
}
class Player{;
    name:str;
    hand: Card[];
    hit();
    getValue();
}
Player <|-- Dealer
Deck o-- Card
Dealer o-- Deck
"""
graphbytes = graph.encode("ascii")
base64_bytes = base64.b64encode(graphbytes)
base64_string = base64_bytes.decode("ascii")
img = Image.open(io.BytesIO(requests.get('https://mermaid.ink/img/' + base64_string).content))
plt.imshow(img)
plt.show()