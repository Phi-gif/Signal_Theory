#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:45:18 2020

@author: prenaudin
"""

#Ecriture du début de la comptine "Au clair de la Lune"
##Notes à produire : "do do ré mi do" pendant des durées respectives de [0.5,0.5,0.5,0.5,1,1].

from scipy.io import wavfile
import numpy as np

#Fréquence d'échantillonnage choisie
delta = 44100

#Fonction de recadrage choisie (16 bits signés)
def u(v):                                   
    return(int((1/2)*(65535*v-1)))   
    
#Différentes notes (basées sur le La440)
def do(t):
    return(np.sin(2*np.pi*440*2**(-9/12)*t))
    
def re(t):
    return(np.sin(2*np.pi*440*2**(-7/12)*t))
    
def mi(t):
    return(np.sin(2*np.pi*440*2**(-5/12)*t))
    
#Liste des durées de chaques notes
durees = [0.5,0.5,0.5,0.5,1,1]
sumcum_duree = np.cumsum(durees)  #somme cumulées pour l'intégrer plus facilement dans la def du signal
interlude = 1e-3
    
#Signal complet de la chanson
def signal(t):
    if 0<=t<=sumcum_duree[0]-interlude:              #retranche 1 interlude de quelques milliseconde pour bien entendre la séparation des notes
        return(do(t))
    if sumcum_duree[0]<=t<=sumcum_duree[1]-interlude:
        return(do(t))
    if sumcum_duree[1]<=t<=sumcum_duree[2]-interlude:
        return(do(t))
    if sumcum_duree[2]<=t<=sumcum_duree[3]-interlude:
        return(re(t))
    if sumcum_duree[3]<=t<=sumcum_duree[4]-interlude:
        return(mi(t))
    if sumcum_duree[4]<=t<=sumcum_duree[5]-interlude:
        return(do(t))
    else :
        return(0)                                       #mettre 0 ou autre chose ? crache sur mon ordi (essayer des fondues)
        
#Création du tableau de données        
def remplissage_array_chanson(sig,freq_ech,t,recadrage):
    data=np.ndarray((freq_ech*t,),dtype=np.int16)
    for step in range(freq_ech*t):                     
        temps=step/freq_ech
        signal=sig(temps)
        data[step]=recadrage(signal)
    return(data)
    
data_chanson = remplissage_array_chanson(signal,delta,int(sum(durees)),u)

#Ecriture du fichier son
wavfile.write('Comptine.wav',delta,data_chanson)

    
