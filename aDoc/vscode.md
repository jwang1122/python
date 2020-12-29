# VS Code tricks

## Table of Contents
- [VS Code tricks](#vs-code-tricks)
  - [Table of Contents](#table-of-contents)
  - [Disable pylint check](#disable-pylint-check)
  - [Setup Unit test](#setup-unit-test)
  - [Setup Python Interpretor](#setup-python-interpretor)
  - [Create Virtual Environment](#create-virtual-environment)
  - [Check in GitHub](#check-in-github)

## Disable pylint check
Just hit Ctrl+Shift+P > Select linter > Disabled Linter

the result will be written in ./.vscode/settings.json as below
```json
    "python.linting.enabled": false,
```
---
[Table of Contents](#Table-of-Contents)

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
[Table of Contents](#Table-of-Contents)

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
[Table of Contents](#Table-of-Contents)

## Create Virtual Environment
* Terminal > New Terminal
* type in command in the open terminal
```
python -m venv env
```
---
[Table of Contents](#Table-of-Contents)

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
---
[Table of Contents](#Table-of-Contents)

