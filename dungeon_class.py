class Dungeon:

    def __init__(self, filename):
        with open(filename, "r") as in_file:
            self.dungeon_map = in_file.read().splitlines()

    def print_map(self):
        for line in self.dungeon_map:
            print (line)

    def spawn(self, hero):
        pass

    def move_hero(self, position="None"):
        pass


dungeon_map = Dungeon("level1")
dungeon_map.print_map()
