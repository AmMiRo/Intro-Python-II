# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def move_self(self, direction):
        target_room = getattr(self.current_room, '{}_to'.format(direction))
        if target_room is not None:
            self.current_room = target_room
        else:
            print("You can't go that way.\n")

    def get_inventory(self):
        if len(self.items) > 0:
            print("Your inventory:")
            for item in self.items:
                print(item)
        else:
            print("You have nothing in your inventory.\n")
        
    def get_item(self, item):
        if self.current_room.items and item in self.current_room.items:
            self.items.append(item)
            self.current_room.items.remove(item)
            print(f"You picked up {item}")
        else:
            print(f"There is no {item} to get.\n")

    def drop_item(self, item):
        if item in self.items:
            self.current_room.items.append(item)
            self.items.remove(item)
            print(f"You dropped {item}.\n")
        else:
            print(f"You have no {item} to drop.\n")