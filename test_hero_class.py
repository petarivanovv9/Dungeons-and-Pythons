from hero_class import Hero
import unittest


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero("Masturbarq", "the Great")

    def test_init(self):
        self.assertTrue(isinstance(self.test_hero, Hero))

    def test_known_as(self):
        result = "{} the {}".format(self.test_hero_name, self.test_hero_title)
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
