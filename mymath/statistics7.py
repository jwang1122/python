from statistics import mean, pstdev, pvariance

l = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
mu = mean(l)
N = len(l) 
s = 0
for x in l:
    s += pow((x-mu),2)
jfc = pow(s/N, 0.5)
print("PSD calculated by python for-loop:",jfc)

jfc = pstdev(l)
print("PSD calculated by pandas function:",jfc)

pv = pvariance(l)
print("The population variance is",pv)
print("The population standard diviation is",pow(pv, 0.5))