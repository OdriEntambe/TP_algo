# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:45:43 2023

@author: User
"""

from abc import ABCMeta, abstractmethod
from math import pi, sqrt

class Forme_géométrique(metaclass = ABCMeta):    #Forme_géométrique est une classe abstraite
    @abstractmethod
    
    def périmètre():     #méthode_abstraite pour pouvoir calculer le périmètre
        pass

    @abstractmethod
    
    def surface():        #méthode_abstraite pour pouvoir calculer la surface
        pass
    
class Rectangle(Forme_géométrique):   #Qui est une classe qui recueille de Forme_géométrique
        def __init__(self, longueur, largeur):
            self._longueur = longueur
            self._largeur = largeur
        def périmètre(self):
            return 2*self._longueur + 2*self._largeur     
        def surface(self):
            return self._longueur*self._largeur
    
class Cercle(Forme_géométrique):        #Qui est aussi une classe qui recueille de Forme_géométrique
        def __init__(self, rayon):
            self._rayon = rayon
        def périmètre(self):
            return 2*pi*self._rayon
        def surface(self):
            return  pi*(self._rayon**2)

class Triangle(Forme_géométrique):    #Encore qui est une classe qui recueille de Forme_géométrique
        def __init__(self, hauteur, cotéA, cotéB, cotéC):
            self._hauteur = hauteur
            self._cotéB = cotéB
            self._cotéA = cotéA
            self._cotéC = cotéC
        def périmètre(self):
            return self._cotéB + self._cotéA + self._cotéC
        def surface(self):
            return(self._cotéA*self._hauteur/2)
    
class Carré(Rectangle):         #Qui est également une classe qui recueille de Forme_géométrique
        def __init__(self, coté):
            Rectangle.__init__(self, coté, coté)

class TriangleRectangle(Triangle):     #Qui est une classe qui recueille de Forme_géométrique encore une fois
        def __init__(self, base, hauteur):
            hyp = sqrt(base**2+hauteur**2)
            Triangle.__init__(self, cotéA = base, cotéB = hauteur, hauteur = hauteur, cotéC = hyp)


    

