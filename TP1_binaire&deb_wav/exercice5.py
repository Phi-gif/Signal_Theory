#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:24:16 2020

@author: prenaudin
"""

from scipy.io import wavfile
import numpy as np


delta = 44100                                       #fréquence d'échantillonnage

def s(t):                                           #le signal considéré
    return(np.sin(2*np.pi*440*t))

## Fonction de recadrage pour écrire des entiers de 0 à 255 (8 bits non signés) et non plus des nombres binaires
def u(v):
    return(int((255/2)*(v+1)))                      # fonction pour écrire des entiers de 0 à 255 (8 bits)
    
## Fonction permettant de remplir un ndarray avec des entiers (sur 8 bits : np.int8) 
## toutes les 44100 valeurs du signal (1s)
def remplissage_array(time, freq_ech):                              
    data=np.ndarray((time*freq_ech,),dtype=np.int8)
    for step in range(time*freq_ech):                     
        temps=step/freq_ech
        signal=s(temps)
        data[step]=u(signal)
    return(data)
    
data=remplissage_array(2, delta)    #ndarray rempli d'entiers

wavfile.write('la.wav',delta,data) #création du fichier wav 'la.wav', en fréquence 44100


