# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:16:32 2023 
@author: 
    Groupe18 :
ENTAMBE EYOFELA ODRI
KABAMA MUTELA JORIS
KANYIKY NGANDU KALLY
"""
"""REPONSE 7"""
from progr1_18 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, GeoFig

if __name__ == '__main__':
    print("Depuis les classes seules :")
    print()
    try:
        for i in range (1,7):
            rectangle = Rectangle("Rectangle KANYIKY1", 12+i, 7)
            cercle = Cercle("Cercle EYOFELA2", 14)
            triangle = Triangle("Triangle KABAMBA3", 9, 6, 7)
            carre = Carre("Carré ODRI4", 6)
            t_rectangle = TriangleRectangle("Triangle Rectangle JORIS5", 5, 7)
        
            rectangle.decris_toi()
            print()
            cercle.decris_toi()
            print()
            triangle.decris_toi()
            print()
            carre.decris_toi()
            print()
            t_rectangle.decris_toi()
            print()
    except Exception:
        print("Parametres non pris en considération.")
    
    print()
    print()
    print("On comme à partir la classe <Globale> : ")
    print()
    for i in range (1,2):
        figureA = GeoFig() 
        figureB = GeoFig() 
        figureC = GeoFig()
        figureD = GeoFig()
        figureE = GeoFig()
        
        figureA.add(Rectangle("Rectangle EYOFELA1", 12, 5))
        figureB.add(Cercle("Cercle JORIS2", 5))
        figureC.add(Triangle("Triangle ODRI3", 9, 6, 7))
        figureD.add(Carre("Carré B4", 10))
        figureE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
        
        figureA.decris_toi()
        figureB.decris_toi()
        figureC.decris_toi()
        figureD.decris_toi()
        figureE.decris_toi()
        
        try:
            figureA.add(Rectangle("Rectangle EYOFELA1", 12, 5))
            figureB.add(Cercle("Cercle MUTELA2", 5))
            figureC.add(Triangle("Triangle NGANDU3", 9, 6, 7))
            figureD.add(Carre("Carré KADY4", 10))
            figureE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
            
            figureA.decris_toi()
            figureB.decris_toi()
            figureC.decris_toi()
            figureD.decris_toi()
            figureE.decris_toi()
        except Exception:
            print("Parametres non pris en charge.")
print(" *Fin du programme:)* ")
        
