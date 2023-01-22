
import matplotlib.pyplot as plt
import numpy as np
import urllib.request as urq
import matplotlib.dates as mdates
import requests


def bytespdate2num(fmt, encoding='utf-8'):
    def bytesconverter(b):
        s = b.decode(encoding)
        return (mdates.datestr2num(s))
    return bytesconverter

def graph_data():

    stock_price_url='https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urq.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Volume' not in line:
                stock_data.append(line)

    datep, openp, highp, lowp, closep, ad_closep, vol = np.loadtxt(stock_data,
                                                                  delimiter=',',
                                                                  unpack=True,
                                                                  converters={0:bytespdate2num('%Y-%m-%d')}
                                                                  )

    plt.plot_date(datep, closep, '-', label='Price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

graph_data()