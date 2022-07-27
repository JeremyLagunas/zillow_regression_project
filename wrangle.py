import pandas as pd
import numpy as np
import os
from env import host, user, password
import sklearn.preprocessing


# Acquire

def get_connection(db, user = user, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
# This function will be used in other functions to connect with the required databases. 

def new_zillow_data():
	# this query pulls houses that had a transaction date in 2017 and are considered to be single family residential properties
    sql_query = """
                   SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, lotsizesquarefeet, regionidzip, yearbuilt, poolcnt, fireplacecnt 
                   FROM properties_2017
                   JOIN predictions_2017 AS pred using (parcelid)
                   JOIN propertylandusetype AS prop using (propertylandusetypeid)
                   WHERE pred.transactiondate < '2018'
                   AND prop.propertylandusetypeid = 261;
                   """
    df = pd.read_sql(sql_query, get_connection('zillow'))
    return df

# Prepare

def zillow_clean(df):
    # rename our columns to make them easier to read and use
    df.rename(columns = {'bedroomcnt':'bed', 'bathroomcnt':'bath', 'calculatedfinishedsquarefeet':'square_feet', 'taxvaluedollarcnt':'price', 'lotsizesquarefeet':'lot_square_feet', 'regionidzip':'zipcode', 'yearbuilt':'year_built', 'poolcnt':'pool', 'fireplacecnt':'fireplace'}, inplace=True)
    # turn NaN in fireplace and pool to 0's
    df.fireplace = df.fireplace.fillna(value=0)
    df.pool = df.pool.fillna(value=0)
    # drop null values
    df = df.dropna()
    # only include houses with 6 or less bedrooms
    df = df[df.bed <= 6]
    # only include houses with 6 or less bathrooms
    df = df[df.bath <=6]
    # only include houses worth 2000000 dollars or less
    df = df[df.price <= 2000000]
    # only include houses with 6000 square feet or less
    df = df[df.square_feet <= 6000]
    # only include houses with at least one bedroom and one bathroom
    df = df[df.bed > 0]
    df = df[df.bath > 0]
    
    return df