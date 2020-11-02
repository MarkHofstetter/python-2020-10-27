from pprint import pprint
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('daten.csv', delimiter =';', header=1, decimal=",")

print(data['2004'])

data.plot(kind='line')
plt.show()

# print(np.mean(data.iloc[1]))
data['mean'] = data.mean(axis = 1)
data['max'] = data.max(axis = 1)
print(data)