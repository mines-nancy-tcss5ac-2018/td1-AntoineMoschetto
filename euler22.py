# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:39:43 2018

@author: moschett4u
"""

lis=[]
"on extrait la liste de noms et on la trie"
for line in open('p022_names.txt', 'r'):
    lis.append(line)
    lis=str(lis)

liste=lis.split('","')
liste[0]='MARY'
liste[-1]='ALONSO'
listriee=sorted(liste)




def points(nom):
    "compte les points d'un nom"
    s=0
    for k in range(len(nom)):
        s+=ord(nom[k])-64
    return(s)
    
def solve(lis):
    "ajoute le multiplicateur de point et renvoie le resultat"
    s=0
    for k in range(len(lis)):
        s+=points(lis[k])*(k+1)
        
    return(s)
    
assert(points('COLIN')==53)
print("la solution du probleme euler 22 est", solve(listriee))