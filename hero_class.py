from weapon_class import Weapon
from spell_class import Spell


class CantCastError(Exception):
    pass

class Hero:
    def __init__(self,
                 name, title, health=100, mana=100, mana_regeneration_rate=2):
        self.hero_name = name
        self.hero_title = title
        self.hero_health = health
        self.hero_mana = mana
        self.hero_mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        message = "{} the {}"
        return message.format(self.hero_name, self.hero_title)

    def get_health(self):
        return int(self.hero_health)

    def get_mana(self):
        return int(self.hero_mana)

    def is_alive(self):
        if self.hero_health == 0:
            return False
        else:
            return True

    def can_cast(self):
        if self.hero_mana == 0:
            return False
        else:
            return True

    def take_damage(self, damage_points):
        self.hero_health -= damage_points
        if self.hero_health < 0:
            self.hero_health = 0

    def take_healing(self, healing_points):
        if self.hero_health == 0:
            return False
        self.hero_health += healing_points
        if self.hero_health >= 100:
            self.hero_health = 100

    def take_mana(self, mana_points):
        if self.hero_mana + mana_points > 100:
            self.hero_mana = 100
        else:
            self.hero_mana += mana_points

    def equip(self, weapon):
        self.hero_weapon = weapon

    def learn(self, spell):
        self.hero_spell = spell

    def attack(self, by="None"):
        if by == "weapon":
            return self.hero_weapon.get_weapon_damage()
        if by == "magic":
            if self.hero_mana < self.hero_spell.get_spell_damage():
                raise CantCastError
            else:
                self.hero_mana -= self.hero_spell.get_spell_mana_cost()
                return self.hero_spell.get_spell_damage()
