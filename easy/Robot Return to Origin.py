# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:59:09 2019

@author: kruti
"""

"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. 
Given a sequence of its moves, 
judge if this robot ends up at (0, 0) after it completes its moves.
back to origin  return true. Otherwise, return false.
Inputs can be U / D / L / R
"""

def judgeCircle(moves: 'str') -> 'bool':
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

judgeCircle("UDDU")