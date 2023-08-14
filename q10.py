import matplotlib.pyplot as plt
import numpy as np
month=np.array(['jan','feb','mar','april','may'])
sales=np.array([10,30,20,40,50])
plt.plot(month,sales)
plt.show()
plt.bar(month,sales)
plt.show()


