from hero_class import Hero
from enemy_class import Enemy


class Dungeon:

    def __init__(self, filename):
        with open(filename, "r") as in_file:
            lines = in_file.read().splitlines()
            self.dungeon_map = []
            for line in lines:
                self.dungeon_map.append(list(line))

    def print_map(self):
        for line in self.dungeon_map:
            print (''.join(line))

    def spawn(self, hero):
        counter = 0
        for i in range(0, len(self.dungeon_map)):
            for j in range(0, len(self.dungeon_map[i])):
                if self.dungeon_map[i][j] == "S" and counter < 1:
                    counter += 1
                    self.dungeon_map[i][j] = "H"

    def move_hero(self, direction="None"):
        for i in range(0, len(self.dungeon_map)):
            for j in range(0, len(self, dungeon_map[i])):
                pass


h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

dungeon_map = Dungeon("level1")
dungeon_map.print_map()
dungeon_map.spawn(h)
print (10 * '-')
dungeon_map.print_map()
