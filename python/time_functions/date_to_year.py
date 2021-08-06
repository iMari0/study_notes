# CREATE A COLUMN EXTRACTING YEAR FROM DATE DIMENSION #

import pandas as pd
import sqlalchemy as sa
from pandas import ExcelWriter
from datetime import datetime

DATABASE = "prd"
USER = "iuliano"
PASSWORD = "7xmajmuWCWj0c2N74TRz"
HOST = "10.217.198.5"
PORT = "5439"
SCHEMA = "public"

engine = sa.create_engine('postgres://iuliano:7xmajmuWCWj0c2N74TRz@10.217.198.5:5439/prd')
connection = engine.connect()

# Creating connection and assigning SQL query results into 'df'
with engine.connect() as conn, conn.begin():
    df = pd.read_sql("""
 Select *
from analytics.v_efa_ga
where companyid isnull
""", conn)


df['year'] = pd.DatetimeIndex(df['date']).year
#documentation https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html