# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import warnings
#import re
#import xlrd as xl
#import math
import time
import datetime

print("L8r Sk8r")
warnings.filterwarnings('ignore')
start = time.time()
print datetime.datetime.fromtimestamp(start).strftime('%c')

def Graph():
    df = pd.read_excel("applemobilitytrends.xlsx")
    
    df = df[df['country'] == 'United States']
    df = df[df['transportation_type'] == 'driving']
    
    df.reset_index(drop=True)
    
    writer = pd.ExcelWriter('applemobilitytrends2.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    return

Graph()

end = time.time()
print(end - start), datetime.datetime.fromtimestamp(end).strftime('%c')
