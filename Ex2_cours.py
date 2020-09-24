#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:30:10 2020

@author: prenaudin
"""

import numpy as np

#Question a

delta = 44100                                   #fréquence d'échantillonnage

def s1(t):                                           #le premier signal considéré
    return(np.sin(2*np.pi*440*t))

def s2(t):                                           #le deuxième signal considéré
    return((1/2)*np.sin(2*np.pi*660*t))
    
def s(t):                                           #le signal final
    return(s1(t)+s2(t))

def u(v,maximum,minimum):                           #fonction codant le signal v=s(t) en nombre binaire sur 8 bits 
    vol_zoom = (255/(maximum-minimum))*(v-minimum)  #non signé en tenant compte des nouvelles bornes de s(t)
    return(int(vol_zoom).to_bytes(1,byteorder = 'little',signed=False))
 
#Question b
def echantillonnage():                            #fonction permettant de coder en bianire sur 8 bits toutes les 44100 valeurs du signal
    tab=[]                                          #en tenant compte du min et du max du signal s(t)
    signaux=[]
    for step in range(delta):                     # 44100 car on échantillonne que sur 1 seconde
        temps=step/delta
        signal=s(temps)
        signaux.append(signal)
    minimum=min(signaux)
    maximum=max(signaux)
    for signal in signaux:
        tab.append(u(signal,maximum, minimum))
    return(tab)
        
#Question c
with open('la_cours.pcm','wb') as f:                      #écrit le fichier qui nous intéresse
    for i in echantillonnage():
        f.write(i)