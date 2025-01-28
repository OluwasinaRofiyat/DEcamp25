#!/usr/bin/env python
# coding: utf-8


pip install sqlalchemy psycopg2-binary
from sqlalchemy import create_engine
from time import time
import pandas as pd

import pandas as pd





pd.__version__




df1 =pd.read_csv('/workspaces/DEcamp25/taxi_zone_lookup.csv')





df1.head()





df = pd.read_csv('/workspaces/DEcamp25/green_tripdata_2019-10.csv.gz', dtype={'store_and_fwd_flag': str})


df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'], format='%Y-%m-%d %H:%M:%S')

df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'], format='%Y-%m-%d %H:%M:%S')


pd.io.sql.get_schema(df, 'green_taxi_data')




engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')





print(pd.io.sql.get_schema(df, 'green_taxi_data'))











print(pd.io.sql.get_schema(df1, 'taxi_zone_lookup', con=engine))



print(pd.io.sql.get_schema(df, 'green_taxi_data', con=engine))



df_iter = pd.read_csv('/workspaces/DEcamp25/green_tripdata_2019-10.csv.gz', iterator= True, chunksize = 100000)



get_ipython().run_line_magic('time', "df.to_sql(name= 'green_taxi_data', con=engine, if_exists='append')")







while True:
    try:
        t_start = time()
        
        # Fetch the next chunk
        df = next(df_iter)

        # Convert datetime columns
        df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'], format='%Y-%m-%d %H:%M:%S')
        df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'], format='%Y-%m-%d %H:%M:%S')

        # Write the chunk to the database
        df.to_sql(name='green_taxi_data', con=engine, if_exists='append')

        t_end = time()
        print(f"Inserted another chunk... took {t_end - t_start:.3f} seconds")
    
    except StopIteration:  # Correct exception handling
        print("All chunks processed. Exiting loop.")
        break


















