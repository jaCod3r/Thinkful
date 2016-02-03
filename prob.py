# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:02:22 2016

@author: Juber
"""

"""
Write a script called "prob.py" that outputs frequencies, as well as creates
and saves a boxplot, a histogram, and a QQ-plot for the data in this lesson.
Make sure your plots have names that are reasonably descriptive.
Push your code to GitHub and enter the link below.

"""
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

#Sample Data
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7,
     7, 7, 7, 7, 7, 8, 8, 9, 9]

#Prints frequency of Data
frequencyOfX = collections.Counter(x)
count_sum = sum(frequencyOfX.values())
for k,v in frequencyOfX.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))


#Plots Box
plt.boxplot(x)
#plt.show() #Cannot invoke show method if going to save/ img doesnt appear
plt.savefig("plots/boxplot.png") #Saves the box plot into a jpeg

#Plots Histogram
plt.hist(x, histtype='bar')
#plt.show() #Shows the bar plot
plt.savefig("plots/barplot.png") #Saves the bar plot(histogram) into a jpeg

#QQ Plot Normal
plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
#plt.show() #this will generate the first graph
plt.savefig("plots/randnormalQQPlot.png") #Saves the the

#QQ Plot Unifrom
plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
#plt.show() #this will generate the second graph
plt.savefig("plots/randuniformQQPlot.png")
