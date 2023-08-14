import pandas as pd
file=pd.read_csv("order_data q7.csv")
cust=file.groupby("id")
summ=cust['quantity'].sum()
print(summ)

prod=file.groupby("name")
avg=prod["quantity"].mean()
print(avg)

file['date']=pd.to_datetime(file['date'])
print(file['date'].min().date())
print(file['date'].max().date())
