class Entity():
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

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
