import numpy as np 
a = np.array([1,2,3,4]) 

print ('Our array is:' )
print (a) 
print()  

print ('Applying average() function:' )
print (np.average(a)) 
print ()

# this is same as mean when weight is not specified 
wts = np.array([4,3,2,1])

# Weighted average = (1*4+2*3+3*2+4*1)/(4+3+2+1) 
print ('Applying average() function again:') 
print (np.average(a,weights = wts)) 
print ()

# Returns the sum of weights, if the returned parameter is set to True. 
print ('Sum of weights') 
print (np.average([1,2,3, 4],weights = wts, returned = True))