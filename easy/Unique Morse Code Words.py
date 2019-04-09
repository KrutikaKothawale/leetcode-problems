# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:06:50 2019

@author: kruti
"""

def uniqueMorseRepresentations(words: 'List[str]') -> 'int':

    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    d={}
    for i in range(len(a)):
        d[a[i]]=b[i]
    result={''.join(d[x] for x in word ) for word in words}
    return len(result)

uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])