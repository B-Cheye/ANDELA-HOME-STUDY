# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:20:06 2018

@author: Cheye
"""
import random
import time
responces = ["Just read more","Not so sure","Most Likely","Absolutely not",
             "Outlook is Good","I see Things Happening","Never","Negative",
             "Could Be","Unclear","Ask again","Yes","No","Possible, but not probable",
             "It doesnt matter","Are you sure you want me to answer that?"]
def answerQuery():
    input("Ask and you shall receive: ")
    print("Let me dive deep into the waters of life, and find your answer")
    time.sleep(3)
    print("Hmmmmm!!!,,")
    time.sleep(2)
    print(random.choice(responces))
    print("\n")
answerQuery()

secondQuestion = (input("Would you like to ask the wise one another question? Y/N: "))
while secondQuestion == str("Y"):
    answerQuery()
    secondQuestion = (input("Would you like to ask the wise one another question? Y/N: "))
else:
    print(input("Press any key to exit"))