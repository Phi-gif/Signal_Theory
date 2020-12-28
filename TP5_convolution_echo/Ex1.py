# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:39:32 2020

@author: Philippine
"""

import numpy as np
from scipy.io import wavfile

#Question 1

## f(x) = x pour tout x dans [0,10]
##      = 0 sinon
## Donc on obtient la liste suivante pour f : np.arange(11)

f1 = np.arange(11)

##Convolution de f1 par elle même
convol_f1 = np.convolve(f1,f1)


#Question 2

## f(x) = x pour tout x dans [-5,5]
##      = 0 sinon
## Donc on obtient la liste suivante pour f : np.arange(-5,6)
## g(x) = pour tout x dans [8,10]
##      = 0 sinon
## Donc on obtient la liste suivante pour g : np.arange(8,11)

f2 = np.arange(-5,6)
g2 = np.arange(8,11)

##Convolution de f2 par g2
convol_f2g2 = np.convolve(f2,g2)
##Or comme x de f commence à -5 et x de g commence à 8, le premier chiffre -40 que l'on
##obtient correspond en fait à f(3), donc on rajoute 3 zéros au début du résultat qu'on 
##obtient pour être cohérents avec les conventions qui prennent x = 0 comme premier indice

convol_f2g2 = list(np.zeros(3)) + list(convol_f2g2)

#Question 3

wav_file = 'touche43.wav'
samplerate, data = wavfile.read(wav_file) 

##samplerate = 44100 Hz
##data est bien de taille 21554 et en int16

#Question 4
##Construction du ndarray u

u = np.zeros(100001) #de type float64
for i in range(1,len(u)):
    if i%20000 == 0:
        u[i] = (20000/i)**2
        
conv = np.convolve(data,u) #conv de type float64 avec 121554 valeurs

#Question 5 
M_obs = max(conv)
m_obs = min(conv)

def normalisation(maxi,mini,v):
    a = 2/(maxi - mini)
    b = -(a/2)*(mini + maxi)
    return(np.float32(a*v+b))
    

##normalisation de conv pour passer en float32 signés

tableau = []
for i in range(len(conv)):
    tableau.append(normalisation(M_obs,m_obs,conv[i]))

conv_norm = np.array(tableau,dtype=np.float32)

##avec le type ndarray
conv_norm_bis = np.ndarray((len(conv),),dtype = np.float32)
for i in range(len(conv)):
    conv_norm_bis[i] = normalisation(M_obs,m_obs,conv[i])
    
#Question 6
    
wavfile.write('touche43echo.wav',samplerate,conv_norm)
wavfile.write('touche43echobis.wav',samplerate,conv_norm_bis)

