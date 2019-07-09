# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:59:51 2018

@author: Brian
"""

def Range(list1): 
    largest = list1[0] 
    largest2 = list1[0] 
    lowest = list1[0] 
    lowest2 = list1[0] 
    for item in list1:        
        if item > largest:  
            largest = item 
        elif largest2!=largest and largest2 < item: 
                largest2 = item 
        elif item < lowest: 
            lowest = item 
        elif lowest2 != lowest and lowest2 > item: 
            lowest2 = item 
              
    print("Largest element is:", largest) 
    print("Smallest element is:", lowest) 
    print("Second Largest element is:", largest2) 
    print("Second Smallest element is:", lowest2) 
  
# Driver Code 
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4] 
Range(list1) 