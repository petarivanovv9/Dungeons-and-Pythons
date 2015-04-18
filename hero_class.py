from entity_class import Entity


class Hero(Entity):

    def __init__(self,
                 name, title, health=100, mana=100, mana_regeneration_rate=2):
        Entity.__init__(self, health, mana, damage=0)
        self.hero_name = name
        self.hero_title = title
        self.hero_mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        message = "{} the {}"
        return message.format(self.hero_name, self.hero_title)
