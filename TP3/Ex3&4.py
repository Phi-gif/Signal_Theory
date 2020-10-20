#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:21:26 2020

@author: prenaudin
"""

from scipy.linalg import dft
import numpy as np

#Fonction renvoyant le matrice de fourier et la matrice inverse de fourier

def MatriceFourrier(d):
    N = dft(d, scale = None)
    M = (1/d)*np.conj(N)
    return(M,N)
    
M = MatriceFourrier(3)[0]
M_inv = MatriceFourrier(3)[1]

#Exercice 4
##Question c

Mat_inv = MatriceFourrier(9)[1]
c = [1,1,0,0,3*1j/2,-3*1j/2,0,0,1]  #pris les conjugués, pk ?
res = np.dot(Mat_inv,c)

