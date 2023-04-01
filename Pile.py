class Pile:
    def __init__(self):
        # Initialise une liste vide en mémoire, on peut importer cette classe dans npi.py et en faire un objet,
        # cela nous permet d'avoir des méthodes qui ressemblent étroitement au comportement d'une pile
        self.pile = []

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        # Stocke l'élément en haut de la liste, supprime l'index supérieur et renvoie l'élément
        item = self.pile[-1]
        self.pile.pop(-1)
        return item

    def voir_elem(self):
        return self.pile[-1]
    
    def est_vide(self):
        return self.pile == []
    
    def longueur_pile(self):
        j = 0
        while not self.vide():
            self.depile()
            j += 1
        return j

    def non_pleine(self, length):
        # Renvoie vrai si la pile est <= une longueur donnée
        return (len(self.pile) <= length)

    def est_pleine(self):
        # Renvoie vrai si le nombre d'éléments dans la pile est supérieur à 22
        return len(self.pile) > 22

    def voir_pile(self):
        return self.pile
