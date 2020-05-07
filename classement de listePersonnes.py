Eleves = [["Yannis","Jeras","Aminata"],["Adem","Rémi","Kevindra"]]
L = []

def Algorithme():
    for sous_listes in Eleves:
        for items in sous_listes:
            L.append(items)
    dictionnaire = {}
    for items in L:
        points = 0
        for sous_listes in Eleves:
            for itemsSousListes in sous_listes:
                if itemsSousListes == items:
                    points += 10 / ( sous_listes.index(itemsSousListes) + 1 )
        dictionnaire[items] = str(int(points)) + " points"
    print(dictionnaire)

Algorithme()
