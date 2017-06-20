'''
Author: Michael Mazzone
Used: https://github.com/hongtaocai/googlefinance

Uses googstock.py methods to save formatted data to CSV for analysis.
Also uses schedule 0.4.3 to run at specified times.
'''

import csv
import realtime
import re
import schedule
import time

def marketOpen(tickerSymbolList, fileType="csv"):
    '''
    Save stock info (name, price, date, year, exchange) of given stocks to CSV
    or Excel file (CSV by default).
    Ex: marketOpen(companies, "excel") saves as
        Name    Price   Date    Year    Exchange
        GOOG    939.78  Jun 16  2017    NASDAQ
        AAPL    142.27  Jun 16  2017    NASDAQ

    Ex: marketOpen(companies) saves as
    GOOG,939.78,Jun 16,2017,NASDAQ
    AAPL,142.27,Jun 16,NASDAQ
    '''
    # TODO
