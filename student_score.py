import pandas as pd
import numpy as np
arr=pd.read_csv("student_Score.csv")
avg_score=np.mean(arr,axis=0)
print(avg_score)
h_s=np.argmax(avg_score)
sub=['sub1','sub2','sub3','sub4']
print(sub[h_s],'=',max(avg_score))
