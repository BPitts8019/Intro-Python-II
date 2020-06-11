from item import Item


class LightSource(Item):
    def __init__(self, name: str, description: str, *alias_list):
        super().__init__(name, description, *alias_list)

    def on_drop(self):
        print("It's not wise to drop your source of light!")
        print(f"\tYou drop the {self.name}")
