# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 00:17:53 2019

@author: kruti
"""
"""
Given two lists Aand B, and B is an anagram of A.
We want to find an index mapping P, 
from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
"""
def anagramMappings(A: 'List[int]', B: 'List[int]') -> 'List[int]':
    op = []
    dict1 = {}
    for i,j in enumerate(B):
        dict1[j] = i
    for num in A:
        op.append(dict1[num])
    return op

anagramMappings([12, 28, 46, 32, 50],[50, 12, 32, 46, 28])