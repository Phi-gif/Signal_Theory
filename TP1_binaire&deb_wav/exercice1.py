# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
"""
#Exercice 1 

#Qb
##De l'entier à l'écriture binaire
(18).to_bytes(1, byteorder = 'little')          #on code sur 1 octet, convention little-endian 
                                                #(mais qui ne sert à rien quand on est dur un octet)

##De l'écriture binaire à l'entier
int.from_bytes(b'\x12', byteorder = 'little')   

"""cf documentation python de ces 2 fonctions"""

#Qd

with open('f8u.bin','wb') as f:                                        #création d'un fichier binaire 'f8u.bin'
    for i in range(1,11):
        f.write((i).to_bytes(1, byteorder='little', signed=False))     #écriture des nombres en binaire (1 octet)
                                                                       #dans le fichier, en convention little-endian et non signés
        
with open('f8u.bin','rb') as g:                                        #ouverture du fichier 'f8u.bin' en mode binaire
    print(g.read())                                                    #affiche les nombres sous forme binaire mais en
                                                                       #1 seule chaine de byte
with open('f8u.bin','rb') as g:                                        
    print(list(g.read()))                         #Le 'list' marche ici car juste 1 octet, sinon regarder la méthode 
                                                  #généralisée ci-dessous

#Question e
    
with open('f16sl.bin','wb') as f:
    for i in range(1,11):
        f.write((i).to_bytes(2, byteorder='little', signed=True))       #écriture des nombres en binaire (2 octets)
                                                                        #dans le fichier
#fonction affichant la liste des nombres
with open('f16sl.bin','rb') as g:
    liste=[]                                                            #liste récupérant les nombres entier
    chaine = g.read()                                                   #correspond au contenu du fichier 'f16sl.bin'
    i=0
    n=len(chaine)
    while i<n:
        liste.append(int.from_bytes(chaine[i:i+2], byteorder='little', signed=True))
        #le i+2 permet de considéré le codage sur 2 octets (16 bits)
        i+=2
    print(liste)
    
#fonction affichant les nombres à la suite (version du code précédent sans liste)
with open('f16sl.bin','rb') as g:                                                                
    chaine = g.read()                                                   
    i=0
    n=len(chaine)
    while i<n:
        print(int.from_bytes(chaine[i:i+2], byteorder='little', signed=True))
        i+=2

#Question f
    
with open('f16sb.bin','wb') as f:
    for i in range(1,11):
        f.write((i).to_bytes(2, byteorder='big', signed=True))

with open('f16sb.bin','rb') as g:                                       #version sans liste focntionne aussi ici
    liste=[]
    chaine = g.read()
    i=0
    n=len(chaine)
    while i<n:
        liste.append(int.from_bytes(chaine[i:i+2], byteorder='big', signed=True))
        i+=2
    print(liste)
      
##Remarque : tant qu'un fichier binaire est écrit et lu avec les mêmes conventions 
## (nb d'octets, little/big endian et signed/non signed), alors tout fonctionne correctement
    
#Qg
##Coder des float en binaire
import array as ar #autre façon de faire, qui marche bien pour les float

A=ar.array('f',[-0.5,-1.7,2.3]) #'f' pour float

with open('ffloat.bin', 'wb') as f:
     A.tofile(f)                                                #on écrit dans le fichier 'ffloat.bin' les float en binaire (ou en hexa ?)

with open('ffloat.bin', 'rb') as g:
    B=ar.array('f',[])                                          #on est obligé de créer un deuxième objet array
    B.frombytes(g.read())                                       #pour pouvoir 'écrire'/ajouter la conversion des nombres
                                                                #binaire dans B, avec la commande .frombytes
    