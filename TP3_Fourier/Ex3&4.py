#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:21:26 2020

@author: prenaudin
"""

#Exercice 3

from scipy.linalg import dft
import numpy as np

#Fonction renvoyant le matrice de fourier et la matrice inverse de fourier

def MatriceFourrier(d):
    M = dft(d, scale = 'n')     #matrice de Fourier du cours
    N = np.conj(d*M)
    return(M,N)

#Tests
M = MatriceFourrier(3)[0]
M_inv = MatriceFourrier(3)[1]

#Exercice 4
##Question c

#Détermination des valeurs du signal en fonction des coefficients ci calculés à la main 
Mat_inv = MatriceFourrier(9)[1]
c = [1,1,0,0,-3*1j/2,3*1j/2,0,0,1]  #Attention à l'ordre des coefficients (c0,c1,...,c4,c-4,...,c-1)
res = np.dot(Mat_inv,c).real        #valeurs du signal (ne prend que la partie réelle car on a des arrondis
                                    #de complexe)

##sinon, on peut utiliser la focntion suivante :
from numpy.fft import fft,ifft

valeurs = 9*ifft(c).real
coef = (1/9)*fft(valeurs)

#on aurait aussi c = (1/9)*fft(valeurs)

