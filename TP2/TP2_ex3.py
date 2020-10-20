#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:39:20 2020

@author: prenaudin
"""

from scipy.io import wavfile
import numpy as np

delta = 44100

#Question a

def s1(t):                                       
    return(np.sin(2*np.pi*440*t))
    
def s2(t,phi):                                       
    return(np.sin(2*np.pi*440*t + phi))
    
def s(t,phi):
    return(s1(t)+s2(t,phi))
    
def u(v,maximum,minimum):                                   
    a =((2**16)-1)/(maximum-minimum)
    b = -(a/2)*(maximum+minimum)-1/2
    return (int(a*v+b))        

def simult(sig,phi,t,recadrage):
    data=np.ndarray((delta*t,),dtype=np.int16)
    signaux = []
    for step in range(delta*t):                     
        temps=step/delta
        signal=sig(temps,phi)
        signaux.append(signal)
    minimum=min(signaux)
    maximum=max(signaux)
    i=0
    for signal in signaux:
        data[i]=recadrage(signal,maximum, minimum)
        i+=1
    return(data)
    
#Question b

data_pi_sur_2 = simult(s,np.pi/2,3,u)
data_pi = simult(s,-np.pi/2,3,u)

wavfile.write('simulpisur2.wav',delta,data_pi_sur_2)
wavfile.write('simulpi.wav',delta,data_pi)


    
