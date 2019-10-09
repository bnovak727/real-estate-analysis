# This script parses zillow real estate data

import pandas as pd
import numpy as np
import os

# Parse Data
path = os.getcwd()
data_path = path + "/data/"

# Price to rent ratio
price_to_rent_file = data_path + "/Zip_PriceToRentRatio_AllHomes.csv"
df_p2r = pd.read_csv(price_to_rent_file)
print('Price to rent ratio')
p2r_lt_05 = lt_quantile_loc(df_p2r, -1, 0.05)
p2r_lt_05.sort(p2r_lt_05.columns[-1], inplace=True)
print(p2r_lt_05.iloc[:,[0,2,-1]])
exit(0)

# Price History
price_history_file = data_path + "/Zip_Zri_SingleFamilyResidence.csv"
df_price_history = pd.read_csv(price_history_file)
print('Price History Headers')
print(list(df_price_history))

# Market Health Index
market_health_file = data_path + "/MarketHealthIndex_Zip.csv"
df_health = pd.read_csv(market_health_file)
print('Market Health')
print(list(df_health))

# Rental Index
rental_index_file = data_path + "/Zip_Zri_SingleFamilyResidenceRental.csv"
df_ri = pd.read_csv(rental_index_file)

zhvi_95_percentile = df_health['ZHVI'].quantile(q=0.95)
zips_95_per = df_health.loc[df_health['ZHVI'] > zhvi_95_percentile, ['RegionName']]

zips_95_per = gt_quantile_name(df_health, 'ZHVI', 0.95)
#print(get_df_col(zips_95_per, 'RegionName'))

zips_5_p2r = lt_quantile_loc(df_p2r, -1, 0.5)
#print(get_df_col(zips_5_p2r, 'RegionName'))
