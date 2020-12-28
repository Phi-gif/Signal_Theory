#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:04:40 2020

@author: prenaudin
"""

import numpy as np

#Question a

delta = 44100                                       #fréquence d'échantillonnage

def s(t):                                           #le signal considéré
    return(np.sin(2*np.pi*440*t))

## Fonction codant le signal v=s(t) en nombre binaire sur 16 bits signés, convention little endian
def u(v):                                           
    vol_zoom = (1/2)*((2**16-1)*v-1)
    return(int(vol_zoom).to_bytes(2,byteorder = 'little', signed=True))
 
#Question b
## Fonction permettant de coder en binaire sur 16 bits signés toutes les 44100 valeurs du signal (1s)
def echantillonnage(time, freq_ech):                              
    tab=[]
    for step in range(time*freq_ech):                     
        temps=step/freq_ech
        signal=s(temps)
        tab.append(u(signal))
    return(tab)
        
data = echantillonnage(1, delta) #on joue le son sur 1 seconde

#Question c
with open('la2.pcm','wb') as f:                      #écrit le fichier qui nous intéresse
    for i in data:
        f.write(i)