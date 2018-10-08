# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:38:26 2018

@author: moschett4u
"""
def inverser(n):
    "on cree le nombre renverse"
    chaine=str(n)
    lis=''
    for k in range(len(chaine)):
        lis+=chaine[len(chaine)-k-1]
    return(int(lis))
        
def solve(n):
    "on test si un nombre est de lychrels ou non"
    nb_test=0
    while nb_test<50 and n!=inverser(n):
        nb_test+=1
        n=n+inverser(n)
    if nb_test==50:
        return(False)
    else:
        return(True)
        
def final(n):
    "on test pour les n premiers nombres"
    nb=0
    for k in range(n):
        if solve(k)==True:
            nb+=1
    return(nb)
        
print("le nombre de nombre de lychrels est", final(10000))
        
