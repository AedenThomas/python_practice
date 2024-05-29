# How to get the dates of yesterday, today and tomorrow using datetime numpy function?

import numpy as np

yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
