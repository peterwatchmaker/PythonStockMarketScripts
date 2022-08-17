import yfinance as yf
import mplfinance as mpf
import pprint
import datetime
import requests
from bs4 import BeautifulSoup;
#ticker = "hln"
#yticker = yf.Ticker(ticker)
def plotprices(ticker,interval:str,period:str):
    #ticker = "hln"
    #interval = "1h" # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    #period = "1y" # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    
    df = ticker.history(period=period,interval=interval) # max, 1y, 3mo, etc
    #yticker = yf.Ticker(ticker)
    mpf.plot(df, type='candle', style='charles', volume=True,title="{} - period={} - interval={}".format(ticker.ticker, period, interval))

#plotprices(yticker,'1h','5d')
#plotprices(yticker,'1d','3mo')
#plotprices(yticker,'2m','1d')
response = requests.get("https://www.nasdaq.com/market-activity/dividends")
response
content = response.content
parser = BeautifulSoup(content, 'html.parser')
parser