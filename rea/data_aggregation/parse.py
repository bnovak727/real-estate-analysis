# Parse and merge Zillow data

import pandas as pd
import numpy as np
import os

# Parse Data
path = os.getcwd()
data_path = path + "/../data/"

# Price to rent ratio
price_to_rent_file = data_path + "/Zip_PriceToRentRatio_AllHomes.csv"
df_p2r = pd.read_csv(price_to_rent_file)
df_p2r = df_p2r.add_prefix('p2r_')
df_p2r = df_p2r.rename(columns={'p2r_RegionName': 'ZipCode'})

# Price History
price_history_file = data_path + "/Zip_Zri_SingleFamilyResidence.csv"
df_price_history = pd.read_csv(price_history_file)
df_price_history = df_price_history.add_prefix('ph_')
df_price_history = df_price_history.rename(columns={'ph_RegionName': 'ZipCode'})

# Market Health Index
market_health_file = data_path + "/MarketHealthIndex_Zip.csv"
df_health = pd.read_csv(market_health_file)
df_health = df_health.add_prefix('health_')
df_health = df_health.rename(columns={'health_RegionName': 'ZipCode'})

# Rental Index
rental_index_file = data_path + "/Zip_Zri_SingleFamilyResidenceRental.csv"
df_ri = pd.read_csv(rental_index_file)
df_ri = df_ri.add_prefix('ri_')
df_ri = df_ri.rename(columns={'ri_RegionName': 'ZipCode'})

# Merge Data
df_complete = pd.merge(df_p2r, df_price_history, on='ZipCode')
df_complete = pd.merge(df_complete, df_health, on='ZipCode')
df_complete = pd.merge(df_complete, df_ri, on='ZipCode')

print(list(df_complete))
