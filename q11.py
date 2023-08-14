import matplotlib.pyplot as plt
import numpy as np
month=np.array(['jun','jul','aug','sep','oct'])
sales=np.array([10,90,15,40,60])
plt.plot(month,sales)
plt.show()
plt.bar(month,sales)
plt.show()
plt.scatter(month,sales)
plt.show()


