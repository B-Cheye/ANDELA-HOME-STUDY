# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 07:46:50 2018

@author: User
"""

myList=[34,34,67,67,54,43,32,32,32,45]
processedList = [x for x in myList if myList.count(x)==1]
print(processedList)
print("First non-repeated character is: " +str(processedList[0]))