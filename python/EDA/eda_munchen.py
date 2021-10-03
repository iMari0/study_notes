import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading data
path = '/Users/iuliano/Documents/projects/listings.csv'
df = pd.read_csv(path)

# Check the df shape
print(df.shape)
print(df.info)

# Will store the original share to have a percentage of data that we'll lose after dropping nan and outliers
original_shape = df.shape

# First observation goes to the 'price' dtype --> obj. Investigating why and convert it into float
print(df['price'].sample(10))
# Dtype is obj, some values carry the dollar sign which will need to be dropped and converted to float
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
         'longitude', 'room_type', 'accommodates', 'bedrooms',
         'beds', 'price']]

# I will investigate the price distribution to have a general idea of listings prices in the city
print(df['price'].describe())

# Observations: prices with 0 values will be considered as corrupted data. Analysing the impact on the dataset
zero_price = df['price'][df['price'] == 0].value_counts()
# Only 3 listings: will drop those observations
df = df.drop(df[df.price == 0].index)
print(df['price'].describe())
plt.boxplot(df['price'])

# By plotting the price distribution, we can see the presence of outliers
# I want to be sure that the prices are not the result of poor data quality.
# First I will assign the list of outliers to a variable.
# Outliers will contain all listings with a price > upper_whisker

# Percentiles and outliers boundary
q_1, q_2, q_3 = df['price'].quantile([0.25, 0.5, 0.75])
iqr = q_3 - q_1
upper_whisker = q_3 + (1.5 * iqr)

# Identify outliers
outliers = df[df.price > upper_whisker]
outliers.listing_url.count()
outliers.listing_url.count() / len(df)
# 7% of the listings fall into the outliers' region

# I want to look at the distribution of the outliers to understand how prices vary
outliers.describe()
o_q_1, o_q_2, o_q_3 = outliers['price'].quantile([0.25, 0.5, 0.75])
o_iqr = o_q_3 - o_q_1
o_upper_whisker = o_q_3 + (1.5 * o_iqr)
outliers[['beds', 'bedrooms', 'neighbourhood_cleansed', 'price']].sort_values(by='price')
print(o_upper_whisker)

# The upper whisker of the outliers' list is 705.
# For simplicity, I will check the percentage of listings with prices above this threshold.
# I will eventually remove the observations if the impact is not too big
round(df['price'][df.price > o_upper_whisker].count() / len(df), 2)
# 0.01% of listings fall into this region. I will drop these observations to remove noise from the data.
df = df.drop(df[df.price > o_upper_whisker].index)

print(df['price'].describe())
_ = sns.distplot(df['price'], color='b')
_ = plt.title("Price Distribution")
_ = plt.xlabel("Price")
_ = plt.ylabel("Percentage of Listings in Bin")
plt.show()


# Plotting ECDF
def ecdf(df, column):
    data = df[column]
    x = np.sort(data)
    y = np.arange(1, len(df) + 1) / len(df)
    plt.plot(x, y, linestyle='none', marker='.')
    plt.title(f"ECDF {column.upper()} ")
    plt.legend()
    plt.xlabel(column.upper())
    plt.ylabel("Probability")
    plt.show()


# Analysing distribution w/ and w/o outliers
ecdf(df, 'price')
ecdf(df[df.price < upper_whisker], 'price')
plt.legend()


fig, ax = plt.subplots(2)
ax[0].boxplot(df['price'], vert=False)
ax[0].set_title('Price Distribution w/ Outliers')
ax[1].boxplot(df['price'][df.price < upper_whisker], vert=False)
ax[1].set_title('Price Distribution w/o Outliers')


# There are still some nan in bedrooms and beds.
# In this section I'm not going to focus on the best approach to handle them
# I simply impute the median
# Another option could be to scrape 'description' and look up for strings containing that info
df['bedrooms'] = df['bedrooms'].fillna(df.bedrooms.median())
df['beds'] = df['beds'].fillna(df.bedrooms.median())

# How much data we lost? --> 0.1%
data_loss = 1 - round(df.shape[0] / original_shape[0], 2)

# Now let's explore correlations among int types
num = df.select_dtypes(include=['int64', 'float64'])
num.hist()
