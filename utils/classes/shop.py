from dataclasses import dataclass
from typing import Optional, List
from .powerup import PowerUp


@dataclass
class Shop:
    items: List[dict[PowerUp]]


    def get_items(self) -> Optional[List[str]]:
        player_response = input('Would you like to look at the shop? (Y/N): ').strip().upper()

        if player_response == 'Y':
            return [i.name for i in self.items]
        else:
            return None


    def see_item_attributes(self):
        return [f'Name: {i.name}, Price: {i.price}, Description: {i.description}' for i in self.item]