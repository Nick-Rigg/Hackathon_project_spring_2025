from dataclasses import dataclass

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