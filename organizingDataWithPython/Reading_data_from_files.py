import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import requests
response = requests.get("https://gbfs.citibikenyc.com/gbfs/en/station_information.json")

if response.status_code != 200:
    print("Error with website. If problem persists, contact your Facilitator!")
else:
    print("Data download successful")

# variable is assigned to call the JSON
datadict = response.json()
print(datadict.keys())
print(datadict['data'].keys())


# last updated
print(datadict['last_updated'])
print(time.ctime(datadict['last_updated']))

nums = np.array([1, 2, 3, 4, 5, 7, 8, 9, 10])

np.savetxt('sales_test.txt', nums, header='New Nums', fmt='%d')
# print(nums)

# reading data from a url csv file changing data
# how to create a url csv link

poll_data = pd.read_csv('https://projects.fivethirtyeight.com/polls-page/president_primary_polls.csv', low_memory=False)
# print(poll_data)



