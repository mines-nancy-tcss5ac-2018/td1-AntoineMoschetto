# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:18:01 2018

@author: moschett4u
"""

def solve(n):
    "solve the 16th Euler problem."
    chaine=str(2**n)
    somme=0
    for k in range(len(chaine)):
        somme+=int(chaine[k])
        
    return somme
    
    
    


assert(solve(15)==26)
print("la solution au probleme 16 est", solve(1000))