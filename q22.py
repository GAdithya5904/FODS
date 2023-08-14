import pandas as pd
import numpy as np
file=pd.read_csv('q22.csv')
cr=np.array(file['cr'])
z=1.96

cr_m=np.mean(cr)
cr_s=np.std(cr)
cr_l=len(cr)

cr_se=cr_s/(cr_l**0.5)

cr_ci=cr_m+(z*cr_se)
cr_cii=cr_m-(z*cr_se)

print("the confidence intreval of the given data is:",cr_ci,'to',cr_cii)


