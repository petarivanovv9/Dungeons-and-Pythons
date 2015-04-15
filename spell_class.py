class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.spell_name = name
        self.spell_damage = damage
        self.spell_mana_cost = mana_cost
        self.spell_cast_range = cast_range

    def get_spell_name(self):
        return str(self.spell_name)

    def get_spell_damage(self):
        return int(self.spell_damage)

    def get_spell_mana_cost(self):
        return int(self.spell_mana_cost)
