import pandas as pd
import random
from datetime import timedelta


def cal(last_date, len_days):
    """Function returns len_days days and a random number assigned to it
    last_date: the date from which len_days days will be created
    len_days: len of the df"""
    global df
    last_date = pd.to_datetime('2021-01-1', format='%Y-%m-%d')
    dates = []
    counter = 0
    while counter <= len_days:
        d = last_date - timedelta(days=counter)
        dates.append(d)
        counter += 1
    dates = [d.strftime('%Y-%m-%d') for d in dates]
    metric = [random.randint(1, 50) for x in range(len(dates))]
    df = pd.DataFrame({'date': dates, 'metric': metric})
    return df
