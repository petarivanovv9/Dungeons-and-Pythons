from entity_class import Entity


class Enemy(Entity):

    def __init__(self, damage, health=100, mana=100):
        Entity.__init__(self, health, mana, damage)

    def get_damage(self):
        return int(self.damage)

    def __str__(self):
        return "Enemy(hp:{}, mana:{}, damage:{})".format(
            self.health, self.mana, self.damage)

    def __repr__(self):
        return self.__str__()
