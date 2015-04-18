class CantCastError(Exception):
    pass


class Entity():

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.weapon = None
        self.spell = None

    def get_health(self):
        return int(self.health)

    def get_mana(self):
        return int(self.mana)

    def is_alive(self):
        if self.health == 0:
            return False
        else:
            return True

    def can_cast(self):
        if self.mana == 0:
            return False
        else:
            return True

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        self.health += healing_points
        if self.health >= 100:
            self.health = 100

    def take_mana(self, mana_points):
        if self.mana + mana_points > 100:
            self.mana = 100
        else:
            self.mana += mana_points

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0
        return self.health

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by="None"):
        if by == "weapon":
            return self.damage + self.weapon.get_weapon_damage()
        if by == "magic":
            if self.mana < self.spell.get_spell_damage():
                raise CantCastError
            else:
                self.mana -= self.spell.get_spell_mana_cost()
                return self.damage + self.spell.get_spell_damage()

    def has_weapon(self):
        return self.weapon is not None

    def has_spell(self):
        return self.spell is not None
