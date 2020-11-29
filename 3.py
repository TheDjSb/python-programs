# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:14:12 2020

@author: NotYourPc
"""

import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)