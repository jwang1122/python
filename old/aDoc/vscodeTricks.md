# VSCode Tricks

👍👎✔️❌❓💾🗑📝📓📒💡⚠️😄😢✉️♻️🔥☄️🛠⚡️📐🎯📄⏪📌

## Table of Contents
- [VSCode Tricks](#vscode-tricks)
  - [Table of Contents](#table-of-contents)
  - [😄Disable Editor minimap](#disable-editor-minimap)
  - [👍Define Key-shortcut for clear terminal](#define-key-shortcut-for-clear-terminal)
  - [👍Move Terminal window to right](#move-terminal-window-to-right)
  - [Key shortcut](#key-shortcut)
  - [🔥Command Palette](#command-palette)
  - [Convert Markdown to PDF](#convert-markdown-to-pdf)
  - [Disable pylint check](#disable-pylint-check)
  - [Setup Unit test](#setup-unit-test)
  - [👍 Setup Python Interpretor](#-setup-python-interpretor)
  - [Create Virtual Environment](#create-virtual-environment)
  - [Check in GitHub](#check-in-github)
  - [Increase/decrease window characters](#increasedecrease-window-characters)

## 😄Disable Editor minimap

Gear(bottom-left) > settings > Text Editor: minimap: Enable > uncheck
 
## 👍Define Key-shortcut for clear terminal
Right-click > Command palette > Terminal: clear > click the gear > click +

Shift+ctrl+c

## 👍Move Terminal window to right

Right-click Terminal tab > Move panel right

## Key shortcut
* Copy/Paste one line: Shift+Alt+Arrow
* Copy/Paste multiple lines: highlight > Shift+Alt+Arrow
* Delete one line: Ctrl+Shift+k
* Replace String: highlight + Ctrl+Shift+l
* Change Name: F2
* Pick different open file: Ctrl+tab
* jump word: ctrl+arrow
* move window to right: window+arrow

## 🔥Command Palette
* Command Palette...:Ctrl+Shift+p
* Python Interpreter: CP > Python: Select Interpretor
* Unit test: CP > Configure Test
* Table of Contents: CP > Markdown All in one: Table of contents
* Code Snippet: CP > Configure user snippet
* Search Snippet: Ctrl+Space
* setting: "editor.tabCompletion": "on"
* Command Palette > view toggle Zen mode
* [Python Snippet](/Users/12818/AppData/Roaming/Code/User/snippets/python.json)
* [create user snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

## Convert Markdown to PDF
* Extension: Markdown Preview Enhanced
* Right-click > Chrome (Puppeteer) > PDF

## Disable pylint check
Just hit Ctrl+Shift+P > Select linter > Disabled Linter

the result will be written in ./.vscode/settings.json as below
```json
    "python.linting.enabled": false,
```
---

## Setup Unit test
* Right-click > Command Palette... 
* Python: Configure Tests
* unittest Standard Python test framework
* . Root Directory
* test_*.py
* Click flask icon on tool left bar

the result will be written in ./.vscode/settings.json as below
```json
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        ".",
        "-p",
        "test_*.py"
    ],

```
---

## 👍 Setup Python Interpretor
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


