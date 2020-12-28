# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:33:17 2020

@author: Philippine
"""
import numpy as np
from numpy.fft import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt

#Question 1 et 2

wav_file = 'touche43.wav'
samplerate, data = wavfile.read(wav_file) 

x = range(np.shape(data)[0])
#plt.bar(x,data)
plt.plot(x,data)

#Question 3

coefs = fft(data[:21553]) #u de l'énoncé (pas obligé de normaliser par n car on ne s'en sert pas dans la suite)
##on obtient 21553 coeficients rangés de c0 c1 .. ck c-k ... c-1

#Question 4

## Il faut trouver la fréquence f commune à toutes les autres fréquences : 
## N = 21553, e = 44100 donc f = e/N = 44100/21553
## on veut les fréquences non pas de la plus petite à la plus grande mais rangées comme les coefficients 
## au dessus

f = 44100/21553
l = int((21553-1)/2)

freq = np.array([k*f for k in range(l+1)] + [k*f for k in range(-l,0)])

#Question 5

plt.plot(freq, np.abs(coefs))
##apparement la fréquence du fondamental est autour de 320 Hz (faudrait pouvoir Zommer)

#Question 6

##Si on veut zoomer sur le fondamental, on ne va s'intéresser qu'à l'intervalle 200-400Hz.
##Il faut donc récupérer les indices des fréquences correspondantes

ind200_400 = np.where((200 <= freq) == (freq <= 400))[0]

freq_zoom = freq[ind200_400]
coefs_zoom = coefs[ind200_400]

plt.plot(freq_zoom,np.abs(coefs_zoom))

u_max = max(np.abs(coefs_zoom))
coef_max = np.where(np.abs(coefs_zoom) == u_max)[0]
freq_max = freq_zoom[coef_max]







