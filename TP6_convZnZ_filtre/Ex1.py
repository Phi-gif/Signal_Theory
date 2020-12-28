# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:06:13 2020

@author: Philippine
"""

# Calcul de convolution dans Z/nZ

import numpy as np
from numpy.fft import fft,ifft

f = np.arange(10)
g = [0,0,1,1,0,0,3,0,0,0]
##f et g vues comme des fonctions de Z/nZ
##donc si on veut faire leur convolution, il faut utiliser la transformée de Fourier et de Fourier inverse

four_f = fft(f)
four_g = fft(g)

prod = four_f * four_g

convol_fg = ifft(prod).real #.real pour avoir la notation avec des nb réels

## pas besoin de normaliser par n ici dans les fft ou ifft car on utilise les 2 ensemble