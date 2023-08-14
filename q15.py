import pandas as pd
file=pd.read_csv('q15.csv')
count=file['likes'].value_counts()
print(count)
