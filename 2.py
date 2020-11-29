# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:10:45 2020

@author: NotYourPc
"""

from datetime import datetime
date_object = datetime.strptime('Apr 19 2020 1:14PM', '%b %d %Y %I:%M%p')

print("String to Datetime :",date_object)