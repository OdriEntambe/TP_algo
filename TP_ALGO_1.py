# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:02:16 2023
@author: Joris Kabamba
"""

class ArrayStack:
    """ Implémentation de la pile LIFO à l'aide
     une liste Python comme stockage sous-jacent"""
    def __init__(self):
        """ Créer une pile vide"""
        self._data = []
    def __len__(self):
        """Renvoyez le nombre de
         éléments de la pile"""
        return len(self._data)
    def is_empty(self):
        """Renvoie True si la pile est vide"""
        return len(self._data) == 0
    def push(self, e):
        """Ajouter l'élément e en haut de la pile"""
        self._data.append(e)
    def top(self):
        """Renvoyer (mais pas supprimer) le
         élément en haut de la pile
         Lever une exception vide si la pile est vide"""
        if self.is_empty():
            raise Empty("La pile est vide")
        return self._data[-1]
    def pop(self):
        """Retirer et retourner l'élément
     du haut de la pile (c'est-à-dire LIFO).
     Raise Empty exception si la pile est vide."""
        if self.is_empty():
            raise Empty("La pile est vide")
        return self._data.pop()
    #whrite by DILemagnifique.



