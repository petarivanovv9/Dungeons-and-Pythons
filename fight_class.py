from hero_class import Hero
from enemy_class import Enemy
from weapon_class import Weapon
from spell_class import Spell


class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def determine_damage_source(self):
        if self.hero.has_weapon() is True and self.hero.has_spell() is True:
            if self.hero.spell.get_spell_damage() >= self.hero.weapon.get_weapon_damage():
                if self.hero.get_mana() >= self.hero.spell.get_spell_mana_cost():
                    return "spell"
            return "weapon"
        elif self.hero.has_spell():
            if self.hero.get_mana() >= self.hero.spell.get_spell_mana_cost():
                return "spell"
        elif self.hero.has_weapon():
            return "weapon"

    def start_fight(self):
        print ("A fight is started between {} and {}".format(
            self.hero, self.enemy))

        while True:
            if self.determine_damage_source() == "spell":
                self.enemy.take_damage(self.hero.attack(by="magic"))
                print ("Hero casts a {}, hits enemy for {} dmg. Enemy health\
 is {}".format(self.hero.spell.get_spell_name(), self.hero.spell.get_spell_damage(
                ), self.enemy.get_health()))
            elif self.determine_damage_source() == "weapon":
                self.enemy.take_damage(self.hero.attack(by="weapon"))
                print ("Hero hits enemy with {} for {} dmg. Enemy health\
 is {}".format(self.hero.weapon.get_weapon_name(), self.hero.weapon.get_weapon_damage(
                ), self.enemy.get_health()))
            if self.enemy.is_alive() == False:
                print ("Enemy is dead!")
                return self.hero
            self.hero.take_damage(self.enemy.get_damage())
            print("Enemy hits hero for {} dmg. Hero health is {}".format(
                self.enemy.get_damage(), self.hero.get_health()))
            if self.hero.is_alive() == False:
                print ("Hero is dead!")
                return False


# h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
# w = Weapon(name="The Axe of Destiny", damage=20)
# h.equip(w)
# s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
# h.learn(s)
# e = Enemy(40)

# fight = Fight(h, e)
# print (fight.start_fight())
