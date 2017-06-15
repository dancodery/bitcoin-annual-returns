"""

This simple Python script shows the annual bitcoin price performance. 

The average price is determined each year. 
For the performance the average price of the current year is divided by the average price of the last year.
The last row shows the average percentage change per year (performance).

__author__ = "Daniel Gockel"
__copyright__ = "Copyright 2017"
__email__ = "daniel@gockel.co"
"""

import urllib2

url = "https://blockchain.info/charts/market-price?showDataPoints=false&timespan=all&show_header=true&daysAverageString=1&scale=0&format=csv&address="

stream = urllib2.urlopen(url).read()

with open('btcdata.csv','w') as f:
    f.write(stream)

def getdatatable():
    with open('btcdata.csv','r') as file:
        lines = file.readlines()
    return lines

def average_price(list):
    return (sum(list) / len(list))

datatable = getdatatable()
count = 0
first_day = ''
current_year = ''
years_prices = list()
returns_list = list()
last_average = None
firstyear = True
print '** Bitcoin yearly performance **'
print 'year .. price end of year .. avg for year .. performance'
for line in datatable:
    line = line.replace('\n','')
    datetime, price = line.split(',')
    date = datetime.split(' ')[0]
    price = float(price)

    if price == 0.0: continue
    if(not first_day):
        first_day = date
    y, m, d = date.split('-')

    if(not current_year):
        current_year = y
    years_prices.append(price)
    count+=1

    if current_year != y: 
        years_average = average_price(years_prices[:-1])
        increase = 0
        if last_average != None:
            increase = (years_average / last_average) - 1
            returns_list.append(increase)
            last_average = years_average
        else:
            last_average = years_average
        print current_year, '  ', format(years_prices[-2], '.6f'), '            ', round(years_average,3), '  ', round(increase,3)
        current_year = y
        years_prices = [years_prices[-1]]

years_average = average_price(years_prices)
increase = (years_average / last_average) - 1
returns_list.append(increase)
print current_year, '  ', format(years_prices[-1], '.6f'), '            ', round(years_average,3), '  ', round(increase,3)

average_returns = average_price(returns_list)
print 'total days: ',count
print 'first day: ', first_day
print 'last day: ', date
print 'average return per year: ', round(average_returns  * 100, 5) , '%';