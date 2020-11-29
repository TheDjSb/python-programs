# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 03:28:16 2020

@author: Subarna Basnet
"""
"""39.	Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
"""

word = {'right':'left','up':'down','good':'bad','cool':'hot','east':'west'}
print ("Enter any word from following words")
for i in word.keys():
	print (i)
user_input = input()
if word.get(user_input):
	print ("Antonym of",user_input,"is",word[user_input])
else:
	print ("Enter correct input")