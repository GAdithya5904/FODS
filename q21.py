import numpy as np
import pandas as pd

file=pd.read_csv('q21.csv')
arr=np.array(file['unit'])

p=np.mean(arr)
s=np.std(arr)

s=int(input("enter sample size"))
c_l=float(input("enter confidence level"))

arr_se=s/(len(arr)**0.5)

arr_ci=p+(c_l*arr_se)
arr_ci1=p-(c_l*arr_se)

print('the confidence intreval of the given dataset is' ,arr_ci,'to',arr_ci1)



