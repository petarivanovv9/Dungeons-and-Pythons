from entity_class import Entity


class Enemy(Entity):
    def __init__(self, damage, health=100, mana=100):
        Entity.__init__(self, health, mana)
        self.damage = damage

    def is_alive(self):
        return Entity.is_alive(self)

    def can_cast(self):
        return Entity.can_cast(self)

    def get_health(self):
        return Entity.get_health(self)

    def get_mana(self):
        return Entity.get_mana(self)

    def take_healing(self, healing_points):
        return Entity.take_healing(self, healing_points)

    def take_mana(self, mana_points):
        return Entity.take_mana(self, mana_points)

    def take_damage(self, damage_points):
        return Entity.take_damage(self, damage_points)
