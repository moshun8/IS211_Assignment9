#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Stock Stats'''

import urllib2
from bs4 import BeautifulSoup

# if the user wanted to pick the stock to scrape:
# pickStock = raw_input('Pick a 4 letter stock code: ')
# URL = 'http://finance.yahoo.com/q/hp?s=' + pickStock + '+Historical+Prices'
# or do an argparse on the command line

URL = 'http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)

def stockPrices():
    stockData = []
    stockInfo = SOUP.find('table', {'class': 'yfnc_datamodoutline1'})
    rows = stockInfo.findAll('tr')

    for row in rows:
        try:
            cells = row.find_all('td')
            date = cells[0].get_text()
            close = cells[4].get_text()
            stockData.append({date: close})
            # chose a list with dicts so it's more easily 
            # searchable by date
        except:
            print "bad cell"
            continue
    print stockData[1:]

stockPrices()