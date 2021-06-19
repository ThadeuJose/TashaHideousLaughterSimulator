import main 


def create_deck__legacy_lands():
    deck = main.Deck()
    deck.addFormat('Legacy')
    deck.addTitle('Lands')
    deck.addCard(qtd = 38, cmc = 0)
    deck.addCard(qtd = 10,cmc = 1)
    deck.addCard(qtd = 9, cmc = 2)
    deck.addCard(qtd = 3, cmc = 3)
    return deck

def create_deck__legacy_delver():
    deck = main.Deck()
    deck.addFormat('Legacy')
    deck.addTitle('Izzet Delver')
    deck.addCard(qtd = 18, cmc = 0)
    deck.addCard(qtd = 28,cmc = 1)
    deck.addCard(qtd = 7, cmc = 2)
    deck.addCard(qtd = 1, cmc = 3)
    deck.addCard(qtd = 4, cmc = 5)
    deck.addCard(qtd = 2, cmc = 7)
    return deck 