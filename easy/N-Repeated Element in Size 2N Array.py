# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:48:45 2019

@author: kruti
"""
"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
"""

def repeatedNTimes(A: 'List[int]') -> 'int':
    for i in A:
        if A.count(i) > 1:
            return i

repeatedNTimes([1,2,3,3])