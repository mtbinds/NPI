
import unittest
from NPI import EntreeUtilisateur


class TestNPI(unittest.TestCase):
    
    # Test des opérations de notre calculatrice NPI
    npi=EntreeUtilisateur()
    # Test addition 
    def test_addition(self):

        

        for car in ['2','2','+','=']:
            self.npi.traiter_commande(car)

        self.assertEquals('4', self.npi.pile.resultat)
        
    # Test_soustraction
    def test_soustraction(self):

        for car in ['100','37','-', '=']:
            self.npi.traiter_commande(car)

        self.assertEquals('63', self.npi.pile.resultat)

    # Test multiplication    
    def test_multiplication(self):


        for car in ['100','3','*','=']:
            self.npi.traiter_commande(car)

        self.assertEqual('300', self.npi.pile.resultat)

    # Test division
    def test_division(self):


        for car in ['125','5','/','=']:
            self.npi.traiter_commande(car)

        self.assertEqual('25', self.npi.pile.resultat)

    # Test modulo
    def test_modulo(self):
    
        for car in ['100','90','%','=']:
            self.npi.traiter_commande(car)

        self.assertEqual('10', self.npi.pile.resultat)
    
    # Test puissance 
    def test_puissance(self):

        for car in ['3','2','^','=']:
            self.npi.traiter_commande(car)

        self.assertEqual('9', self.npi.pile.resultat)

   
if __name__ == "__main__":
    unittest.main()