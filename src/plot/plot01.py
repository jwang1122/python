import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [1,4,9,16]
y2 = [1,8,27,64]
plt.plot(x,y1)
plt.plot(x,y2)
 
# when you want to give a label
plt.xlabel('This is X label')
plt.ylabel('This is Y label')
plt.show()