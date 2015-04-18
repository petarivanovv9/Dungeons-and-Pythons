class Weapon:

    def __init__(self, name, damage):
        self.weapon_name = name
        self.weapon_damage = damage

    def get_weapon_name(self):
        return str(self.weapon_name)

    def get_weapon_damage(self):
        return int(self.weapon_damage)

    def __repr__(self):
        return "{} - {} damage".format(self.weapon_name, self.weapon_damage)
