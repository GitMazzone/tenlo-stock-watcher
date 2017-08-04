'''
Author: Michael Mazzone

Functions for writing data to CSV or Excel files
'''

import csv
import realtime
import xlsxwriter

# TODO: Append to end of existing CSV file
def saveCSV(tickerSymbolList, fileName):
    '''
    tickerSymbolList is given as a list of strings, but must be converted to
    a list of lists for csv.writer
    Open or create new file, get the string stored in companies 2D list, use
    realtime.py to fill CSV with real time data
    '''
    numCompanies = len(tickerSymbolList)
    companies = [[] for i in range(numCompanies)] # 2D list, list for each symbol

    # Fill companies (2D list) with company ticker symbols as lists
    for i in range(0, numCompanies):
        companies[i].append(tickerSymbolList[i])

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

def saveExcel(tickerSymbolList, fileName):
    numCompanies = len(tickerSymbolList)

    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Name', bold)
    worksheet.write('B1', 'Price', bold)
    worksheet.write('C1', 'Date', bold)
    worksheet.write('D1', 'Year', bold)
    worksheet.write('E1', 'Exchange', bold)

    worksheet.set_column('C:C', 20) # Widen date column for legibility

    for company in companies:
        ticker = company[0]
