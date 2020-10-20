#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:02:00 2020

@author: prenaudin
"""

#Question c
##Fonction renvoyant la liste des coefficients complexes ci associés aux coefs réels ai et bi du signal réel

def trigToExp(a,b):
    c = [(a[i]-1j*b[i])/2 for i in range(min(len(a),len(b)))]
    return(c)
    
#Question d
##Fonction renvoyant les listes des coefs réels ai et bi asscociés aux coefs complexes ci du signal exponentiel
    
def expToTrig(c):
    a=[2*c[i].real for i in range(len(c))]
    b=[-2*c[i].imag for i in range(len(c))]
    return(a,b)
    
