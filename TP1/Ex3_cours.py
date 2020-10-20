#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:13:20 2020

@author: prenaudin
"""


import numpy as np

#Question a

delta = 44100                                       #fréquence d'échantillonnage

def s1(t):                                           #le premier signal considéré
    return(np.sin(2*np.pi*440*t))

def s2(t):                                           #le premier signal considéré
    return((1/2)*np.sin(2*np.pi*660*t))
    

def u(v,maximum,minimum):                                           #fonction codant le signal v=s(t) en nombre binaire sur 8 bits (version automatique)
    vol_zoom = (255/(maximum-minimum))*(v-minimum)
    return(int(vol_zoom).to_bytes(1,byteorder = 'little',signed=False))
 
#Question b
def echantillonnage():                              #fonction permettant de coder en binaire sur 8 bits toutes les 44100 valeurs des deux signaux
    tab_g=[]                                        #tableau pour l'oreille gauche
    tab_d=[]                                        #tableau pour l'oreille droite
    tab=[]
    signaux_1=[]
    signaux_2=[]
    for step in range(delta):                     # 44100 car on échantillonne que sur 1 seconde
        temps=step/delta
        signal_1=s1(temps)
        signal_2=s2(temps)
        signaux_1.append(signal_1)
        signaux_2.append(signal_2)
    minimum_1=min(signaux_1)                        #calcul du min et du max des deux signaux pour pouvoir calculer la fonction g
    maximum_1=max(signaux_1)
    minimum_2=min(signaux_2)
    maximum_2=max(signaux_2)
    for signal in signaux_1:                            #remplissage des deux tableau
        tab_g.append(u(signal,maximum_1, minimum_1))
    for signal in signaux_2:
        tab_d.append(u(signal,maximum_2, minimum_2))
    for i in range(len(tab_g)):                         #remplissage du tableau final
        tab.append(tab_g[i])
        tab.append(tab_d[i])
    return(tab)
        
#Question c
with open('stéréo_cours.pcm','wb') as f:                      #écrit le fichier qui nous intéresse
    for i in echantillonnage():
        f.write(i)