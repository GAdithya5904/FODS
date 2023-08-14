import pandas as pd
import numpy as np
from scipy import stats

data_product1 = {'rating': [4.2, 3.9, 4.5, 4.0, 4.3]}
data_product2 = {'rating': [3.8, 4.1, 4.4, 4.2, 4.6]}
df_product1 = pd.DataFrame(data_product1)
df_product2 = pd.DataFrame(data_product2)


t_statistic, p_value = stats.ttest_ind(df_product1['rating'], df_product2['rating'])

alpha = 0.05

print(f"T-Statistic: {t_statistic:.2f}")
print(f"P-Value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis - There is a significant difference.")
else:
    print("Fail to reject the null hypothesis - There is no significant difference.")
