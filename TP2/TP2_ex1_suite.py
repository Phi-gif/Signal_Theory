# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:58:42 2020

@author: Philippine
"""

from scipy.io import wavfile
import numpy as np

delta = 44100                                       #fréquence d'échantillonnage

#Question e

def s1(t):                                          #La440
    return(np.sin(2*np.pi*440*t))
    
def s2(t):                                          #Si un ton plus haut que le La440
    return(np.sin(2*np.pi*440*2**(1/6)*t))

def s(t):                                           #Signal non fondu
    return(s1(t)+s2(t))

def a(t):                                          
    if 0<=t<=1:
        return(t)
    else:
        return(1)

def s_mix(t):                                       #signal fondu au début
    return(a(t)*(s1(t)+s2(t)))
    
def u_mix(v,maximum, minimum):                      #focntion pour renvoyer des entiers quand on code en 16 bits signés
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

data_mix_mono_fondu = remplissage_array_mix_mono(s_mix,3,u_mix)       

wavfile.write('LaSiMonoFonduDeb.wav',delta,data_mix_mono_fondu)       #création du fichier wav 'LaSiMonoFonduDeb.wav', en fréquence 44100, pendant 3 secondes

#Question f

def param(wav_fname):                                                 #Fonction permettant de rendre la fréquence d'échantillonnage et
    samplerate, data = wavfile.read(wav_fname)                        #la durée d'un fichier .wav ainsi que le tableau de nombre associé
    d = data.shape[0] / samplerate
    return(samplerate,d,data)


#Question g
    
def amplitude_fondu_fin(t,d):                                       #Fonction amplitude permettant de diminuer le volume du signal d'entrée sur la dernière seconde                                          
    if 0<=t<=d-1:
        return(1)
    else:
        return(d-t)
      
def data_modif(file):                                               #Fonction modifiant le signal d'entré (vecteur de nombre) pour le fondre sur la dernière seconde
    samplerate, d, data = param(file)
    fondue = np.ndarray((samplerate*int(d),),dtype = np.int16)
    for i in range(samplerate*int(d)):
        fondue[i] = data[i] * amplitude_fondu_fin(i/samplerate,d)
    return(fondue)
   
file = 'LaSiMono.wav'                           #fichier à lire puis 'fondre'
data_fondu = data_modif(file)

wavfile.write('LaSiMonoFonduFin.wav',delta,data_fondu)       #création du fichier wav 'LaSiMonoFonduFin.wav', en fréquence 44100
                                                                            #pendant 3 secondes (temps du fichier en entrée)
