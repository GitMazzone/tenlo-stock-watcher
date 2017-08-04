'''
Author: Michael Mazzone
Used: https://github.com/hongtaocai/googlefinance

Uses realtime.py methods to save formatted data to CSV or Excel for analysis.
Also uses schedule 0.4.3 to run at specified times.
'''

# TODO: Give csv and excel writing duties to own functions or file

import datetime
import re
import schedule
import stocksave
import time

def getMarketOpenOrClose(tickerSymbolList, openOrClose, fileType="csv"):
    '''
    Save stock info (name, price, date, year, exchange) of given stocks to CSV
    or Excel file (CSV by default). Data retrieved from market open or close.
    Ex: marketOpen(companies, "open", "excel") saves 'June 16, 2017 9:30AM' as:
        Name    Price   Date    Year    Exchange
        GOOG    939.78  Jun 16  2017    NASDAQ
        AAPL    142.27  Jun 16  2017    NASDAQ

    Ex: marketOpen(companies, "close") saves 'June 16, 2017 4:00PM' as:
    GOOG,939.78,Jun 16,2017,NASDAQ
    AAPL,142.27,Jun 16,NASDAQ
    '''

def getMarketLive(tickerSymbolList, fileType="csv"):
    '''
    Save stock info (name, price, date, year, exchange) of given stocks to CSV
    or Excel file (CSV by default). Data retrieved in real time.
    Ex: marketOpen(companies, "excel") saves 'June 16, 2017 9:45AM' as:
        Name    Price   Date    Year    Exchange
        GOOG    939.78  Jun 16  2017    NASDAQ
        AAPL    142.27  Jun 16  2017    NASDAQ

    Ex: marketOpen(companies, "close") saves 'June 16, 2017 3:00PM' as:
    GOOG,939.78,Jun 16,2017,NASDAQ
    AAPL,142.27,Jun 16,NASDAQ
    '''
    date = datetime.date.today().strftime("%B %d %Y %I:%M")
    fileName = ""

    if fileType == "csv":
        fileName = date + ".csv"
        stocksave.saveCSV(tickerSymbolList, fileName)

    else:
        fileName = date + ".xlsx"
        stocksave.saveExcel(tickerSymbolList, fileName)

getMarketLive(["GOOG", "AAPL", "AMZN"])
