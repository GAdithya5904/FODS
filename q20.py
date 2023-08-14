import numpy as np
A=np.array([4,7,3,9,5,6,8])
B=np.array([6,4,7,8,1,5,9])
A_p=1000
B_p=1000

A_mean=np.mean(A)
B_mean=np.mean(B)

a1=A_p*A_mean
b1=B_p*B_mean

p=(a1+b1)/(A_p+B_p)

SE=(((p*(1-p))*(1/A_p+1/B_p))**0.5)

t=(A_mean-B_mean)/SE

T=abs(t)

if T>1.96:
    print('there is a significant diffrence')
else:
    print('there is no significant diffrence')
