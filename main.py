import statistics
from random import sample
from matplotlib import pyplot
import legacy

class Deck:

    def __init__(self):
        self.title = ""
        self.format = ""
        self.cards = []

    def addCard(self,qtd,cmc):
        self.cards += [cmc]*qtd

    def addTitle(self, title):
        self.title = title

    def addFormat(self, format):
        self.format = format

    def getTitle(self):
        return " - ".join([self.format, self.title, "Total MV " + str(self.totalMV()), "Avg MV " + str(self.avgMV())])        

    def totalMV(self):
        return sum(self.cards)

    def avgMV(self):        
        return statistics.mean(self.cards) 

    def build(self):
        return self.cards

def tasha(arr):
    mana = 0
    for i in range(len(arr)):
        mana += arr[i]
        if(mana > 19):
            break
    qtd_exiled_card = i + 1
    return qtd_exiled_card

def simulation():
    deck = legacy.create_deck__legacy_lands()
    arr = deck.build()

    exile = []
    MAX_SIMULATIONS = 999
    for i in range(MAX_SIMULATIONS):
        shuffleddeck = sample(arr, len(arr))
        exile.append(tasha(shuffleddeck))
        
    B = pyplot.boxplot(exile, vert=0)
    pyplot.suptitle(deck.getTitle())
    outliers = [flier.get_xdata() for flier in B["fliers"]][0]
    arrPlotLabels = list(outliers)+[item.get_xdata()[1] for item in B['whiskers']] + [item.get_xdata()[1] for item in B['boxes']]+[item.get_xdata()[1] for item in B['medians']] + [item.get_xdata()[2] for item in B['boxes']]
    pyplot.xlabel('Number of Cards Exiled')
    pyplot.xticks(arrPlotLabels)
  
    pyplot.show()
    
if __name__ == "__main__":
    simulation()