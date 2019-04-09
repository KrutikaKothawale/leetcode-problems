# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:19:44 2019

@author: kruti
"""

def toLowerCase(str: 'str') -> 'str':
    output = ""
    for i in str:
        if ord(i) >= 65 and ord(i)<= 90:
            output += chr(ord(i)+32)
            print(output)
        else:
            output +=i
    return output

toLowerCase("Hello")