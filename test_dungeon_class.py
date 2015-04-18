from dungeon_class import Dungeon
from hero_class import Hero
import unittest


class TestDungeon(unittest .TestCase):

    def setUp(self):
        self.test_dungeon = Dungeon("level1")

    def test_init(self):
        # dungeon = Dungeon("level1")
        self.assertIsInstance(self.test_dungeon, Dungeon)

    # def test_print_map(self):
    #     # dungeon = Dungeon("level1")
    #     test_map = ["S.##.....T", "#T##..###.",
    #                 "#.###E###S", "#.E...###.", "###T#####G"]
    #     self.assertEqual(self.test_dungeon.print_map(), test_map)

    def test_spawn(self):
        pass

    def test_move_hero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.test_dungeon.spawn(h)
        self.assertFalse(self.test_dungeon.move_hero("down"))
        self.assertFalse(self.test_dungeon.move_hero("up"))
        self.assertTrue(self.test_dungeon.move_hero("right"))
        self.assertTrue(self.test_dungeon.move_hero("left"))


if __name__ == '__main__':
    unittest.main()
