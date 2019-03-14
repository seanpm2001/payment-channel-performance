import requests
import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(b * (x)) + c
#   return a * np.log(b * (x)) + c

def fitFunc(t, A, B, k):
    return A - B*np.exp(-k*t)

# get count
url = 'http://localhost:5000/gasmedian'
headers = {'content-type': 'application/json'}
response = requests.get(url, headers=headers)
results = json.loads(response.content)

print('count: ', str(len(results)))
print('an example of result:', results[0])

# gas_price of a transaction
x = []

# waiting_time of a transaction
y = []

for row in results:
    x.append(row['_id'])
    y.append(row['value'])

# get the max of actual cost
print('the max gas price is: ', str(max(x)))
print('the min gas price is: ', str(min(x)))
print('the max waiting time is: ', str(max(y)))
print('the min waiting time is: ', str(min(y)))

print(len(x))
print(len(y))

# Plot original data
plt.scatter(x, y)

# Fit a curve with exponential 
x = np.array(x, dtype=float) 
y = np.array(y, dtype=float)
# popt, pcov = curve_fit(func, x, y)
popt, pcov = curve_fit(fitFunc, x, y)

print(popt)
print(pcov)

# Plot curve fit
# plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")

plt.plot(x, fitFunc(x, *popt), 'r-', label="Fitted Curve")

plt.title('Relation between gas price and waiting time')
plt.xlabel('gas price')
plt.ylabel('waiting time')

# Set ranges of x-axis and y-axis
plt.xlim(0,50)
# # # plt.xlim(0.2,0.4)
plt.ylim(0,500)
plt.legend()
plt.show()

#

# # matplotlib histogram
# plt.hist(x, color = 'blue', edgecolor = 'black',
#          bins = int(180/5))

# # seaborn histogram
# sns.distplot(x, hist=True, kde=False, 
#              bins=int(180/5), color = 'blue',
#              hist_kws={'edgecolor':'black'})
# # Add labels
# plt.title('Histogram of Arrival Delays')
# plt.xlabel('Delay (min)')
# plt.ylabel('Flights')
# plt.show()