import random
import json


class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.spell_name = name
        self.spell_damage = damage
        self.spell_mana_cost = mana_cost
        self.spell_cast_range = cast_range

    def __str__(self):
        return "Spell {} with damage {}, mana cost {}, cast range {}".format(self.spell_name, self.spell_damage, self.spell_mana_cost, self.spell_cast_range)

    @staticmethod
    def load_spell_from_file(filename):
        with open(filename) as f:
            contents = f.read()
            data = json.loads(contents)
            str_spell = data[random.randint(0, len(data) - 1)]
            return Spell(name=str_spell['name'], damage=str_spell['damage'], mana_cost=str_spell['mana_cost'], cast_range=str_spell['cast_range'])

    def prepare_json(self):
        data = {
            "name": self.spell_name,
            "damage": self.spell_damage,
            "mana_cost": self.spell_mana_cost,
            "cast_range": self.spell_cast_range
        }
        return data

    def save(self, filename):
        with open(filename, "w+") as f:
            f.write(json.dumps(self.prepare_json(), 4))

# Getters
    def get_spell_name(self):
        return str(self.spell_name)

    def get_spell_damage(self):
        return int(self.spell_damage)

    def get_spell_mana_cost(self):
        return int(self.spell_mana_cost)

    def get_spell_cast_range(self):
        return int(self.spell_cast_range)

    def __repr__(self):
        return "{} - {} damage {} mana".format(
            self.spell_name, self.spell_damage, self.spell_mana_cost)
