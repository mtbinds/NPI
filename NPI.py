import Pile


class EntreeUtilisateur:
    # Le maximum et le minimum entier qui peut etre donne en entree pour le programme
    VALEUR_MIN = -2147483648
    VALEUR_MAX = 2147483647
    LISTE_ALEATOIRE = [
        1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736,
        35005211, 521595368, 294702567, 1726956429, 336465782, 861021530, 278722862, 233665123,
        2145174067, 468703135, 1101513929, 1801979802, 1315634022, 635723058, 1369133069, 1125898167
    ]  # Stocke la liste des valeurs aleatoires dans le stockage

    def __init__(self):
        self.pile = Pile.Pile()  # Initialise la classe de pile en tant qu'objet
        self.pointeur_aleatoire = 0  # Utilisé pour pointer vers le prochain nombre alaatoire dans la liste

    def traiter_commande(self, commande):
        if commande.lstrip('-').isdigit():
            # Verifie si l'ajout du chiffre entraînera un debordement de la pile, sinon on l'empile dans la pile
            if self.pile.est_pleine():
                print('La pile est pleine.')
            else:
                self.pile.empiler(str(self.limite_valeur(int(commande))))

        elif commande in "+*-%":
            # Vérifie que la commande est +, *, - ou % et appelle la fonction en la passant comme paramètre.
            self.calculer(commande)

        elif commande == "^":
            # Appelle la fonction caculer_puissance si la commande contient un exposant,
            # nous avons besoin de verifications supplementaires pour les exposants dans NPI
            self.calculer_puissance()

        elif commande == '/':
            # Passe "//" comme parametre pour calculer la methode, car NPI preforme une division entiere
            self.calculer('//')

        elif commande == "=":
            # Verifie si la file d'attente est vide, nous imprimons un message et poussons la valeur min, sinon nous
            # appelons la methode voir_pile
            if self.pile.non_pleine(0):
                print("La pile est vide.")
                self.pile.empiler(str(EntreeUtilisateur.VALEUR_MIN))
            else:
                print(self.pile.voir_elem())

        elif commande == 'd':
            # Si la pile est vide, le programme imprimera VALEUR_MIN, sinon imprimera toutes les valeurs de la pile
            if self.pile.non_pleine(0):
                print(EntreeUtilisateur.VALEUR_MIN)
            else:
                self.afficher_pile()

        elif commande == " ":
            pass

        # Verifie si l'utilisateur a donne un flottant, cela donnera un message d'erreur
        # et pousse chaque cote de la decimale comme son propre nombre
        elif commande.lstrip('-').replace(".", "").isdigit():
            number_split = commande.split(".")
            generer_message_erreur(".")
            self.pile.empiler(number_split[0])
            self.pile.empiler(number_split[1])

        elif commande == "a":
            # Appelle la methode des nombres aleatoires
            if self.pile.est_pleine():
                print('La pile est pleine.')
            else:
                self.trouver_nombre_aleatoire()
        else:
            generer_message_erreur(commande)

    def calculer(self, operation):
        # Prend une entree sous forme d'une operation. Éjecte les deux elements de la pile, effectue le calcul et le
        # repousse sur la pile. si la longueur de la pile est <= 1, imprime le sous-depassement de la pile à la place
        if not self.pile.non_pleine(1):
            try:
                val_droite = self.pile.depiler()
                left_val = self.pile.depiler()
                number = eval(left_val + operation + val_droite)
                self.pile.empiler(str(self.limite_valeur(number)))
            except ZeroDivisionError:
                print("Diviser par 0.")
                self.pile.empiler("0")
        else:
            print("La pile est pleine.")

    def calculer_puissance(self):
        # Cacule l'exposant d'un nombre. imprime le message si l'exposant est negatif. Transforme le nombre minimum
        # en nombre maximum si la base est negative. Pousse le resultat de calcul vers la pile
        val_droite = self.pile.depiler()
        val_gauche = self.pile.depiler()
        if int(val_droite) < 0:
            print("Puissance négative.")
            self.pile.empiler(val_gauche)
            self.pile.empiler(val_droite)
        else:
            number = self.limite_valeur(eval(val_gauche + "**" + val_droite))
            if number == EntreeUtilisateur.VALEUR_MIN:
                number = EntreeUtilisateur.VALEUR_MAX
            self.pile.empiler(str(number))

    def trouver_nombre_aleatoire(self):
        self.pile.empiler(
            str(EntreeUtilisateur.LISTE_ALEATOIRE[self.pointeur_aleatoire]))  # Trouve le nombre à l'index et
        # l'empile dans la pile
        if self.pointeur_aleatoire == 23:  # Remet pointeur_aleatoire à 0 si il est == 23 sinon l'incremente de 1
            self.pointeur_aleatoire = 0
        else:
            self.pointeur_aleatoire += 1

    def afficher_pile(self):
        # Itere dans la pile, imprime chaque valeur sur une nouvelle ligne
        for valeur in self.pile.voir_pile():
            print(valeur)

    def limite_valeur(self, number):
        # Limite la valeur maximale et minimale d'un nombre donne en parametre, puis renvoie le nombre
        return max(min(EntreeUtilisateur.VALEUR_MAX, number), EntreeUtilisateur.VALEUR_MIN)


def generer_message_erreur(commande):
    # Generer un message d'erreur pour chaque caractère de la commande et l'affiche à l'écran
    for car in commande:
        print(f'Opérateur ou opérande non reconnu (e) "{car}".')


def supprimer_commentaires(expression):
    # Supprime les chaines contenues dans le bloc #___#
    if "#" in expression:
        for i in range(int(expression.count("#") / 2)):
            debut = expression.index("#")  # Stocke l'index du premier # en partant de la gauche
            expression.empiler(debut)
            fin = expression.index("#")  # Stocke l'index du # suivant en partant de la gauche
            expression.empiler(fin)
            del (expression[debut:fin])  # Supprime le bloc # de la liste
    return expression


if __name__ == "__main__":
    entree_utilisateur = EntreeUtilisateur()
    while True:
        try:
            # Invite l'utilisateur à entrer, divise l'entrée, supprime les commentaires et appelle la méthode
            # traiter_commande
            expression = input()
            expression = supprimer_commentaires(expression.split())
            for car in expression:
                entree_utilisateur.traiter_commande(car)
        except EOFError:
            exit()
