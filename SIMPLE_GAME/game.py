class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []

    def connect(self, direction, room):
        self.connections[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Game:
    def __init__(self):
        self.current_room = None
        self.inventory = []

    def start(self):
        # Initialize rooms and items
        room1 = Room("Living Room", "A cozy living room with a fireplace.")
        room2 = Room("Kitchen", "A kitchen with a fridge and a stove.")
        room1.connect("north", room2)

        key = Item("Key", "A small rusty key.")
        room1.add_item(key)

        self.current_room = room1
        self.game_loop()

    def game_loop(self):
        while True:
            print(f"You are in the {self.current_room.name}.")
            print(self.current_room.description)
            command = input("> ").strip().lower()

            if command == "quit":
                break
            elif command.startswith("move "):
                direction = command.split(" ")[1]
                if direction in self.current_room.connections:
                    self.current_room = self.current_room.connections[direction]
                else:
                    print("You can't go that way.")
            elif command.startswith("take "):
                item_name = command.split(" ")[1]
                for item in self.current_room.items:
                    if item.name.lower() == item_name:
                        self.inventory.append(item)
                        self.current_room.remove_item(item)
                        print(f"You took the {item.name}.")
                        break
                else:
                    print("Item not found.")
            # Add more commands as needed

if __name__ == "__main__":
    game = Game()
    game.start()
