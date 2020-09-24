#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:24:16 2020

@author: prenaudin
"""

from scipy.io import wavfile
import numpy as np


delta = 44100 #fréquence d'échantillonnage

def s(t):                                           #le signal considéré
    return(np.sin(2*np.pi*440*t))

def u(v):
    return(int((255/2)*(v+1)))                      # fonction pour écrire des entiers de 0 à 255 (8 bits)
    
def remplissage_array():                              #fonction permettant de remplir un ndarray avec des entiers (sur 8 bits : np.int8)
                                                        #toutes les 44100 valeurs du signal
    data=np.ndarray((delta,),dtype=np.int8)
    for step in range(delta):                     # 44100 car on échantillonne que sur 1 seconde
        temps=step/delta
        signal=s(temps)
        data[step]=u(signal)
    return(data)
    
data=remplissage_array()    #ndarray rempli d'entiers

wavfile.write('la.wav',44100,data) #création du fichier wav 'la.wav', en fréquence 44100


