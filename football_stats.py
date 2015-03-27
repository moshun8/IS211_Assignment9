#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Beautiful Soup'''

import urllib2
from bs4 import BeautifulSoup

URL = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2014-season-regular-category-touchdowns'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)

def tdStats():
    tdList = []
    topTD = SOUP.find('table', {'class': 'data'})
    rows = topTD.findAll('tr')

    for row in rows[3:23]:
        try:
            cells = row.find_all('td')
            name = cells[0].get_text()
            position = cells[1].get_text()
            team = cells[2].get_text()
            numTD = cells[6].get_text()
            tdList.append([name, position, team, numTD])
        except:
            print "bad cell"
            continue
    print tdList

tdStats()
