# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:42:22 2020

@author: Philippine
"""

#Question 1
import pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import dft
import numpy as np

data = pd.read_csv('meteo.csv').iloc[9::,1].reset_index(drop=True)

#On récupère les données sur "une période", cad 25 données (de minuit à minuit inclus)
data_9_nov = data.iloc[0:25,]

x = range(25)
y = [float(data_9_nov[i]) for i in range(len(data_9_nov))]
plt.scatter(x,y)
plt.plot(x,y, linewidth = 1)

#Question 2 

#on a choisi N=25, et e=1 mesure/h donc f= 1.1e-5 Hz (résolution fréquencielle)
#les fréquences complexes sont donc [-12f,...,-f,0,f,...,12f]


#on calcul les coefficients associés à ces fréquences

def MatriceFourrier(d):
    M = dft(d, scale = 'n')     #matrice de Fourier du cours
    N = np.conj(d*M)
    return(M,N)
    
M = MatriceFourrier(25)[0]
M_inv = MatriceFourrier(25)[1]

coefs = np.dot(M,y) #attention à l'ordre des coefs, le premier est c0 puis c1 jusqu'à c12 puis c-12 jusqu'à c-1
#on peut aussi les calculer avec (1/25)*fft(y)

#Question c

f = 1.1e-5
#on met les fréquences dans le même ordre que les coefficients
liste_freq = np.array([k*f for k in range(13)] + [k*f for k in range(-12,0)])
    
def temperature(t,coefficients):
    freq = 2*1j*np.pi*3600*t*liste_freq          #3600t car le t ici est en seconde et nous on veut des heures
    vect_exp = np.exp(freq)                      # freq = [2*i*pi*0f*t, 2*i*pi*f*t,....,2*i*pi*12f*t, -2*i*pi*12f*t, ..., -2*i*pi*f*t]
    valeurs = np.dot(coefficients,vect_exp)      # vect_exp  = [exp(2*i*pi*0f*t), exp(2*i*pi*f*t),....,exp(2*i*pi*12f*t), exp(-2*i*pi*12f*t), ..., exp(-2*i*pi*f*t)]
    signal_réel = np.real(valeurs)               # valeurs = c0exp(2*i*pi*0f*t) + c1......
    return(signal_réel)
    
#Question d

t = np.linspace(0, 25, 100)
signal=[temperature(u,coefs) for u in t]
valeurs_aux_points = [temperature(t,coefs) for t in x]

plt.scatter(x,y)
plt.scatter(x,valeurs_aux_points, c='r')
plt.plot(x,y, linewidth = 1)
plt.plot(t,signal, c='r')
plt.show()

#Question e

#filtre passe bas
def tempsLisse(t):
    coefs_modif = np.zeros(len(coefs), dtype = complex)
    coefs_modif[0:5] = coefs[0:5]
    coefs_modif[-4::] = coefs[-4::]
    return(temperature(t,coefs_modif))
    
signal_lisse = [tempsLisse(u) for u in t]
#valeurs_pts_lisse = [tempsLisse(t) for t in x]

plt.scatter(x,y)
plt.scatter(x,valeurs_aux_points, c='r')
#plt.scatter(x,valeurs_pts_lisse, c='g')
plt.plot(x,y, linewidth = 1)
plt.plot(t,signal, c='r')
plt.plot(t,signal_lisse, c='g')
plt.show()

#Question f : resamplage

new_x = np.arange(0,25,2/3)
valeurs_pts_lisse_40min = [tempsLisse(t) for t in new_x]

plt.scatter(x,y)
plt.scatter(x,valeurs_aux_points, c='r')
plt.scatter(new_x,valeurs_pts_lisse_40min, c='g')
plt.plot(x,y, linewidth = 1)
plt.plot(t,signal, c='r')
plt.plot(t,signal_lisse, c='g')
plt.show()