#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:02:00 2020

@author: prenaudin
"""

#Question c
##Fonction renvoyant la liste des coefficients complexes ci associés aux coefs réels ai et bi du signal réel
#dans l'ordre qui nous arrange pour Fourier (c0,c1...,c100,c-100,....,c-1)

def trigToExp(a,b):
    #a[0]+b[0] = constante (on considère b[0]=0)
    c = [(a[i]-1j*b[i])/2 for i in range(1,len(a))]
    d = [(a[i]+1j*b[i])/2 for i in range(1,len(b))][::-1]
    c0 = a[0]
    coefs_complex = [c0] + c + d
    return(coefs_complex)
    
#Question d
##Fonction renvoyant les listes des coefs réels ai et bi associés aux coefs complexes ci du signal exponentiel
##En considérant que les coefs ci sont rangés dans l'ordre habituel (cf ci dessus)
    
def expToTrig(coefs_complex):
    n = len(coefs_complex)
    c = coefs_complex[0:((n+1)//2)]
    a = [c[0]]
    b = [0]
    for i in range(1,len(c)):
        a.append(2*c[i].real)
        b.append(-2*c[i].imag)
    return(a,b)
    