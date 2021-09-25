import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim

path = '/Users/iuliano/Documents/projects/listings.csv'

df = pd.read_csv(path)

# Check the df shape
df.shape
df.info

# Price columns has no missing values, let's explore it
df['price'].describe()
# Dtype is obj, some values carry the dollar sign which will need to be dropped and converted to int
df['price'] = df['price'].str.replace('$', '')
df['price'] = df['price'].str.replace(',', '')
df['price'] = df['price'].astype(float)
df['price'].describe()

# One listing has 11999$ price which seems too high for an air bnb. I'm assuming that this might be data quality issue.
# As only 1 listing has this price, I will drop the row
df = df.drop(df[df.price == 11999].index)

# Plot price distribution
_ = plt.boxplot(df['price'])
_ = plt.title('Price Distribution')
plt.show()

# Percentiles and outliers boundary
lower_25 = np.percentile(df['price'], 25)
median = np.percentile(df['price'], 50)
upper_75 = np.percentile(df['price'], 75)
iqr = upper_75 - lower_25
upper_whisker = upper_75 + (1.5 * iqr)

# Identify outliers
outliers = df[df.price > upper_whisker]
outliers.id.count()
outliers.id.count() / len(df)
# 7% of the listings fall into the outliers' region

