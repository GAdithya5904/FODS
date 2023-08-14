import matplotlib.pyplot as plt
import numpy as np
price=210
mont=np.array(['jan','feb','mar','april','may'])
sales=np.array([220,230,180,190,200])
profit=np.array([])
loss=np.array([])
for i in sales:
    if i >price:
        profit.append(i-price)
    else:
        profit.append(1)
print(profit)
for j in sales:
        if j<price:
            profit.append(price-i)
        else:
            loss.append(1)
plt.plot(mont,profit)
plt.show()
        
