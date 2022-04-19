<h1> Visual Studio Code Tricks</h1>

[](myIcons.md)

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Virtual Environment](#virtual-environment)
- [Install PIL](#install-pil)
- [Disable Editor minimap](#disable-editor-minimap)
- [Define Key-shortcut for clear terminal](#define-key-shortcut-for-clear-terminal)
- [Move Terminal window to right](#move-terminal-window-to-right)
- [Key shortcut](#key-shortcut)
- [Command Palette](#command-palette)
- [Convert Markdown to PDF](#convert-markdown-to-pdf)
- [Disable pylint check](#disable-pylint-check)
- [Setup Unit test](#setup-unit-test)
- [Setup Python Interpretor](#setup-python-interpretor)
- [Create Virtual Environment](#create-virtual-environment)
- [Check in GitHub](#check-in-github)
- [Increase/decrease window characters](#increasedecrease-window-characters)

## Virtual Environment

```
python -m venv env
1. Command Palette... ➡️ Select Interpreter ➡️ Find ➡️ env/Script/python.exe
2. close terminal, reopen it
```
👎😢 there is no indicator on bottom bar; there is no (env) in front of command prompt❗️
👍😄 close the VS code, reopen it.

## Install PIL
```dos
pip install pillow
```

## Disable Editor minimap

😄Gear(bottom-left) ⟹ settings ⟹ Text Editor: minimap: Enable ⟹ uncheck
 
## Define Key-shortcut for clear terminal
Right-click ⟹ Command palettes ⟹ Terminal: clear ⟹ click the gear ⟹ click +

👍Shift+ctrl+c

## Move Terminal window to right

👍Right-click Terminal tab ⟹ Move panel right

## Key shortcut
* Copy/Paste one line: Shift+Alt+Arrow
* Copy/Paste multiple lines: highlight ⟹ Shift+Alt+Arrow
* Delete one line: Ctrl+Shift+k
* Replace String: highlight + Ctrl+Shift+l
* Change File Name: F2
* Pick different open file: Ctrl+tab
* jump word: ctrl+arrow
* move window to right: window+arrow

## Command Palette
* 🔥Command Palette...(CP):Ctrl+Shift+p
* Python Interpreter: CP ⟹ Python: Select Interpretor
* Unit test: CP ⟹ Configure Test
* Table of Contents: CP ⟹ Markdown All in one: Table of contents
* Code Snippet: CP ⟹ Configure user snippet
* Search Snippet: Ctrl+Space
* setting: "editor.tabCompletion": "on"
* Zen mode: Command Palette ⟹ view toggle Zen mode
* [Python Snippet](/Users/12818/AppData/Roaming/Code/User/snippets/python.json)
* [create user snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

## Convert Markdown to PDF
* Extension: Markdown Preview Enhanced
* Right-click ⟹ Chrome (Puppeteer) ⟹ PDF

## Disable pylint check
Just hit Ctrl+Shift+P ⟹ Select linter ⟹ Disabled Linter

the result will be written in ./.vscode/settings.json as below
```json
    "python.linting.enabled": false,
```
---

## Setup Unit test
* Right-click ⟹ Command Palette... 
* Python: Configure Tests
* unittest Standard Python test framework
* . Root Directory
* test_*.py
* Click flask icon on tool left bar

the result will be written in ./.vscode/settings.json as below
```json
{
    "python.linting.enabled": false,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.unittestEnabled": true
}
```

👎😢❌Python unittest uses root folder to find test code, but if you import one module1 from another module2, unittest would **NOT** be able to find the module2, you need to use absolute file path, or relative file path showing below👇

```py
from .card import Card # use this line for unit test
# from card import Card # use this line for product

class BlackjackCard(Card):
    def getValue(self):
        switch = {"A":11,"J":10,"Q":10,"K":10}
        if self.face.isdigit():
            return int(self.face)
        return switch.get(self.face)
```
❌❗️📌⚡️Unfortunatly, this make unittest work, but python code no longer works.
```output
Traceback (most recent call last):
  File "c:\Users\12818\workspace\python-I\src\blackjack\blackjackcard.py", line 1, in <module>ne 1, in <module>
    from .card import Card # use this line for unit test
😢ImportError: attempted relative import with no known parent package
```

```output
<project root>
    ├── 🔥src/
    └── blackjack/
          ├── card.py 
          └── blackjackcard.py (import card) 
```

```<project root>
👌python -m src.blackjack.card
👌python -m src.blackjack.blackjackcard
❌❗️python ./src/blackjack/blackjackcard.py
```
❌❗️Directly run blackjackcard.py from root project folder cause the following error:
```output
(env) C:\Users\12818\workspace\python-I>python ./src/blackjack/blackjackcard.py
Traceback (most recent call last):
  File "C:\Users\12818\workspace\python-I\src\blackjack\blackjackcard.py", line 1, in <module>
    from .card import Card # use this line for unit test
ImportError: attempted relative import with no known parent package
```
---

## Setup Python Interpretor
* Right-click > Command Palette... 
* Python: Select Interpreter
* Enter Interpreter path
* Browse File foldre for 
```
C:\Users\12818\workspace\python-I\env\Scripts\python.exe
```

the result will be written in ./.vscode/settings.json as below
```json
    "python.pythonPath": "c:\\Users\\12818\\workspace\\python-I\\env\\Scripts\\python.exe",
```
---

## Create Virtual Environment
* Terminal > New Terminal
* type in command in the open terminal
```
python -m venv env
```
---

## Check in GitHub
* Cannot check in due to configure user.namd and user.email
```
git config user.name "jwang1122"
git config user.email "jwang1122@gmail.com"
```
* add collaborator in the repository
[GitHub repository](https://github.com/jwang1122/python1)

> Settings > Options: Manage access > regular password > button: Invite a collaborator

Ask collaborator open email > Review Invitation > Accept Invitation

* Cannot push
    pull first.
```
git pull
```

## Increase/decrease window characters

```
ctrl +/-
```
---


