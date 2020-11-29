# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:10:24 2020

@author: NotYourPc
"""

from scipy.interpolate import interpld
import pandas as pd
import plotly.express as px
import numpy as np
df=pd.read_excel(r"")
list1 =df.cases.values.tolist()
#####making circle
m = interpld([1,max(list1)],[5,18])
circle_radius =(list1)
typelist= ['open-street-map','white-bg','carto-darkmatter','stamen-terrain','stamen-toner','stamen-watercolor']
##plotting heatmap

for i in typelist:
    print (i)
    fig = px.density_mapbox(df,lat='Lat', lon='Long', radius=circle_radius,zoom=0,mapbox_style=i)
    
fig.show()
 