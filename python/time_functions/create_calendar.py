from datetime import datetime,date,timedelta
import pandas as pd

#Define time var
today = date.today()
d_from = date(2020, 1, 1)
t_range = today-d_from
t_range = t_range.days

#Function for iterating
counter= 0
d = []
while counter <= t_range:
    day = date.today() - timedelta(days = counter)
    day = day.strftime('%Y, %m, %d')
    d.append(day)
    counter+=1

df = pd.DataFrame({'date': d,
                   'val': [x for x in range(t_range+1)]})