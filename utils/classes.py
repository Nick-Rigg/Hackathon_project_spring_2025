from dataclasses import dataclass, field
import random



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
    
    def reset_hand(self):
        self.hand = []
# ----------------------------------------------------------------------


# --------------- Class related to shop --------------------------------
@dataclass
class Shop:
    items: list = field(default_factory=list)

    def get_items(self):
        return self.items
    

@dataclass
class PowerUps:
    shop: Shop
    name: str
    price: int
    description: str

    def peek_at_dealers_score(self):
        self.name = 'Dealer Insight'
        self.price = 50
        self.description = 'Peek at the dealers score'
        self.add_item_to_shop(self.name)

    def add_item_to_shop(self):
     self.shop.items.append(self.name)
