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
plt.savefig("plots/boxplot.png") #Saves the box plot into a jpeg

#Plots Histogram
plt.hist(x, histtype='bar')
plt.savefig("plots/barplot.png") #Saves the bar plot(histogram) into a jpeg

#QQ Plot Normal
plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("plots/randnormalQQPlot.png") #Saves the the

#QQ Plot Unifrom
plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("plots/randuniformQQPlot.png")
