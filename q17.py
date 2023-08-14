import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

fr = {}
file = pd.read_csv('data.csv')
f = file['feedback']
f1 = list(f)
st = set(['this', 'is', 'was', 'not'])
translator = str.maketrans('', '', string.punctuation)
p = []

for sentence in f1:
    words = sentence.lower().translate(translator).split()
    filtered = [word for word in words if word not in st]
    fil = str(filtered)
    p.append(fil)

for i in p:
    if i in fr:
        fr[i] += 1
    else:
        fr[i] = 1

n = int(input("Enter the value of n "))
top = Counter(fr).most_common(n)
print(top)
words, frequencies = zip(*top)

plt.bar(words, frequencies)
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title(f'Top {n} Most Frequent Words')

plt.show()
