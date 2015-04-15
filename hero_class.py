from entity_class import Entity
from weapon_class import Weapon
from spell_class import Spell


class CantCastError(Exception):
    pass


class Hero(Entity):
    def __init__(self,
                 name, title, health=100, mana=100, mana_regeneration_rate=2):
        Entity.__init__(self, health, mana)
        self.hero_name = name
        self.hero_title = title
        self.hero_mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        message = "{} the {}"
        return message.format(self.hero_name, self.hero_title)

    def get_health(self):
        return Entity.get_health(self)

    def get_mana(self):
        return Entity.get_mana(self)

    def is_alive(self):
        return Entity.is_alive(self)

    def can_cast(self):
        return Entity.can_cast(self)

    def take_damage(self, damage_points):
        return Entity.take_damage(self, damage_points)

    def take_healing(self, healing_points):
        return Entity.take_healing(self, healing_points)

    def take_mana(self, mana_points):
        return Entity.take_mana(self, mana_points)

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
