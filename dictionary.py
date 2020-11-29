# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:48:40 2020

@author: Subarna Basnet
"""

#D={'username':'subarna','online': True,'followers': 987}
#print(D.keys())
#print(D.values())
#print(D.items())


"""wap to enter the detail of student and by using dictionary access the third and fifth element stored in the dictionary .and also check any specific key exits in the dictionary or not //using values keys and both + """

s={'system ID':'2019008144','Roll No':'190101306','Name':'Subarna Basnet','Branch':'B-Tech CSE'}
"""keys"""
#print(s.keys())
"""" Code to print Values"""
#print(s.values())
""""code to print Items"""
#print(s.items())
"""code to print data from key with the help of get"""
#print('Sytem ID:',s.get('system ID'))
#print('Name:',s.get('Name'))
#print('Roll No:',s.get('Roll No'))
#print('Branch:',s.get('Branch'))
"""Code to display value from keys"""
#key=list(s.keys())
#value=list(s.values())
#print(key[0])
#print(value[0])
#print(key[1])
#print(value[1])
#print(key[2])
#print(value[2])
#print(key[3])
#print(value[3])
"""Code to clear dictionary"""
#s.clear()
#print('data =',s)
"""to Copy dictionary"""
#copy= s.copy()
#print('Copied=',copy)
"""from keys"""
#vowels =dict.fromkeys(s)
#print(vowels)

a=input('Enter number')
b=len(a)
print(b)



