## Useful Icons

❓✔️ 👍😄 👎😱 ❌✔️ 💡👉 🔔⚡️ 🔒🔑
✏️📄✂️♻️
📌❗️📝🔍🔨☝️👇👈👉👍👎👌👊⭐️😢🌎💾🗑🐛📒⚠️🔥🛠📐🎯✉️☎️

:hammer:

[](images/bug.png)
<img src="images/bug.png" width="32"/>

## references
* [Color Picker](https://www.webfx.com/web-design/color-picker/)
* [favorite icon website](https://www.webfx.com/tools/emoji-cheat-sheet/)

## Sample File Structure:

```output
<project root>
    ├── 📝doc/
    |    ├── mistakes.md 
    |    └── python.md 
    ├── 🔨homeworks/
    |       └── filenameXX.md
    ├── 🔥src/
    |       └── string.py
    └── 👉ReadMe.md
```

## Sample Mermaid Diagram

😄Include frequently used mermaid diagram features below👇

```mermaid
graph TB

START((start))
END[end]
B[code block]
C(["Round box<br>function(arguments)"])
IF{condition<br> block}
DB[(database)]

START-->IF
IF--True-->DB-->END
IF--False-->B-->END

classDef start fill:blue,stroke:#DE9E1F,stroke-width:2px,color:white;
classDef html fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef js fill:yellow,stroke:black,stroke-width:2px;
classDef if fill:#EBCD6F,stroke:black,stroke-width:2px;
classDef db fill:#BEBDB7,stroke:black,stroke-width:2px;
classDef end1 fill:red,stroke:#DE9E1F,stroke-width:2px,color:white;

class START start
class B,D,E js
class IF if
class DB db
class END end1
```