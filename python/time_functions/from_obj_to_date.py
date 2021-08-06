from datetime import datetime, timedelta,date
import pandas as pd

day = '2021-01-01'
print(type(day))
conv_day = datetime.strptime(day, '%Y-%m-%d')
conv_day = conv_day.date()
print(type(conv_day))

#Applied to df column - pd.to_datetime

df = pd.DataFrame({'date': ['2021-01-01','2021-02-01','2021-03-01'],
                   'count': [1,2,3]})

df['date']= pd.to_datetime(df['date'],format='%Y-%m-%d')

#PRACTICE#
#CREATE A DATAFRAME BY ITERATING N DAYS#
def date_generator(n_days):
    counter = 1
    today = date.today()
    date_list = []
    for x in range(n_days):
        counter +=1
        date_list.append(today+timedelta(days = counter))
    return date_list

df = pd.DataFrame({'date': date_generator(10),
                   'count': [x for x in range(10)]})

df['day'] = pd.DatetimeIndex(df['date']).month
