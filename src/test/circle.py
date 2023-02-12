import os
import sys

fpath = os.path.join(os.path.dirname(__file__), '../mymath')
sys.path.append(fpath)
print(sys.path)

from simple import circleArea

r = 1
area = circleArea(r)
print(area)