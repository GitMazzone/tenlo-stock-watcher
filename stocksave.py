'''
Author: Michael Mazzone
Used: https://github.com/hongtaocai/googlefinance

Uses googstock.py methods to save formatted data to CSV for analysis.
Also uses schedule 0.4.3 to run at specified times.
'''

import csv
import datetime
import realtime
import re
import schedule
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

    tickerSymbolList is given as a list of strings, but must be converted to
    a list of lists for csv.writer
    Open or create new file, get the string stored in companies 2D list, use
    realtime.py to fill CSV with real time data
    '''
    date = datetime.date.today().strftime("%B %d %Y %I:%M")
    fileName = ""
    numCompanies = len(tickerSymbolList)
    companies = [[] for i in range(numCompanies)] # 2D list, list for each symbol

    # Fill companies (2D list) with company ticker symbols as lists
    for i in range(0, numCompanies):
        companies[i].append(tickerSymbolList[i])

    if fileType == "csv":
        fileName = date + ".csv"
    else:
        fileName = date + ".xlsx"

    with open(fileName, 'w') as outputFile:
        wr = csv.writer(outputFile, dialect='excel')
        wr.writerow(["Company", "Price", "Date", "Year", "Exchange"])
        ticker = ""
        for company in companies:
            ticker = company[0] # realtime takes a string from company list
            # writerow: each parameter is a column in a the current row written
            wr.writerow([
                ticker,
                realtime.getStockPrice(ticker),
                realtime.getLastTradeDate(ticker),
                realtime.getLastTradeYear(ticker),
                realtime.getStockExchange(ticker)
                ])
