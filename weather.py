#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Weather

Instructions:
1. Display the actual temperatures for the days of the month that have passed
2. Display the forcasted temperatures for the days of the month that have not yet passed

'''

import urllib2
from bs4 import BeautifulSoup


URL = 'http://www.wunderground.com/history/airport/KNYC/2015\
/3/1/MonthlyCalendar.html'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)

def weatherTemps():
    weatherData = []
    weatherInfo = SOUP.find_all('table', class_='dayTable')
    date = None
    for info in weatherInfo:
        try:
            if date == None:
                date = info.find('a', class_='dateText').text.strip()
                continue
            header = info.find('td', class_='value-header',
                text=['Actual:', 'Forecast:'])

            if header != None:
                high = info.find('span', class_='high').text
                low = info.find('span', class_='low').text
                weatherData.append({
                    'date': date,
                    'header': header.text,
                    'high': high,
                    'low': low
                    })
            date = None
        except:
            print 'error'
            continue

    for dateInfo in weatherData:
        print dateInfo['date'] + '  '\
        + dateInfo['header'] + '  '\
        + dateInfo['high'] + '  '\
        + dateInfo['low']

weatherTemps()