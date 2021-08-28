"""
Understand monad
"""

class Monad:
  # pure :: a -> M a
  @staticmethod
  def pure(x):
    raise Exception("pure method needs to be implemented")
  
  # flat_map :: # M a -> (a -> M b) -> M b
  def flat_map(self, f):
    raise Exception("flat_map method needs to be implemented")

  # map :: # M a -> (a -> b) -> M b
  def map(self, f):
    return self.flat_map(lambda x: self.pure(f(x)))

class Option(Monad):
  # pure :: a -> Option a
  @staticmethod
  def pure(x):
    return Some(x)

  # flat_map :: # Option a -> (a -> Option b) -> Option b
  def flat_map(self, f):
    if self.defined:
      return f(self.value)
    else:
      return nil
  
  def __rshift__(self, f): # override >> operator
    return self.flat_map(f)


class Some(Option):
  def __init__(self, value):
    self.value = value
    self.defined = True
  
  def __repr__(self):
    return str(self.value)

class Nil(Option):
  def __init__(self):
    self.value = None
    self.defined = False
  
  def __repr__(self):
    return "Undefined"

nil = Nil()


def add4(x):
  return Some(x + 4)


def mul5(x):
  return Some(x * 5)


def div2(x):
  return Some(x / 2)

def sub10(x):
  if x < 10:
    # return nil      # if something happen, give up
    return mul5(x)    # if something happen, do something else
  return Some(x - 10) 

if __name__ == '__main__':
  x = Some(3).flat_map(add4)
  print(x)

  x = nil.flat_map(sub10)
  print(x)

  x = x.pure(1) # change value
  print(x)

  x = x.flat_map(mul5).flat_map(sub10).flat_map(div2) # function chain
  print(x)

  x = x >> mul5 >> sub10 >> div2 >> add4
  print(x)

  print("Done.")