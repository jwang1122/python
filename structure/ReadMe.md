# Python File Structured

- [Python File Structured](#python-file-structured)
  - [File Structured](#file-structured)
  - [ModuleNotFoundError](#modulenotfounderror)
  - [ImportError:](#importerror)
  - [Solution (Get rid of from)](#solution-get-rid-of-from)
  - [Solution 2 (Change file structure)](#solution-2-change-file-structure)

## File Structured

```output
python-I
  └── structure/
    ├── main.py
    └── util.py
```

## ModuleNotFoundError
```py
# util.py

def doSomethingCool():
    print("Doing something cool...")
```

```py
# main.py
from structure.util import doSomethingCool

print("About to do something from main.")
doSomethingCool()
```

```output
(env) C:\Users\12818\workspace\python-I>c:/Users/12818/workspace/python-I/env/Scripts/python.exe c:/Users/12818/workspace/python-I/structure/main.py
Traceback (most recent call last):
  File "c:\Users\12818\workspace\python-I\structure\main.py", line 2, in <module>
    from structure.util import doSomethingCool
ModuleNotFoundError: No module named 'structure'
```

## ImportError: 
```py
# main.py
from .util import *

print("About to do something from main.")
doSomethingCool()
```

```output
(env) C:\Users\12818\workspace\python-I>c:/Users/12818/workspace/python-I/env/Scripts/python.exe c:/Users/12818/workspace/python-I/structure/main.py
Traceback (most recent call last):
  File "c:\Users\12818\workspace\python-I\structure\main.py", line 2, in <module>
    from .util import *
ImportError: attempted relative import with no known parent package
```
## Solution (Get rid of from)
```py
# main.py
import util

print("About to do something from main.")
util.doSomethingCool()
```

```output
(env) C:\Users\12818\workspace\python-I>c:/Users/12818/workspace/python-I/env/Scripts/python.exe c:/Users/12818/workspace/python-I/structure/main.py
About to do something from main.
Doing something cool...
```
## Solution 2 (Change file structure)
```output
python-I
  └── structure/
    ├── main.py
          └── utils
            ├── __init__.py
            └── util.py
```
```py
# main.py
import utils.util as util

print("About to do something from main.")
util.doSomethingCool()
```

```output
(env) C:\Users\12818\workspace\python-I>c:/Users/12818/workspace/python-I/env/Scripts/python.exe c:/Users/12818/workspace/python-I/structure/main.py
About to do something from main.
Doing something cool...
```
```py
# main.py
from utils.util import *

print("About to do something from main.")
doSomethingCool()
```

