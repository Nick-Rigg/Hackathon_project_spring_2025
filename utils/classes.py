from dataclasses import dataclass, field
import random
from typing import List, Optional




# ---------------- Class relating to the Deck -------------------------
@dataclass
class Card:
    suit: str
    rank: str

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank


@dataclass
class Deck:
    suits: list = field(default_factory=lambda: ['Heart', 'Diamond', 'Club', 'Spade'])
    ranks: dict = field(default_factory=lambda: {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11})
    cards: list = field(init=False)

    def __post_init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def reset_deck(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()
# ---------------------------------------------------------------------


# ------------ Class relating to the dealer and player ----------------
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


@dataclass
class Dealer:
    deck: Deck
    hand: list[Card] = field(default_factory=list)

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
    
    def calculate_hidden_hand(self):
        total = 0
        aces = 0
        total += self.deck.ranks[(self.hand[0]).rank]
        #while total > 21 and aces:
        #    total -= 10
        #    aces -= 1
        return total

    
    def reset_hand(self):
        self.hand = []
# ----------------------------------------------------------------------


# --------------- Class related to shop --------------------------------
@dataclass
class PowerUp:
    name: str
    price: int
    description: str


@dataclass
class Shop:
    item:List[PowerUp]


    def get_items(self) -> Optional[List[str]]:
        player_response = input('Would you like to look at the shop? (Y/N): ').strip().upper()

        if player_response == 'Y':
            return [i.name for i in self.item]z
        else:
            return None
        
    def see_item_attributes(self):
        return [f'Name: {i.name}, Price: {i.price}, Description: {i.description}' for i in self.item]
