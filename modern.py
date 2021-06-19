import main 

def create_deck__burn():
    deck = main.Deck()
    deck.addFormat('Modern')
    deck.addTitle('Burn')
    deck.addCard(qtd = 20, cmc = 0)
    deck.addCard(qtd = 16,cmc = 1)
    deck.addCard(qtd = 16, cmc = 2)
    deck.addCard(qtd = 8, cmc = 3)
    return deck

def create_deck__atitan():
    deck = main.Deck()
    deck.addFormat('Modern')
    deck.addTitle('Amulet Titan')
    deck.addCard(qtd = 39, cmc = 0)
    deck.addCard(qtd = 9,cmc = 1)
    deck.addCard(qtd = 2, cmc = 2)
    deck.addCard(qtd = 6, cmc = 3)
    deck.addCard(qtd = 4, cmc = 6)
    return deck 

def create_deck__gshadow():
    deck = main.Deck()
    deck.addFormat('Modern')
    deck.addTitle('Grixis Shadow')
    deck.addCard(qtd = 22, cmc = 0)
    deck.addCard(qtd = 28,cmc = 1)
    deck.addCard(qtd = 10, cmc = 2)
    return deck 

#TODO 
#Humans 