'''
Author: Michael Mazzone
Used: https://github.com/hongtaocai/googlefinance

A simple module wrapping the above googlefinance tool to return exchange and
stock price stripped of any surrounding characters.
'''

from googlefinance import getQuotes
import json
import re

def printFullStockDetail(tickerSymbol):
    '''
    Print the unedited json dump for given stock ticker(s).

    Example: printFullStockDetail(['AAPL', 'VIE:BKS'])
    Prints: entire dump from getQuotes for both AAPL and VIE:BKS
    '''
    try:
        print(json.dumps(getQuotes(tickerSymbol), indent = 2))
    except:
        print("Bad stock symbol.")

re_StockPriceRaw = r'(Price": "\d+\.?\d+")' # RegEx for line containing price
re_StockPrice = r'\d+\.?\d+' # RegEx for dollar amount only (from full line)

def getStockPrice(tickerSymbol):
    '''
    Return the value of the given stock ticker as string.

    Use regex to first get full price line, then use regex again
    to get only the dollar value.
    '''
    try:
        company = json.dumps(getQuotes(tickerSymbol), indent = 2)
        rawPriceData = re.search(re_StockPriceRaw, company)
        stockPrice = re.search(re_StockPrice, rawPriceData.group(0))

        print(tickerSymbol + ": $" + stockPrice.group(0))
        return stockPrice.group(0)
    except:
        print("Bad stock symbol, can't determine price.")

re_StockExchangeRaw = r'("Index": "\D+"\,)' # RegEx for line containing exchange
re_StockExchange = r'"[A-Z]+"' # RegEx for quoted exchange
re_QuoteTrimmer = r'[A-Z]+' # RegEx for exchange stripped of quotes

def getStockExchange(tickerSymbol):
    '''
    Return the stock exchange of the given stock ticker as string.

    Use regex to first get full Exchange line, then use regex again to
    only get the quoted Exchange, then a final time to strip quotes.
    '''
    try:
        company = json.dumps(getQuotes(tickerSymbol), indent = 2)
        rawExchangeData = re.search(re_StockExchangeRaw, company)
        stockExchangeQuoted = re.search(re_StockExchange, rawExchangeData.group(0))
        stockExchange = re.search(re_QuoteTrimmer, stockExchangeQuoted.group(0))

        print(tickerSymbol + " exchange: " + stockExchange.group(0))
        return stockExchange.group(0)
    except:
        print("Bad stock symbol, can't determine exchange.")
