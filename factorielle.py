# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 19:07:44 2025

@author: LOUKMANE
"""

import numpy as np
def fact(N):
   if(N==0 or N==1):
      return 1
   else:
    F=N*fact(N-1)
    return F
N=int(input("donner un nombre:"))
F=fact(N)
print("le factorielle est:",F)

    
    