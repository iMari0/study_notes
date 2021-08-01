import numpy as np
import pandas as pd
from sklearn.utils import resample
import numpy as np
from numpy import random

#Create the sample
my_sample = [np.random.randint(1,1000) for x in range(1000)]

#Define empty list where sample statistics will be appended
results = []
for x in range(1000):
    sample = resample(my_sample)
    results.append(np.percentile(sample,50))
results = pd.Series(results)
print("Bootstrap statistics:")
print(f'original: {np.percentile(my_sample,50)}')
print(f'bias: {np.mean(results)-np.mean(my_sample)}')
print(f'std. error: {results.std()}')
