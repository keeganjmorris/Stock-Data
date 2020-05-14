import pandas as pd
from pandas_datareader import data
import statistics
import matplotlib.pyplot as plt

print()
ticker = input("Enter the name of the ticker symbol you want to work with: ")
print()

#you can set automatic start and dates and ticker with this code 
#df = data.DataReader(ticker, start='2019-1-1', end='2019-12-31',data_source='yahoo') 
#or..

import timeToUnix

sd = timeToUnix.startDate
ed = timeToUnix.endDate

monthsDifference = timeToUnix.monthDiff
df = data.DataReader(ticker, start=sd, end=ed,data_source='yahoo') #dataframe
confidence=0.05



#df = pd.read_csv(fileName)   this code is if you manually want to download the .csv file off of yahoo


def Daily_Returns(df):
    # The logic here is that given a list of Adjusted Closes, Daily_Returns is 
    # calculated by dividing the Adj Close by the Previous Close (preceding Adj Close)
    
    # In order to do this I sliced the Adj Close array from the first onwards to omit the
    # first close price (since there is no preceding, it doesn't give us a daily return).

    # Then I sliced it again omitting the very last element to create two equally sized arrays
    # to create the previous_close array

    # The return statement performs the manipulation to these two arrays to yield daily_returns
    
    adj_close = df["Adj Close"][1:].values
    previous_close = df["Adj Close"][:-1].values 
    return (((adj_close/previous_close)-1)*100)

def Monthly_VaR(ticker:str, confidence): 
    #value at risk how: much are u expected to lose within a given month 
    returns = pd.DataFrame(Daily_Returns(df))
    VaR = returns.quantile(confidence)
    return VaR[0]

def Monthly_CVaR(ticker:str, confidence):
    #conditional value at risk
    returns = pd.DataFrame(Daily_Returns(df))    
    VaR = Monthly_VaR(ticker, confidence)
    CVaR = returns[returns.lt(VaR, axis=1)].mean()
    return CVaR[0]

def Monthly_Volatility(ticker):
    returns = (Daily_Returns(df)) 
    return statistics.stdev(returns) / monthsDifference # Divide by difference in dates months to get Monthly_Vol 


dr = Daily_Returns(df)
mv = Monthly_VaR(ticker, confidence)
mcv = Monthly_CVaR(ticker, confidence)
mvo  = Monthly_Volatility
print()
print("Daily Returns : ")
print(dr)
print()
print("Monthly Variance : ")
print(mv) 
print()
print("Monthly Conditional Variance : ")
print(mcv) 
print()
print("Monthly Variance : ")
print(mvo)
print() 

graph = plt.plot(dr)
print(graph)


    


