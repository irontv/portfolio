# https://www.youtube.com/watch?v=O-O1WclwXck

from datetime import datetime
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Get the stock symbols for the portfolio
stockSymbols = ["FB", "AAPL", "NFLX"]

# Get today' date and format it in the form of YYYY-mm-dd
stockStartDate = '2021-08-01'
today = datetime.today().strftime('%Y-%m-%d')
print(today)

# Get the number of assets in the portfolio
numAssets = len(stockSymbols)
print('You have ' + str(numAssets) + ' assets in your portfolio.')

# Create a function to get the stock prices in the portfolio
def getMyPortfolio(stocks=stockSymbols, start=stockStartDate, end=today, col='Adj Close'):
  data = web.DataReader(stocks, data_source='yahoo', start=start, end=end)[col]
  return data

# Get the stock portfolio Adj. Close price
my_stocks = getMyPortfolio()
print(my_stocks)
def getStockData(stocks=stockSymbols, start=stockStartDate, end=today):
  for s in stocks:
    s_data = web.DataReader(s, data_source='yahoo', start=start, end=end)
    s_data.to_csv(s, index=True, float_format='%.2f', sep=' ')

getStockData()
# Create a function to visualize the portfolio
def showGraph(stocks=stockSymbols, start=stockStartDate, end=today, col='Adj Close'):

  # Create a title for the portfolio
  title = 'Porfolio ' + col + ' Price History'

  # Get the stocks
  my_stocks = getMyPortfolio(stocks, start, end, col)
  # print(my_stocks.columns)
  # print(my_stocks.values)
  # print(my_stocks.columns.values)
  # for c in my_stocks.columns.values:
  #   print(my_stocks[c])

  plt.figure(figsize=(20.2, 8.5))   # inches in width & height
  for c in my_stocks.columns.values:
    plt.plot(my_stocks[c], label=c)

  plt.title(title)
  plt.xlabel('Date', fontsize = 18)
  plt.ylabel(col + ' Price USD ($)', fontsize = 18)
  plt.legend(my_stocks.columns.values, loc='upper left')
  plt.show()

showGraph(stockSymbols, stockStartDate, today, 'Adj Close')

# Calculate the simple returns
daily_simple_returns = my_stocks.pct_change(1)

# show the daily simple returns
print(daily_simple_returns)
# Show the stock correlation
print(daily_simple_returns.corr())

# Show the covariance matrix for simple returns
print(daily_simple_returns.cov())

# show the variance
print(daily_simple_returns.var())
# Print the standard deviation for daily simple returns

print("The Stock Volatility:")
print(daily_simple_returns.std())
# Visualize the stocks daily simple returns

plt.figure(figsize=(12, 4.5))

for c in daily_simple_returns.columns.values:
    plt.plot(daily_simple_returns.index, daily_simple_returns[c], lw=2, label=c)

plt.legend(loc='upper right', fontsize=10)
plt.title('Volatility')
plt.xlabel('Date')
plt.ylabel('Daily Simple Returns')
plt.show()
# the mean of the daily simple return
dailyMeanSimpleReturns = daily_simple_returns.mean()
print(dailyMeanSimpleReturns)

# Calculate the expected portfolio daily return
randomWeights = np.array([0.5, 0.2, 0.3]) # 50% FB, 20% AAPL, 30% NFLX
print(randomWeights)
print(dailyMeanSimpleReturns.values)
portfolioSimpleReturn = np.sum(dailyMeanSimpleReturns * randomWeights)
print(portfolioSimpleReturn)
# Get the yearly simple return for the yearly trading days
print("Expected annualised portfolio simple return: " + str(portfolioSimpleReturn * 253))
# Calcualte the growth of the investment
dailyCumulSimplReturn = (daily_simple_returns+1).cumprod()
print(dailyCumulSimplReturn)

print((daily_simple_returns['FB'][1] + 1) * (daily_simple_returns['FB'][2] + 1))
# Visualize the daily simple cumulative simple returns

plt.figure(figsize=(12.2, 4.5))
for c in dailyCumulSimplReturn.columns.values:
    plt.plot(dailyCumulSimplReturn[c], lw=2, label=c)

plt.legend(loc='upper left', fontsize=10)
plt.xlabel('Date')
plt.ylabel('Growth of $1 investment')
plt.title('Daily cumulative Simple Returns')
plt.show()