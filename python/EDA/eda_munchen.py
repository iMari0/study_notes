import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim
import seaborn as sns

path = '/Users/iuliano/Documents/projects/listings.csv'

df = pd.read_csv(path)

# Check the df shape
print(df.shape)
print(df.info)

# First observation goes to the 'price' dtype --> obj. Investigating why and convert it into float
print(df['price'].sample(10))
# Dtype is obj, some values carry the dollar sign which will need to be dropped and converted to int
df['price'] = df['price'].str.replace('$', '')
df['price'] = df['price'].str.replace(',', '')
df['price'] = df['price'].astype(float)
df['price'].describe()

# Percentage of nulls in columns
df2 = df[[c for c in df if df[c].count() / len(df) >= 0.3]]
# Deleting columns where share of null values is up to 30% of all column data
print("List of dropped columns", end=" ")
for c in df:
    if c not in df2:
        print(c, end=',')
df = df2

# In this section I will only focus on the listing status excluding traffic data
print(df2.columns)
df = df[['listing_url', 'neighbourhood_cleansed', 'latitude', 'longitude',
         'longitude', 'room_type', 'accommodates', 'bathrooms_text', 'bedrooms',
         'beds', 'price']]

# I will investigate the price distribution to have a general idea of listings prices in the city
print(df['price'].describe())

# Observations: prices with 0 values will be considered as corrupted data. Analysing the impact on the dataset
zero_price = df['price'][df['price'] == 0].value_counts()
# Only 3 listings: will drop those observations
df = df.drop(df[df.price == 0].index)

# One listing has 11999$ price which seems too high for an air bnb. I'm assuming that this might be data quality issue.
# As only 1 listing has this price, I will drop the row
df = df.drop(df[df.price == 11999].index)
print(df['price'].describe())


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
