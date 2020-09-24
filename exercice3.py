# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np

#Question a

delta = 44100                                   #fréquence d'échantillonnage

def s(t):                                           #le signal considéré (La 440Hz)
    return(np.sin(2*np.pi*440*t))

def u(v):                                           #fonction codant le signal v=s(t) en nombre binaire sur 8 bits non signés
    vol_zoom = (255/2)*(v+1)                        #fonction à modifier à chaque mode d'encodage différent
    return(int(vol_zoom).to_bytes(1,byteorder = 'little',signed=False))
 
#Question b
def echantillonnage():                              #fonction permettant de coder en binaire sur 8 bits non signé toutes les 44100 valeurs du signal
    tab=[]
    for step in range(44100):                     # 44100 car on échantillonne que sur 1 seconde
        temps=step/delta
        signal=s(temps)
        tab.append(u(signal))                       #on rempli le tableau des 44100 nombres en binaire
    return(tab)
        
#Question c
with open('la.pcm','wb') as f:                      #écrit le fichier qui nous intéresse au format pcm
    for i in echantillonnage():
        f.write(i)

