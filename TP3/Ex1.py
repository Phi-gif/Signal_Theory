# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Fonction permettant de calculer les valeurs d'un signal quand on lui passe les coefficients et les fréquences en entrée

import numpy as np

def evalPolyTrigo(coefs,freq,a,t):
    fonction = 0
    n = len(coefs)
    f = []
    for k in range(a,a+n):
        f.append(k*freq)
    for i in range(a,a+n):
        fonction+= coefs[i-a]*np.exp(2*1j*np.pi*f[i-a]*t)
    return(fonction)
    
test = evalPolyTrigo([1],1,1,1) #test en t = 1 pour a = 1, c0 = 1 et f = 1 --> doit retourner 1