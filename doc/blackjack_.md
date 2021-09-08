<h1> Blackjack Game</h1>
  
[Black Jack Rules](https://bicyclecards.com/how-to-play/blackjack/ )
  
##  Blackjack Rules
  
1. Object of the game: 
>beat the dealer by getting a count as close to 21 as possible, without going over 21
2. Card Values 
>ace is worth 1 or 11, J,Q,K are 10, other card is its pip value
3. Betting
>for simplicity, we don't bet.
4. Shuffle and cut
>the dealer shuffles the pack of card, no need player cut
5. Deal
>dealer gives one card face up to each player, and one card face up for himself. Another round of cards is then dealt face up to each player, but the dealer takes the second card face down.
6. Naturals
>If a player's first two cards are an ace and a "ten-card" (a picture card or 10), giving a count of 21 in two cards, this is a natural or "blackjack." If any player has a natural and the dealer does not, the dealer lose.  If the dealer has a natural, other doesn't, dealer win. If both dealer and player have natural, no body wins.
7. The Play
>any player on his turn must decide whether to "stand" (not ask for another card) or "hit" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly). Thus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards, one at a time, until deciding to stand on the total (if it is 21 or under), or goes "bust" (if it is over 21). In the latter case, play loses the game. The dealer then turns to the next player and serves them in the same manner. The combination of an ace with a card other than a ten-card is known as a "soft hand," because the player can count the ace as a 1 or 11, and either draw cards or not. For example with a "soft 17" (an ace and a 6), the total is 7 or 17. While a count of 17 is a good hand, the player may wish to draw for a higher total. If the draw creates a bust hand by counting the ace as an 11, the player simply counts the ace as a 1 and continues playing by standing or "hitting" (asking the dealer for additional cards, one at a time).
8. The Dealer's Play
>When the dealer has served every player, the dealers face-down card is turned up. If the total is 17 or more, it must stand. If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.
9. No Splitting Pairs
10. No Doubing Down
11. No Insurance
12. Reshuffling when start new game.
  
##  Object relationship
  
  

```
Error: mermaid CLI is required to be installed.
Check https://github.com/mermaid-js/mermaid.cli for more information.

Error: Command failed: npx mmdc --theme default --input C:\Users\12818\AppData\Local\Temp\mume-mermaid202187-16752-19v780u.hs85.mmd --output C:\Users\12818\workspace\python-I\assets\10b7e0bab6ae76f4655ad93d7a3f15f20.png
npm ERR! code E404
npm ERR! 404 Not Found - GET https://registry.npmjs.org/mmdc - Not found
npm ERR! 404 
npm ERR! 404  'mmdc@latest' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it (or use the name yourself!)
npm ERR! 404 
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\12818\AppData\Roaming\npm-cache\_logs\2021-09-07T23_44_58_106Z-debug.log
Install for [ 'mmdc@latest' ] failed with code 1

```  

[blackjack](../src/blackjack.py )
[Unit test](../test/test_blackjack.py )
  
##  Game logic
  

```
Error: mermaid CLI is required to be installed.
Check https://github.com/mermaid-js/mermaid.cli for more information.

Error: Command failed: npx mmdc --theme default --input C:\Users\12818\AppData\Local\Temp\mume-mermaid202187-16752-1td0usq.wd2c.mmd --output C:\Users\12818\workspace\python-I\assets\10b7e0bab6ae76f4655ad93d7a3f15f21.png
npm ERR! code E404
npm ERR! 404 Not Found - GET https://registry.npmjs.org/mmdc - Not found
npm ERR! 404 
npm ERR! 404  'mmdc@latest' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it (or use the name yourself!)
npm ERR! 404 
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\12818\AppData\Roaming\npm-cache\_logs\2021-09-07T23_45_07_470Z-debug.log
Install for [ 'mmdc@latest' ] failed with code 1

```  

##  Code Optimization
  

```
Error: mermaid CLI is required to be installed.
Check https://github.com/mermaid-js/mermaid.cli for more information.

Error: Command failed: npx mmdc --theme default --input C:\Users\12818\AppData\Local\Temp\mume-mermaid202187-16752-1l3lxc7.5p0y.mmd --output C:\Users\12818\workspace\python-I\assets\10b7e0bab6ae76f4655ad93d7a3f15f22.png
npm ERR! code E404
npm ERR! 404 Not Found - GET https://registry.npmjs.org/mmdc - Not found
npm ERR! 404 
npm ERR! 404  'mmdc@latest' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it (or use the name yourself!)
npm ERR! 404 
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\12818\AppData\Roaming\npm-cache\_logs\2021-09-07T23_45_13_378Z-debug.log
Install for [ 'mmdc@latest' ] failed with code 1

```  

  
##  Unit test cases
  
* player get 4 Ace
* player get 3 Ace
* player get 2 Ace
  
  