import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

"""
Challenge
    1. Read in Loan Data
    2. Clean it
    3. Load into Panda DF
    4. Script to Generate boxplot, histogram, and QQ-plot for the values in the 
"Amount.Requested" column
    5. Save boxplot, histogram, and QQ-plot for the values in the 
"Amount.Requested" column
    6. Describe the result - compare "Amount.Funded.By.Investors" vs "Amount.Requested" 
"""

#1 - Read in load data - csv format #3. Save into Panda DF
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#3. CLeans Data removes null values 
loansData.dropna(inplace=True)


#Box Plots
loansData.boxplot(column='Amount.Requested')
plt.savefig("plots/boxPlotAmountRequested.png")

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.savefig("plots/boxPlotAmountFundedByInvestors.png")


#Histogram
loansData.hist(column='Amount.Requested')
plt.savefig("plots/histPlotAmountRequested.png")

loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("plots/histPlotAmountFundedByInvestors.png")


#QQ Plots
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("plots/QQPlotAmountRequested.png")

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("plots/QQPlotAmountFundedByInvestors.png")




