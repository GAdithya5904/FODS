import pandas as pd
file=pd.read_csv("qp.csv")
loc=file.groupby("location")
avg=loc["price"].mean()
print(avg)

mask=file['nb']>4
count=len(file[mask])
print(count,'is the number of bedrooms greater than 4')

print(file['area'].max(),'is the largest area')

