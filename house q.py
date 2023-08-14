import pandas as pd
import numpy as np
h=pd.read_csv("house q3.csv")
arr=np.array(h)
price=h['price']
bedroom=h['nb']
av=np.mean(price[bedroom>3])
print(av)

