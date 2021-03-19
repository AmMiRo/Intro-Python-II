class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def inspect_item(self, player, item):
        if item in player.current_room.items or item in player.items:
            print(f"You inspect the {item}, it {self.description}.\n")
        else:
            print(f"There isn't any {item} to inspect.\n")