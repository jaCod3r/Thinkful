import pandas as pd
from scipy import stats


data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# Write a script called "stats.py" that prints the mean, median, mode, range, 
# variance, and standard deviation for the Alcohol and Tobacco dataset 
# with full text (ex. "The range for the Alcohol and Tobacco dataset is ..."). 

#Print Mean
meanAlcohol = df['Alcohol'].mean() 
meanTobacco = df['Tobacco'].mean()
print "The mean for the Alcohol and Tobacco dataset is %.3f and %.3f" % (meanAlcohol, meanTobacco)

#Print Median
medianAlcohol = df['Alcohol'].median()
medianTobacco = df['Tobacco'].median()
print "The median for the Alcohol and Tobacco dataset is %.3f and %.3f" % (medianAlcohol, medianTobacco)

# Print Mode
# https://docs.python.org/2/library/functions.html#format - information
modeAlcohol = stats.mode(df['Alcohol'])[0][0] 
modeTobacco = stats.mode(df['Tobacco'])[0][0] 
print "The mode for the Alcohol and Tobacco dataset is %.3f and %.3f" % (modeAlcohol, modeTobacco)

#Print Range
rangeAlcohol = max(df['Alcohol']) - min(df['Alcohol'])
rangeTobacco = max(df['Tobacco']) - min(df['Tobacco'])
print "The range for the Alcohol and Tobacco dataset is %.3f and %.3f" % (rangeAlcohol, rangeTobacco)

#Print variance
varianceAlcohol = df['Alcohol'].var() 
varianceTobacco = df['Tobacco'].var() 
print "The variance for the Alcohol and Tobacco dataset is %.3f and %.3f" % (varianceAlcohol, varianceTobacco)

#Print Standard Deviation
stdAlcohol = df['Alcohol'].std()
stdTobacco = df['Tobacco'].std()
print "The standard deviation for the Alcohol and Tobacco dataset is %.3f and %.3f" % (stdAlcohol, stdTobacco)



