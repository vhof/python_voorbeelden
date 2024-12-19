"""
Autheur         : Vincent van 't Hof
Doel            : Dit programma bevat een functie die de    
                  winnaar van een potje steen-papier-schaar 
                  bepaalt
Datum / versie  : 

Invoer          :
Uitvoer         : 
Gebruikte berekeningen / algoritmen :

Python modules die geïmporteerd worden : math
Overige opmerkingen : 

"""
import math


def steenPapierSchaar(s1, s2):
    """Bepaal het resultaat van een potje 
    steen-papier-schaar tussen s1 en s2
    """

    resultaat = ""
    
    # Als beide spelers hetzelfde hebben is het gelijkspel
    if s1 == s2:
        resultaat = "Gelijkspel!"
    
    # s1 wint volgens de regels steen > schaar >papier > steen
    elif (   s1 == "steen"  and s2 == "schaar"
          or s1 == "papier" and s2 == "steen"
          or s1 == "schaar" and s2 == "papier"):
            resultaat = "Player 1 won!"
    
    # In alle andere gevallen wint s2
    else:
        resultaat = "Player 2 won!"
        
    return resultaat
