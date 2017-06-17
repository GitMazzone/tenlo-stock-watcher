'''
Author: Michael Mazzone
Used: https://github.com/hongtaocai/googlefinance

A simple module wrapping the above googlefinance tool to return exchange and
stock price stripped of any surrounding characters. All stock data is fetched in
real time.
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
re_StockPrice = r'\d+\.?\d+' # RegEx for dollar amount

def getStockPrice(tickerSymbol):
    '''
    Return the value (as string) of the given stock ticker.
    Ex: getStockPrice("GOOG") returns 939.78

    Use regex to first get LastTradePrice price line, then use regex again
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
    Return the stock exchange (as string) of the given stock ticker.
    Ex: getStockExchange("GOOG") returns NASDAQ

    Use regex to first get full Exchange line, then use regex again to
    only get the quoted Exchange, then a final time to strip quotes.
    '''
    try:
        company = json.dumps(getQuotes(tickerSymbol), indent = 2)
        rawExchangeData = re.search(re_StockExchangeRaw, company)
        stockExchangeRaw = re.search(re_StockExchange, rawExchangeData.group(0))
        stockExchange = re.search(re_QuoteTrimmer, stockExchangeRaw.group(0))

        print(tickerSymbol + " exchange: " + stockExchange.group(0))
        return stockExchange.group(0)
    except:
        print("Bad stock symbol, can't determine exchange.")

re_lastTradeTimeYearRaw = r'\d{4}-' # RegEx for line containing full year
re_lastTradeTimeYear = r'\d{4}' # RegEx for 4-digit year

def getLastTradeYear(tickerSymbol):
    '''
    Return the year (as string) the given stock was traded.
    Ex: getLastTradeYear("GOOG") returns 2017

    Use regex to first get full LastTradeDateTime line, then use regex again to
    only get the 4-digit year.
    '''
    try:
        company = json.dumps(getQuotes(tickerSymbol), indent = 2)
        lastTradeTimeYearRaw = re.search(re_lastTradeTimeYearRaw, company)
        lastTradeTimeYear = re.search(re_lastTradeTimeYear, lastTradeTimeYearRaw.group(0))

        return lastTradeTimeYear.group(0)
    except:
        print("Bad stock symbol, can't determine last trade time.")

re_LastTradeTimeRaw = r'Long": "[a-zA-Z]* \d+, [^a-z]*"' # RegEx for line containing date
re_lastTradeTimeDate = r'[A-Z][a-z]{2} \d{1,}' # RegEx for month and day

def getLastTradeDate(tickerSymbol):
    '''
    Return the month and day (as string) the given stock was traded.
    Ex: getLastTradeDate("GOOG") returns Jun 16

    Use regex to get full LastTradeDateTimeLong line, then use regex again to
    only get the month and day.
    '''
    try:
        company = json.dumps(getQuotes(tickerSymbol), indent = 2)
        rawTradeTime = re.search(re_LastTradeTimeRaw, company)
        lastTradeTimeDate = re.search(re_lastTradeTimeDate, rawTradeTime.group(0))

        return lastTradeTimeDate.group(0)
    except:
        print("Bad stock symbol, can't determine last trade date.")

re_lastTradeTimeHour = r'\d{1,}:\d{1,}[A-Z]{2} [A-Z]*' # RegEx for hour, AM/PM, time zone

def getLastTradeHour(tickerSymbol):
    '''
    Return the hour and time zone (as string) the given stock was traded.
    Ex: getLastTradeHour("GOOG") returns 4:00PM EDT

    Use regex to get full LastTradeDateTimeLong line, then use regex again to
    only get the hour, AM/PM, and time zone.
    '''
    try:
        company = json.dumps(getQuotes(tickerSymbol), indent = 2)
        rawTradeTime = re.search(re_LastTradeTimeRaw, company)
        lastTradeTimeHour = re.search(re_lastTradeTimeHour, rawTradeTime.group(0))

        return lastTradeTimeHour.group(0)
    except:
        print("Bad stock symbol, can't determine last trade hour.")
