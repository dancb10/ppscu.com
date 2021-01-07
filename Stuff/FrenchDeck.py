import collections
from random import choice

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:

    ranks = [str(i) for i in range(2,11)]+ list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)


# beer_card = Card('7', 'diamonds')
# print(beer_card)


# print(deck._cards)
# len(deck)
# print(deck[0])
# print(deck[-1])
#
# for i in range(10):
#     print(choice(deck))
#
# for card in reversed(deck):
#     print(card)
#
# for card in reversed(deck):  # doctest: +ELLIPSIS
#     print(card)
