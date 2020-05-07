ListesEleves = [["Yannis","Jeras","Aminata"],["Adem","Rémi","Kevindra"]]
ListeTrié = []

def Tri():
    for sous_listes in ListesEleves:
        for items in sous_listes:
            ListeTrié.append(items)
    print(ListeTrié)

def Dico():
    Tri()
    dico = {}
    for itemsListeTrié in ListeTrié:
        points = 0
        for sous_listes in ListesEleves:
            for itemsSousListes in sous_listes:
                if itemsSousListes == itemsListeTrié:
                    points += 100 - ( sous_listes.index(itemsSousListes) * 10 )
        dico[itemsListeTrié] = str(int(points)) + " points"
    print(dico)

Dico()
