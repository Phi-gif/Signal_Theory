#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:22:45 2020

@author: prenaudin
"""

from scipy.io import wavfile
import numpy as np

#Question a

delta = 44100                                       #fréquence d'échantillonnage

def s(t):                                           #le signal considéré (sol un ton plus bas que le La440)
    return(np.sin(2*np.pi*440*2**(-1/6)*t))

def u(v):
    return(int((1/2)*(65535*v-1)))                      # fonction pour écrire des entiers de -32768 à 32767 (16 bits signés)
    
def remplissage_array_mono(sig,t,recadrage):                              #fonction permettant de remplir un ndarray avec des entiers (sur 16 bits signés: np.int16)
                                                           #toutes les 44100*t valeurs du signal car on veut jouer le son pendant t secondes
    data=np.ndarray((delta*t,),dtype=np.int16)
    for step in range(delta*t):                     # 44100*t car on veut jouer le son pendant t secondes
        temps=step/delta
        signal=sig(temps)
        data[step]=recadrage(signal)
    return(data)
    
data_mono=remplissage_array_mono(s,3,u)                    #ndarray rempli d'entiers en 1D car veut jouer en mono (3 secondes)

wavfile.write('Sol.wav',delta,data_mono)            #création du fichier wav 'Sol.wav', en fréquence d'échantillonage de 44100

#Question b

def s1(t):                                          #La440
    return(np.sin(2*np.pi*440*t))
    
def s2(t):                                          #Si un ton plus haut que le La440
    return(np.sin(2*np.pi*440*2**(1/6)*t))
    
def remplissage_array_stereo(sig1,sig2,t,recadrage):                              #fonction permettant de remplir un ndarray avec des entiers (sur 16 bits signés: np.int16)
                                                           #toutes les 44100*t valeurs du signal, en 2D car veut jouer en stéréo
    data=np.ndarray((delta*t,2),dtype=np.int16)
    for step in range(delta*t):                             # 44100*t car on veut jouer le son pendant t secondes
        temps=step/delta
        signal_1=sig1(temps)
        signal_2=sig2(temps)
        data[step,0]=recadrage(signal_1)
        data[step,1]=recadrage(signal_2)
    return(data)
    
data_stereo=remplissage_array_stereo(s1,s2,3,u)                    #ndarray rempli d'entiers en 2D car veut jouer en stéréo

wavfile.write('LaSi.wav',delta,data_stereo)
    
#Question c

def s_mix(t):
    return(s1(t)+s2(t))
    
def u_mix(v,maximum, minimum):
    a =((2**16)-1)/(maximum-minimum)
    b = -(a/2)*(maximum+minimum)-1/2
    return (int(a*v+b))        

def remplissage_array_mix_mono(sig,t,recadrage):
    data=np.ndarray((delta*t,),dtype=np.int16)
    signaux = []
    for step in range(delta*t):                     
        temps=step/delta
        signal=sig(temps)
        signaux.append(signal)
    minimum=min(signaux)
    maximum=max(signaux)
    i=0
    for signal in signaux:
        data[i]=recadrage(signal,maximum, minimum)
        i+=1
    return(data)

data_mix_mono = remplissage_array_mix_mono(s_mix,3,u_mix)

wavfile.write('LaSiMono.wav',delta,data_mix_mono)       #création du fichier wav 'LaSiMono.wav', en fréquence 44100, pendant 2 secondes

#Question d

def u_mix2(v,maximum, minimum):
    a =((2**16)-1)/(maximum-minimum)
    b = -(a/2)*(maximum+minimum)-1/2
    return (int((1/2)*(a*v+b)))                         #change ici les nombres entier à coder sinon dans le signal ne marche pas à cause de la façon dont on l'a codé
    
data_mix_mono_less = remplissage_array_mix_mono(s_mix,3,u_mix2)

wavfile.write('LaSiMonoPasFort.wav',delta,data_mix_mono_less)
    