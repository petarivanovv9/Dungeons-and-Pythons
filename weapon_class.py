import random
import json


class Weapon:

    def __init__(self, name, damage):
        self.weapon_name = name
        self.weapon_damage = damage

    def __str__(self):
        return "Weapon {} with damage {}".format(self.weapon_name, self.weapon_damage)

    def __repr__(self):
        return "{} - {} damage".format(self.weapon_name, self.weapon_damage)

    @staticmethod
    def load_weapon_from_file(filename):
        with open(filename) as f:
            contents = f.read()
            data = json.loads(contents)
            str_weapon = data[random.randint(0, len(data) - 1)]
            return Weapon(name=str_weapon['name'], damage=str_weapon['damage'])

    def prepare_json(self):
        data = {
            "name": self.weapon_name,
            "damage": self.weapon_damage
        }
        return data

    def save(self, filename):
        with open(filename, "w+") as f:
            f.write(json.dumps(self.prepare_json(), 4))

# Getters
    def get_weapon_name(self):
        return str(self.weapon_name)

    def get_weapon_damage(self):
        return int(self.weapon_damage)

