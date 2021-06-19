from main import Deck

def create_deck__w_aggro():
    deck = Deck()
    deck.addFormat('Standard')
    deck.addTitle('Mono White Aggro')
    deck.addCard(qtd = 24, cmc = 0)
    deck.addCard(qtd = 12,cmc = 1)
    deck.addCard(qtd = 10, cmc = 2)
    deck.addCard(qtd = 12, cmc = 3)
    deck.addCard(qtd = 2, cmc = 4)
    return deck

#TODO 
#Sultai Control