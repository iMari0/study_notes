import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

df = [random.randint(0,50) for x in range(0,100)]
df = pd.Series(df)#Only Series can be passed within sort index ()

#sort values by index
df.value_counts().sort_index()

#REPLACE: replace values given in a list with a desired values
values = df.replace([49], np.nan)

#Plot distribution
plt.hist(df.dropna(),bins = 5)

