import unittest
from main import Deck, tasha 

class TestDeckClass(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_if_build(self):
        arr = self.deck.build()
        self.assertEqual(arr, [])

    def test_add_cards(self):
        self.deck.addCard(qtd = 10, cmc = 0)          
        self.deck.addCard(qtd = 4, cmc = 1)
        arr = self.deck.build()
        self.assertEqual(arr, [0,0,0,0,0,0,0,0,0,0,1,1,1,1])

    def test_calculate_total_MV(self):
        self.deck.addCard(qtd = 10, cmc = 0) 
        self.deck.addCard(qtd = 4, cmc = 1)
        self.deck.addCard(qtd = 8, cmc = 2)
        resp = self.deck.totalMV()
        self.assertEqual(resp, 20)

    def test_calculate_total_MV_without_order(self):
        self.deck.addCard(qtd = 10, cmc = 0) 
        self.deck.addCard(cmc = 1, qtd = 4)
        self.deck.addCard(qtd = 8, cmc = 2)
        resp = self.deck.totalMV()
        self.assertEqual(resp, 20)

    def test_calculate_total_MV_without_order(self):
        self.deck.addCard(qtd = 10, cmc = 0) 
        self.deck.addCard(cmc = 1, qtd = 2)
        self.deck.addCard(qtd = 8, cmc = 2)
        self.deck.addCard(cmc = 1, qtd = 2)
        resp = self.deck.totalMV()
        self.assertEqual(resp, 20)

    def test_calculate_average_MV(self):
        self.deck.addCard(qtd = 26, cmc = 0) 
        self.deck.addCard(qtd = 10, cmc = 1)
        self.deck.addCard(qtd = 14, cmc = 2)
        self.deck.addCard(qtd = 10, cmc = 3)
        resp = self.deck.avgMV()
        self.assertEqual(resp, 1.1333333333333333)

    def test_title(self):
        deck = Deck()
        deck.addFormat("Legacy")
        deck.addTitle("Lands")
        deck.addCard(qtd = 38, cmc = 0)
        deck.addCard(qtd = 10,cmc = 1)
        deck.addCard(qtd = 9, cmc = 2)
        deck.addCard(qtd = 3, cmc = 3)        
        resp = deck.getTitle()
        self.assertEqual(resp, 'Legacy - Lands - Total MV 37 - Avg MV 0.6166666666666667')

class TestTashaClass(unittest.TestCase):

    def test_if_work(self):
        deck = Deck()
        deck.addCard(qtd = 10, cmc = 0) 
        deck.addCard(qtd = 4, cmc = 1)
        deck.addCard(qtd = 8, cmc = 2)
        resp = tasha(deck.build())
        self.assertEqual(resp, 22)

    def test_if_work_2(self):
        deck = Deck()
        deck.addCard(qtd = 1, cmc = 22) 
        deck.addCard(qtd = 10, cmc = 0) 
        deck.addCard(qtd = 4, cmc = 1)
        deck.addCard(qtd = 8, cmc = 2)
        resp = tasha(deck.build())
        self.assertEqual(resp, 1)

if __name__ == '__main__':
    unittest.main()