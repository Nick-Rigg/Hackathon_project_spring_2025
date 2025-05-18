from dataclasses import dataclass
from typing import List


@dataclass
class PowerUp:
    items: List[dict]
    name: str
    price: int
    description: str

    def add_power_up(self):
        self.items.append([{
            'name': self.name,
            'price': 50,
            'description': self.description
        }])

    @property
    def dealer_insight(self):
        self.add_power_up('Dealer Insight', 50, 'Peek at the dealers score')

    @property
    def peeping_tom(self):
        self.add_power_up('Peeping Tom', 100, 'Look at the next card')
