from statistics import stdev, pstdev

l = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
sd = stdev(l)
print(sd)

psd = pstdev(l)
print(psd)

'''
Understand population mean and sample mean
sample mean is not equal to population mean, but if the sample is random 
and large enough it could be very close to the population mean.
'''

l=(1,1,2,2,2,3,3,4,5,5)
barX = sum(l)/len(l)
print(barX)

