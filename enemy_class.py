from entity_class import Entity


class Enemy(Entity):
    def __init__(self, damage, health=100, mana=100):
        Entity.__init__(self, health, mana, damage)
        # self.enemy_damage = damage
