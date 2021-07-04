import markdown

text = """
# Title

Some text.

​~~~mermaid
graph TB
A --> B
B --> C
​~~~

Some other text.

​~~~mermaid
graph TB
D --> E
E --> F
​~~~
"""

html = markdown.markdown(text, extensions=['md_mermaid'])

print(html)