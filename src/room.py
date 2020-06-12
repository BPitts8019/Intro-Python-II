# Implement a class to hold room information. This should have name and
# description attributes.
from textwrap import fill
from inventory import Inventory
from item import Item
from lightSource import LightSource


class Room:
    def __init__(self, name: str, description: str, is_lit: bool = True, *items):
        self.name = name
        self.description = description
        self.is_lit = is_lit
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items_list: Inventory = Inventory(list(items))
        self.is_detailed_view = False
        self.is_show_detail = True

    def __str__(self):
        output = self.name

        if self.is_show_detail:
            output += f"\n{fill(self.description)}"

            if len(self.items_list) > 0:
                output += f"\n\nItems in view:\n"
                output += str(self.items_list)

        self.is_detailed_view = self.is_show_detail
        return output

    def __repr__(self):
        return f"Room: [name={self.name}, description={self.description}, items_list={self.items_list}]"

    def show_detail(self):
        self.is_show_detail = True

    def hide_detail(self):
        self.is_show_detail = False

    def has_type(self, item_type: type) -> bool:
        return self.items_list.has_type(item_type)

    def add_item(self, item: Item):
        self.items_list.add_item(item)

    def remove_item(self, item_name: str) -> Item:
        return self.items_list.remove_item(item_name)
