# coding: utf-8
import collections
from random import choice

Card = collections.namedtuple('Card', 'rank suit')


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits  = 'spades diamonds clubs hearts'
    def __init__(self):
        self._cards = [Card(rank, suit)  for suit in self.suits.split() for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
        


deck = FrenchDeck()
    
# len(deck)
# deck[0]
# deck[1]
# deck[2]
# deck[10]
# deck[11]
# deck[12]
# deck[13]
# choice(deck)

choice.__code__
import inspect 
print(inspect.getsource(choice))
deck[1]
deck[1:10]
Card('Q', 'hearts') in deck
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]
    
for card in sorted(deck, key=spades_high):
    print(card)
    
