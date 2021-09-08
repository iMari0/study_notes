import numpy as np
import random
import pandas as pd
import scipy.stats
from matplotlib import pyplot as plt

clicks_a = [random.randint(0, 1) for x in range(100)]
sessions_a = len(clicks_a)
clicks_b = [random.randint(0, 1) for x in range(100)]
sessions_b = len(clicks_b)
conversions_a = sum(clicks_a) / sessions_a
conversions_b = sum(clicks_b) / sessions_b
not_conv_a = sessions_a - sum(clicks_a)
not_conv_b = sessions_b - sum(clicks_b)

df = pd.DataFrame({'Group': ['A', 'B'],
                   'Sessions': [sessions_a, sessions_b],
                   'Clicks': [sum(clicks_a), sum(clicks_b)],
                   'Not Clicked': [not_conv_a, not_conv_b],
                   'Conversions': [conversions_a, conversions_b]})

e_a = sessions_a * (sum(df['Clicks']) / (sessions_a + sessions_b))
e_b = sessions_b * (sum(df['Clicks']) / (sessions_a + sessions_b))

print(df)

#Plot the conversions
_ = plt.title('Conversion Rate for A/B')
_ = plt.xlabel("Groups")
_ = plt.ylabel("Conversion %")
plt.bar(df['Group'], df['Conversions'], color = ['b','g'])
plt.show()

print("The expected value shows how we should expect the data to turn out under the assumption of the null hypothesis"
      "\n (Practical Statistics for Data Science p.124")
print("The expected value will be the product of the all sessions in each group (A,B) by probability of click \n")
print("probability of click = sum(clicks)/sessions_a+sessions")
print("For Example, the expected value of A will be: \n ", e_a)
print("The observed values are the clicks in each group", df['Clicks'])


# Data prepartion for contingency table
array_a = np.array([sum(clicks_a), not_conv_a])
array_b = np.array([sum(clicks_b), not_conv_b])
T = np.array([array_a, array_b])
chi_square = round(scipy.stats.chi2_contingency(T, correction=False)[1],2)


