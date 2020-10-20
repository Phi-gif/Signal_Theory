#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:04:40 2020

@author: prenaudin
"""

import numpy as np

#Question a

delta = 44100 #fréquence d'échantillonnage

def s(t):                                           #le signal considéré
    return(np.sin(2*np.pi*440*t))

def u(v):                                           #fonction codant le signal v=s(t) en nombre binaire sur 16 bits signés
    vol_zoom = (1/2)*(65535*v-1)
    return(int(vol_zoom).to_bytes(2,byteorder = 'little', signed=True))
 
#Question b
def echantillonnage():                              #fonction permettant de coder en bianire sur 16 bits signés toutes les 44100 valeurs du signal
    tab=[]
    for step in range(delta):                     # 44100 car on échantillonne que sur 1 seconde
        temps=step/delta
        signal=s(temps)
        tab.append(u(signal))
    return(tab)
        
#Question c
with open('la2.pcm','wb') as f:                      #écrit le fichier qui nous intéresse
    for i in echantillonnage():
        f.write(i)