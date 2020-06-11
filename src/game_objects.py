from room import Room
from item import Item
from lightSource import LightSource

# Declare all the Items
items = {
    "torch": LightSource(
        "Torch",
        "A rustic wooden handle wrapped in silk.",
        "torch"
    ),
    "whip": Item(
        "Whip",
        "A long, strong, cord made of leather. It's perfect for swinging across gaps.",
        "whip"
    ),
    "gold": Item(
        "Gold Ore",
        "Unrefined, but still worth the time and effort to get.",
        "gold", "gold ore", "ore"
    ),
    "pickaxe": Item(
        "Pickaxe",
        "A heafty tool used for mining ore.",
        "pick", "pickaxe"
    ),
    "item5": Item(
        "Item 05",
        "some item",
        "item5"
    ),
    "item6": Item(
        "Item 06",
        "maybe it's nothing",
        "item6"
    )
}

# Declare all the rooms
outside = Room(
    "Outside Cave Entrance",
    "North of you, the cave mouth beckons",
    items["torch"],
    items["whip"]
)

foyer = Room(
    "Foyer",
    "Dim light filters in from the south. Dusty passages run north and east."
)

overlook = Room(
    "Grand Overlook",
    """A steep cliff appears before you, falling into the darkness. Ahead to the north, 
a light flickers in the distance, but there is no way across the chasm."""
)

narrow = Room(
    "Narrow Passage",
    "The narrow passage bends here from west to north. The smell of gold permeates the air.",
    items["gold"]
)

treasure = Room(
    "Treasure Chamber",
    """You've found the long-lost treasure chamber! Sadly, it has already been completely 
emptied by earlier adventurers. The only exit is to the south.""",
    items["pickaxe"],
    items["item5"],
    items["item6"]
)

# Link rooms together
outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

# Extra items
sword = Item(
    "Elven Sword",
    "Finely crafted, and extremely sharp",
    "sword", "blade"
)
