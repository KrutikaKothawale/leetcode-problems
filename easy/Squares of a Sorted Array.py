# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:36:17 2019

@author: kruti
"""

def sortedSquares(A: 'List[int]') -> 'List[int]':
    op = []
    for i in A:
        op.append(i*i)
    return sorted(op)


sortedSquares([-4,-1,0,3,10])