# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:12:36 2020

@author: Philippine
"""

import numpy as np
from numpy.fft import ifft


#Question 1

## on veut f = 50Hz pour un range de fréquence de 0 à 1000Hz
## Ca nous donne 20 fréquences réelles donc 41 fréquences complexes. N = 41
## et donc e = N*f = 41*50 = 2050 Hz

#Question 2

f = 50
l = 20

liste_freq = np.array([k*f for k in range(l+1)] + [k*f for k in range(-l,0)])
## rangées dans l'ordre f0,f1 ...,f20,-f20,-f19,....,-f1

#Question 3

## On cherche L telle que L*[a0, . . . , aN−1] = [b0, . . . , bN−1] avec bi = ai si la fréquence (réelle)
## est inférieure à 500 Hertzs et bi = 0 sinon.
## Donc on met des 1 dans L tant que |freq|<=500 Hz

L = np.zeros(2*l+1) # L est un filtre fréquentiel
for k in range(len(liste_freq)):
    if np.abs(liste_freq[k])<500:
        L[k]=1

print(L)

#Question 4

L_temp = (2*l+1)*ifft(L).real # on multiplie par N pour retrouver les conventions du cours
## filtre L mais du côté temporel

## Il suffit donc maintenant de convoluer un signal temporel échantillonné à 2050 Hz 
## avec un tel filtre pour ne conserver que les fréquences inférieures à 500 Hz.