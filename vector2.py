# coding: utf-8
get_ipython().show_usage()
get_ipython().run_line_magic('ls', '-la')
get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('bookmark', '-l ')
get_ipython().run_line_magic('clear', '')
import collections
Point = collections.namedtuple('Point', 'x y')
Point(1, 2)
p=Point(1, 2)
p.x
p.y
Card = collections.namedtuple('Card', 'rand suit')
class FrenchDeck:
    rank_value = FrenchDeck.ranks.index(card.rand)
    suits  = 'spades diamonds clubs hearts'
    def __init__(self):
        self._cards = [Card(rank, suit)  for suit in self.suits.split() for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
        
uid['key']
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits  = 'spades diamonds clubs hearts'
    def __init__(self):
        self._cards = [Card(rank, suit)  for suit in self.suits.split() for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
        
def salam():
    return 'hello'
    
fd = FrenchDeck()
fd.ranks
fd.suits
fd._carsss
fd._cards
len(fd)
fd[0]
fd[0].rand
for i in fd:
    print(i)
    
class A:
    def __init__(self):
        self.a = [1,2,3,4,5]
        
class A:
    def __init__(self):
        self.a = [1,2,3,4,5]
    def __getitem__(self, position):
        return self.a[position]
        
a = A()
a.a
a[1]
a[2]
for i in a:
    print(i)
    
class A:
    def __init__(self):
        self.a = [1,2,3,4,5]
    def __iter__(self):
        return iter(self.a)
        
a = A()
for i in a:
    print(i)
    
class A:
    def __init__(self):
        self.a = [1,2,3,4,5]
    def __getitem__(self, position):
        print(position)
        return self.a[position]
        
a = A()
a[1:2]
a[1:2:10]
slice
help(slice)
a[1]
a['key']
fd[0]
from random import choise
from random import choice
choice(fd)
choice(fd)
choice(fd)
choice(fd)
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rand)
    return rank_value * len(suit_value) + suit_value[card.suit]
    
fd._cards
cj = Card(rand='J', suit='hearts')
ck = Card(rand='K', suit='hearts')
spades(cj)
spades_high(cj)
spades_high(ck)
fd.ranks
fd.ranks.index(cj.rand)
len(suit_value)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rand)
    return rank_value + suit_value[card.suit]
    
for card in sorted(deck, key=spades_high):
    print(card)
    
for card in sorted(fd, key=spades_high):
    print(card)
    
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rand)
    return rank_value * len(suit_value) + suit_value[card.suit]
    
for card in sorted(fd, key=spades_high):
    print(card)
    
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rand)
    return rank_value * len(suit_value)
    
for card in sorted(fd, key=spades_high):
    print(card)
    
cj in fd
ck in fd
Card('U', 'spades')
cu = Card('U', 'spades')
cu in fd
class Name:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Name({self.name!r})'
        
class Person:
    def __init__(self):
        self.name = name
        
class Name:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Name({self.name!r})'
        
class Person:
    def __init__(self,name):
        self.name = name
        
    def __repr__(self):
        return f'Person({self.name!r})'
        
       
n = Name('hamid')
p = Person(n)
p
eval(p)
eval(p.__repr__())
a = eval(p.__repr__())
a.name
type(a)
a.__name__
a.__code__
a.__dict__
import math 
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    def __abs__(self):
        return math.hypot(self.x, self.y)
        
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x 
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
        
get_ipython().run_line_magic('save', 'vector.py')
