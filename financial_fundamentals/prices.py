'''
Created on Jul 2, 2013

@author: akittredge
'''


from pandas.io.data import get_data_yahoo
import datetime
import numpy as np
import pytz

def get_prices_from_yahoo(symbol, dates, type_of_price='Adj Close'):
    '''Yields date, value pairs.'''
    start = min(dates)
    end = max(dates)
    prices = get_data_yahoo(name=symbol, start=start, end=end)
    for date_price in prices.iterrows():
        date = datetime.datetime(date_price[0].year,
                                      date_price[0].month,
                                      date_price[0].day,
                                      tzinfo=pytz.UTC)
        yield date, np.float(date_price[1][type_of_price])