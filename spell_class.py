class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.spell_name = name
        self.spell_damage = damage
        self.spell_mana_cost = mana_cost
        self.spell_cast_range = cast_range

    def get_spell_name(self):
        return self.spell_name

    def get_spell_damage(self):
        return self.spell_damage
