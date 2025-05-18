from dataclasses import dataclass, field
from .deck import Deck
from .card import Card

@dataclass
class Player:
    deck: Deck
    hand: list[Card] = field(default_factory=list)
    bank: int = 100

    def add_card(self, card):
        self.hand.append(card)
        return self.hand
    
    def calculate_hand(self):
        total = 0
        aces = 0
        for card in self.hand:
            total += self.deck.ranks[card.rank]
            if card.rank == 'Ace':
                aces += 1
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total
    
    def reset_hand(self):
        self.hand = []