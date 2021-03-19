# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    
    def search_room(self):
        if self.items:
            print("You found:")
            for item in self.items:
                print(item)
        else:
            print("You found nothing.\n")