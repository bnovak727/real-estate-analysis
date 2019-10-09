#!/usr/bin/env python

import time
from selenium import webdriver
import pandas as pd
import os, glob
from range_key_dict import RangeKeyDict

price_to_redfin_range = RangeKeyDict({
    (0,49): None,
    (50,74): '50k',
    (75,99): '75k',
    (100,124): '100k',
    (125,149): '125k',
    (150,174): '150k',
    (175,199): '175k',
    (200,224): '200k',
    (225,249): '225k',
    (250,274): '250k',
    (275,299): '275k',
    (300,1000): '300k'})


def redfin(location, min_price=None, max_price=None):
    """
    """
    # Handle inputs
    min_price_str = price_to_redfin_range[min_price]
    max_price_str = price_to_redfin_range[max_price]

    # Go to redfin
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get('http://www.redfin.com')
    time.sleep(5)

    # Search location
    search_box_list = driver.find_elements_by_xpath('//*[@id="search-box-input"]');
    search_box = search_box_list[0]
    search_box.send_keys(location)
    search_box.submit()
    time.sleep(15)

    # Add filters
    city_url = driver.current_url

    filter_options = []
    if min_price_str is not None:
        filter_options.append('min-price=' + min_price_str)
    if max_price_str is not None:
        filter_options.append('max-price=' + max_price_str)
    filter_options.append('property-type=house+multifamily')
    filters = '/filter/' + ','.join(filter_options)

    filtered_url = city_url + filters
    driver.get(filtered_url)

    # Download data
    download = driver.find_elements_by_xpath('//*[@id="download-and-save"]')
    download = download[0]
    download.click()
    time.sleep(10)

    driver.quit()

    # Convert downloaded data to dataframe
    downloaded_files = glob.glob('/Users/bnovak/Downloads/redfin*.csv')
    newest_time = 0
    for f in downloaded_files:
        if os.path.getctime(f) > newest_time:
            newest_time = os.path.getctime(f)
            newest_file = f

    df = pd.read_csv(newest_file)
    
    return df

if __name__ == "__main__":
    df = redfin('Ypsilanti, MI', 50, 250)
    print(df)
