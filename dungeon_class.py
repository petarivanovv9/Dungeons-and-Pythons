from hero_class import Hero
from enemy_class import Enemy


class Dungeon:

    def __init__(self, filename):
        with open(filename, "r") as in_file:
            lines = in_file.read().splitlines()
            self.dungeon_map = []
            for line in lines:
                self.dungeon_map.append(list(line))
        # It's for level1.
        # Later, I'll generate random enemies for different levels.
        self.enemy1 = Enemy(5)
        self.enemy1_pos = (3, 2)
        self.enemy2 = Enemy(5)
        self.enemy2_pos = (2, 5)
        self.enemy3 = Enemy(10)
        self.enemy3_pos = (2, 9)

    def generate_level(self):
        pass

    def print_map(self):
        # result = []
        for line in self.dungeon_map:
            # result.append(''.join(line))
            print (''.join(line))
        # return result

    def spawn(self, hero):
        counter = 0
        for i in range(0, len(self.dungeon_map)):
            for j in range(0, len(self.dungeon_map[i])):
                if self.dungeon_map[i][j] == "S" and counter < 1:
                    counter += 1
                    self.dungeon_map[i][j] = "H"
                    self.dungeon_hero = hero
                    # self.hero_pos = (i, j)
                    self.hero_x = i
                    self.hero_y = j

    def check_enemy(self, current_x, current_y):
        if current_x == self.enemy1_pos[0] and current_y == self.enemy1_pos[1]:
            return self.enemy1
        if current_x == self.enemy2_pos[0] and current_y == self.enemy2_pos[1]:
            return self.enemy2
        if current_x == self.enemy3_pos[0] and current_y == self.enemy3_pos[1]:
            return self.enemy3

    def move_hero(self, direction="None"):
        rows = len(self.dungeon_map)
        cols = len(self.dungeon_map[0])

        if direction == "up":
            if self.hero_x - 1 >= 0 and self.dungeon_map[self.hero_x - 1][self.hero_y] != "#":
                if self.dungeon_map[self.hero_x - 1][self.hero_y] == "E":
                    # start battle
                    # if end of battle is True ... else exit
                    current_enemy = self.check_enemy(
                        self.hero_x - 1, self.hero_y)
                    print ("A fight is started between {} and {}".format(
                        self.dungeon_hero, current_enemy))
                    self.dungeon_map[self.hero_x][self.hero_y] = "."
                    self.hero_x -= 1
                    self.dungeon_map[self.hero_x][self.hero_y] = "H"
                    return True
                else:
                    self.dungeon_map[self.hero_x][self.hero_y] = "."
                    self.hero_x -= 1
                    self.dungeon_map[self.hero_x][self.hero_y] = "H"
                    return True
            else:
                return False

        if direction == "down":
            if self.hero_x + 1 < rows and self.dungeon_map[self.hero_x + 1][self.hero_y] != "#":
                if self.dungeon_map[self.hero_x + 1][self.hero_y] == "E":
                    # start battle
                    # if end of battle is True ... else exit
                    current_enemy = self.check_enemy(
                        self.hero_x + 1, self.hero_y)
                    print ("A fight is started between {} and {}".format(
                        self.dungeon_hero, current_enemy))
                    self.dungeon_map[self.hero_x][self.hero_y] = "."
                    self.hero_x += 1
                    self.dungeon_map[self.hero_x][self.hero_y] = "H"
                    return True
                else:
                    self.dungeon_map[self.hero_x][self.hero_y] = "."
                    self.hero_x += 1
                    self.dungeon_map[self.hero_x][self.hero_y] = "H"
                    return True
            else:
                return False

        if direction == "right":
            if self.hero_y + 1 < cols and self.dungeon_map[self.hero_x][self.hero_y + 1] != "#":
                if self.dungeon_map[self.hero_x][self.hero_y + 1] == "E":
                    # start battle
                    # if end of battle is True ... else exit
                    current_enemy = self.check_enemy(
                        self.hero_x, self.hero_y + 1)
                    print ("A fight is started between {} and {}".format(
                        self.dungeon_hero, current_enemy))
                    self.dungeon_map[self.hero_x][self.hero_y] = "."
                    self.hero_y += 1
                    self.dungeon_map[self.hero_x][self.hero_y] = "H"
                    return True
                else:
                    self.dungeon_map[self.hero_x][self.hero_y] = "."
                    self.hero_y += 1
                    self.dungeon_map[self.hero_x][self.hero_y] = "H"
                    return True
            else:
                return False

        if direction == "left":
            if self.hero_y - 1 >= 0 and self.dungeon_map[self.hero_x][self.hero_y - 1] != "#":
                if self.dungeon_map[self.hero_x][self.hero_y - 1] == "E":
                    # start battle
                    # if end of battle is True ... else exit
                    current_enemy = self.check_enemy(
                        self.hero_x, self.hero_y - 1)
                    print ("A fight is started between {} and {}".format(
                        self.dungeon_hero, current_enemy))
                    self.dungeon_map[self.hero_x][self.hero_y] = "."
                    self.hero_y -= 1
                    self.dungeon_map[self.hero_x][self.hero_y] = "H"
                    return True
                else:
                    self.dungeon_map[self.hero_x][self.hero_y] = "."
                    self.hero_y -= 1
                    self.dungeon_map[self.hero_x][self.hero_y] = "H"
                    return True
            else:
                return False

        return False

    def hero_attack(self, by="None"):
        pass


# h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
# mapp = Dungeon("level1")
# mapp.spawn(h)
# mapp.print_map()
# print (10 * "-")
# print (mapp.move_hero("right"))
# print (mapp.print_map())
# print (10 * "-")
# print (mapp.move_hero("down"))
# print (mapp.print_map())
# print (10 * "-")
# print (mapp.move_hero("down"))
# print (mapp.print_map())
# print (10 * "-")
# print (mapp.move_hero("down"))
# print (mapp.print_map())
# print (10 * "-")
# print (mapp.move_hero("down"))
# print (mapp.print_map())
# print (10 * "-")
# print (mapp.move_hero("right"))
# print (mapp.print_map())
# print (10 * "-")
# print (mapp.move_hero("right"))
# print (mapp.print_map())
# print (mapp.move_hero("right"))
# print (mapp.print_map())
# print (mapp.move_hero("down"))
# print (mapp.print_map())
