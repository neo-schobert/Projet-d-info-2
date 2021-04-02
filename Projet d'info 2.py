import cmath
import numpy as np
import random

def calcul_R(tab):
    """
    Entrée :
    tab : Le tableau tab contient les coefficients du polynome P c'est à dire : tab=[a_{p-1},a_{p-2},...,a_1,a_0]
    _________

    Sortie : Renvoie le rayon R du disque D tel que défini dans l'énoncé. R=1+max(|a_{p-1}|,...,|a_0|)
    """
    max=abs(tab[0]) # La structure du tableau est la plus adaptée (structure statique est modifiable) même si des listes (pas fait pour être indexée (sauf en python)) pourraient convenir en Python.
    n=len(tab) 
    for k in range(n): #Il s'agit d'un simple parcours de tableau en cherchant le maximum.
        if abs(tab[k])>max:
            max=abs(tab[k]) #La recherche se concentre uniquement sur le maximum
    return max+1 #Renvoie le maximum du tableau des coefficients du polynome P incrémenté de 1.


def P_el(tab,el):
    """
    Entrée : 
    tab : Le tableau tab contient les coefficients du polynome P c'est à dire : tab=[a_{p-1},a_{p-2},...,a_1,a_0]
    el : Il s'agit d'un nombre complexe quelconque
    ________

    Sortie :
    Renvoie True si el est racine de P et False sinon avec P=X^p + a_{p-1}X^{p-1}+...+a_1X + a_0. 
    """
    p=len(tab)
    resultat=el**p
    for k in range(p):
        resultat+=el**(p-k-1)*tab[k]
    return resultat


def random_complex_de_D(R):
    return ((random.random()*R) +  (random.random()*R)*1j)


def suite_Durand_Kerner1(tab,epsilon):
    """
    Entrée :
    tab : Le tableau tab contient les coefficients du polynome P c'est à dire : tab=[a_{p-1},a_{p-2},...,a_1,a_0]
    epsilon : Valeur de la répétition du calcul de x_n^{(k)}. Il agit sur la complexité du programme et doit être choisi
    proportionnelement au degré de P.
    ________
    
    Sortie : 
    Renvoie le tableau des racines du polynôme donné
    """
    p=len(tab)
    t=np.copy(tab)
    R=calcul_R(tab)
    for k in range(p):
        while P_el(tab,t[k])==0 or (t[k] in t[0:k]):
            t[k]=random_complex_de_D(R)
    for i in range(p):
        for l in range(epsilon):
            prod=1
            for m in range(i):
                prod*=t[i]-t[m]
            for m in range(i+1,p):
                prod*=t[i]-t[m]
            print(t[i])
            t[i]-=P_el(tab,t[i])/prod
    return t


print(suite_Durand_Kerner1([0+0j,1+0j],10))


# def visualisation_racine_disque(tab):



