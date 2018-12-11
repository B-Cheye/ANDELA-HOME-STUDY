# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 07:36:24 2018

@author: User
"""
def firstNonRep(list1):
    count = {}
    for c in list1:
        if c not in count:
            count[c] = 0
        count[c] += 1
    for c in list1:
        if count[c] == 1:
            print(c)
list1 = [34,67,67,54,43,32,32,32,45]       
firstNonRep(list1)