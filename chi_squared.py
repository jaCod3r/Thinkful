"""
Challenge
    1. Write a script called "chi_squared.py" 
    2. Loads the data 
    3. Cleans it 
    4. Performs the chi-squared test 
    5. Prints the result. 
    6. Push your code to GitHub

"""
import collections
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


#2 - Read in load data - csv format
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#3. CLeans Data removes null values 
loansData.dropna(inplace=True)

#4 - Performs the Chi-Squared Test 
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()
chi, p = stats.chisquare(freq.values())

#5 Prints the result
print "%.3f" % (chi)
print "%.3f" % (p)