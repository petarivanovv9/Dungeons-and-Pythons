from hero_class import Hero
from enemy_class import Enemy
from fight_class import Fight
from weapon_class import Weapon
from spell_class import Spell
import random


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
        self.treasure = {
                   "heal_potion": [25, 50, 75, 100],
                   "mana_potion": [25, 50, 75, 100],
                   }

    def generate_level(self):
        pass

    def pick_treasure(self):
        treasures = ["heal_potion", "mana_potion"]
        random_treasure = random.choice(treasures)

        if random_treasure == "heal_potion":
            health_points = random.choice(self.treasure[random_treasure])
            self.dungeon_hero.take_healing(health_points)
            print ("Found health potion. Hero health is {}.".format(
                self.dungeon_hero.get_health()))

        if random_treasure == "mana_potion":
            mana_points = random.choice(self.treasure[random_treasure])
            self.dungeon_hero.take_mana(mana_points)
            print ("Found mana potion. Hero mana is {}.".format(
                self.dungeon_hero.get_mana()))

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

    def can_make_move(self, coordinates):
        pass

    def move_consequence(self, position):
        pass

    def move_hero(self, direction):
        pass

    def hero_attack(self, by="None"):
        pass
