# point rotation in python

import math 

def rotate_point(point, angle): 
    angle = math.radians(angle) 

    rotated_x = point[0] * math.cos(angle) - point[1] * math.sin(angle) 
    rotated_y = point[0] * math.sin(angle) + point[1] * math.cos(angle) 

    return (rotated_x, rotated_y) 
  
# Driver Code 
point = (5, 6) 
angle = 45
  
print("Rotated Point is:", rotate_point(point, angle))