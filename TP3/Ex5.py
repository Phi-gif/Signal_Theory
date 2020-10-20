# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
from scipy.linalg import dft

d = 7

#signal 'réel'
def signal(t):
    return(2*np.cos(500*np.pi*t)+10*np.cos(1000*np.pi*t)+3*np.sin(1500*np.pi*t)+200)

#signal avec exp complexes
def signal2(t):
    return(200 + np.exp(-500*1j*np.pi*t) + np.exp(500*1j*np.pi*t) + 5*np.exp(-1000*1j*np.pi*t) + 5*np.exp(1000*1j*np.pi*t) + (3*1j/2)*np.exp(-1500*1j*np.pi*t) + (-3*1j/2)*np.exp(1500*1j*np.pi*t))
    
#remplissage du vecteur des valeurs de s
v = [signal(0)]
v2 = [signal2(0)]
for i in range(1,d):
    v.append(signal(i/(d*250)))
    v2.append(signal2(i/(d*250)))
    
#Matrice de transformée de Fourier et inverse
M = dft(d, scale = 'n')
M_inv = np.conj(d*M)

coefs = np.dot(M,v)  #coefs obtenu à partir de l'évaluation du signal 'réel'
coefs2 = np.dot(M,v2)  #coefs obtenu à partir de l'évaluation du signal 'complexe'

#les 2 signaux donnent les mêmes coefficients ! ouf!
#Ils sont ordonnés de c4 à c7 puis de c1 à c3 (comme dans exo prec.) 