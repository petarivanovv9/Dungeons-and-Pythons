class Weapon:

    def __init__(self, name, damage):
        self.weapon_name = name
        self.weapon_damage = damage

    def get_weapon_name(self):
        return self.weapon_name

    def get_weapon_damage(self):
        return self.weapon_damage
