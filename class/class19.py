"""
Inner or Nested Classes
Composition vs. Inheritance
1. Every car need engine, and engine won't be used without car
    make Engine a inner class of Car class.
2. Hiding code Engine for outside use.
3. Easy to understand the relation of classes.
"""

class Outer:
    class Inner:
        pass
        class InnerInner:
            pass
    
    class _Inner:
        pass

print(dir(Outer))
print(type(Outer.Inner))