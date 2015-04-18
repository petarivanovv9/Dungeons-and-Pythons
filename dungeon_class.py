from hero_class import Hero


class Dungeon:

    def __init__(self, filename):
        with open(filename, "r") as in_file:
            lines = in_file.read().splitlines()
            self.dungeon_map = []
            for line in lines:
                self.dungeon_map.append(list(line))

    def print_map(self):
        result = []
        for line in self.dungeon_map:
            result.append(''.join(line))
            # print (''.join(line))
        return result

    def spawn(self, hero):
        counter = 0
        for i in range(0, len(self.dungeon_map)):
            for j in range(0, len(self.dungeon_map[i])):
                if self.dungeon_map[i][j] == "S" and counter < 1:
                    counter += 1
                    self.dungeon_map[i][j] = "H"
                    self.hero_x = i
                    self.hero_y = j

    def move_hero(self, direction="None"):
        rows = len(self.dungeon_map)
        cols = len(self.dungeon_map[0])

        if direction == "up":
            if self.hero_x - 1 >= 0 and self.dungeon_map[self.hero_x - 1][self.hero_y] != "#":
                self.dungeon_map[self.hero_x][self.hero_y] = "."
                self.hero_x -= 1
                self.dungeon_map[self.hero_x][self.hero_y] = "H"
                return True
            else:
                return False

        if direction == "down":
            if self.hero_x + 1 < rows and self.dungeon_map[self.hero_x + 1][self.hero_y] != "#":
                self.dungeon_map[self.hero_x][self.hero_y] = "."
                self.hero_x += 1
                self.dungeon_map[self.hero_x][self.hero_y] = "H"
                return True
            else:
                return False

        if direction == "right":
            if self.hero_y + 1 < cols and self.dungeon_map[self.hero_x][self.hero_y + 1] != "#":
                self.dungeon_map[self.hero_x][self.hero_y] = "."
                self.hero_y += 1
                self.dungeon_map[self.hero_x][self.hero_y] = "H"
                return True
            else:
                return False

        if direction == "left":
            if self.hero_y - 1 >= 0 and self.dungeon_map[self.hero_x][self.hero_y - 1] != "#":
                self.dungeon_map[self.hero_x][self.hero_y] = "."
                self.hero_y -= 1
                self.dungeon_map[self.hero_x][self.hero_y] = "H"
                return True
            else:
                return False

        return False


# h = Hero(name="Bron", title="Dragonslayer", health=100,
#          mana=100, mana_regeneration_rate=2)

# dungeon_map = Dungeon("level1")
# dungeon_map.print_map()
# dungeon_map.spawn(h)
# print (10 * '-')
# dungeon_map.print_map()
# print (10 * '-')
# print (dungeon_map.move_hero("down"))
# dungeon_map.print_map()
# print (10 * '-')
# print (dungeon_map.move_hero("up"))
# dungeon_map.print_map()
# print (10 * '-')
# print (dungeon_map.move_hero("right"))
# dungeon_map.print_map()
# print (10 * '-')
# print (dungeon_map.move_hero("left"))
# dungeon_map.print_map()
