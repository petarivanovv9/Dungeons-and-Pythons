from hero_class import Hero
from weapon_class import Weapon
from spell_class import Spell
import unittest


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.test_hero = Hero("Masturbarq", "the Great")

    def test_init(self):
        self.assertTrue(isinstance(self.test_hero, Hero))

    def test_known_as(self):
        result = "{} the {}".format(
            self.test_hero.hero_name, self.test_hero.hero_title)
        self.assertEqual(result, self.test_hero.known_as())

    def test_get_health(self):
        self.assertTrue(isinstance(self.test_hero.get_health(), int))

    def test_get_mana(self):
        self.assertTrue(isinstance(self.test_hero.get_mana(), int))

    def test_is_alive(self):
        self.assertTrue(self.test_hero.is_alive())

    def test_can_cast(self):
        pass

    def test_take_damage(self):
        pass

    def test_take_healing(self):
        pass

    def test_take_mana(self):
        pass

    def test_equip(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        self.test_hero.equip(w)
        self.assertIsInstance(self.test_hero.hero_weapon, Weapon)

    def test_learn(self):
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.test_hero.learn(s)
        self.assertIsInstance(self.test_hero.hero_spell, Spell)

    def test_attack(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.test_hero.equip(w)
        self.test_hero.learn(s)
        self.assertEqual(self.test_hero.attack(by="weapon"), 20)
        self.assertEqual(self.test_hero.attack(by="magic"), 30)


if __name__ == '__main__':
    unittest.main()
