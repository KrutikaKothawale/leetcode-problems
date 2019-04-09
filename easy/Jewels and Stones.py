# -*- coding: utf-8 -*-
"""
strings J representing the types of stones that are jewels, 
and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

Note: "a" is considered a different type of stone from "A".
"""

"""
Created on Sun Feb 17 10:41:59 2019

@author: kruti
"""

def numJewelsInStones(J, S):
    total = 0
    for i in S:
        for j in J:
            if j == i :
                total += 1
    return total


numJewelsInStones('aA','aAAbbbb')