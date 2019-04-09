# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:33:59 2019

@author: kruti
"""

def diStringMatch(S: 'str') -> 'List[int]':
    i=0
    j=len(S)
    ans=[]
       
    for x in S:
        if x=='I':
            ans.append(i)
            i+=1
        else:
            ans.append(j)
            j-=1
               
    ans.append(j if S[-1]=='D' else i) #last element
    return ans

diStringMatch("IDID")