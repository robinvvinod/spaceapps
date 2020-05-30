# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
#import re
#import xlrd as xl
#import math
import time
import datetime


warnings.filterwarnings('ignore')
start = time.time()
print datetime.datetime.fromtimestamp(start).strftime('%c')

def moving_average(a, n=7) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def InputFacebookData():
    #df = pd.read_excel("applemobilitytrends.xlsx")
    df = pd.read_csv('applemobilitytrends.csv')
    
    dates = list(df.columns)
    dates = dates[6:]
    dates.insert(0, 'Dates')
    #dates = np.array(dates)
    #dates['dates'] = dates
    
    
    df = df[df['country'] == 'United States']
    df = df[df['transportation_type'] == 'driving']
    df = df[df['geo_type'] == 'county']
    df = df[df['sub-region'] == 'New York']
    df = df.drop(columns=['geo_type', 'alternative_name', 'sub-region','country','transportation_type'])

    df = df.reset_index(drop=True)
     
    df2 = df.T
    
    df2.to_csv('applemobilitytrends2.csv', index=False, encoding='utf-8')
    #writer = pd.ExcelWriter('applemobilitytrends2.xlsx', engine='xlsxwriter')
    #df.to_excel(writer, sheet_name='Sheet1')
    #writer.save()
    return

def Graph():
    df = pd.read_csv('applemobilitytrends2.csv')
    df = df[['Date', 'Albany County']]
    data = np.array(df)
    axx = data[6:,0]
    axy = data[:,1]
    axy = moving_average(axy)
    #print len(axx), len(axy)
    fig1 = plt.figure(num=None, figsize=(8, 6), dpi=100, facecolor='w', edgecolor='k')
    plt.plot(axx,axy)
    ax = plt.axes()
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.xlabel(r'Date', fontsize = 20.0)
    plt.ylabel(r'Percentage (%)', fontsize = 20.0)
    plt.title(r'Driving in Albany County', fontsize = 20.0)
    fig1.tight_layout()
    plt.savefig('Albany County.png')
    plt.show()
    return


#InputFacebookData()
Graph()
    


end = time.time()
print(end - start), datetime.datetime.fromtimestamp(end).strftime('%c')