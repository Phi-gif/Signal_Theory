# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np

#Question a

delta = 44100                                       #fréquence d'échantillonnage

def s(t):                                           #le signal considéré (La 440Hz)
    return(np.sin(2*np.pi*440*t))

## Fonction codant le signal v=s(t) en nombre binaire sur 8 bits non signés
## attention : fonction à modifier à chaque mode d'encodage différent
def u(v):                                           
    vol_zoom = (255/2)*(v+1)                        
    return(int(vol_zoom).to_bytes(1,byteorder = 'little',signed=False))
 
#Question b
## Fonction permettant de coder en binaire sur 8 bits non signé toutes les 44100 valeurs du signal
def echantillonnage(time, freq_ech):                              
    tab=[]
    for step in range(time*freq_ech):                       #time pour modifier la durée du son
        temps=step/freq_ech
        signal=s(temps)
        tab.append(u(signal))                       #on rempli le tableau des 44100 nombres en binaire
    return(tab)
        
data = echantillonnage(1, delta)

#Question c
with open('la.pcm','wb') as f:                      #écrit le fichier qui nous intéresse au format pcm
    for i in data:
        f.write(i)

