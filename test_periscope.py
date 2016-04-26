import unittest
from periscope import Grid


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(2, 3)

    def test_placement_validity(self):
        self.assertEqual(self.grid._check_placement_validity(-1, 0), False)
        self.assertEqual(self.grid._check_placement_validity(2, 0), False)
        self.assertEqual(self.grid._check_placement_validity(0, -1), False)
        self.assertEqual(self.grid._check_placement_validity(0, 3), False)
        self.assertEqual(self.grid._check_placement_validity(0, 0), True)
        self.assertEqual(self.grid._check_placement_validity(0, 2), True)
        self.assertEqual(self.grid._check_placement_validity(1, 2), True)

    def test_place_dirt(self):
        self.grid.place_dirt(0, 0)
        self.assertEqual(self.grid.grid[(0, 0)], 0)
        self.assertEqual(self.grid.grid[(0, 1)], 1)
        self.grid.place_dirt(0, 1)
        self.assertEqual(self.grid.grid[(0, 1)], 0)
        self.grid.place_dirt(-1, 0)
        self.grid.place_dirt(0, +50)

    def test_count_dirt(self):
        self.grid.place_dirt(0, 0)
        self.assertEqual(self.grid.get_dirt_collected(), 0)
        self.grid.set_hoover_pos(0, 0)
        self.assertEqual(self.grid.get_dirt_collected(), 1)
        self.grid.set_hoover_pos(0, 0)
        self.grid.set_hoover_pos(0, 0)
        self.grid.set_hoover_pos(0, 0)
        self.grid.set_hoover_pos(0, 0)
        self.assertEqual(self.grid.get_dirt_collected(), 1)

    def test_hoover_placement(self):
        self.grid.set_hoover_pos(2, 0)
        self.assertEqual(self.grid.get_hoover_pos(), None)
        self.grid.set_hoover_pos(0, 1)
        self.assertEqual(self.grid.get_hoover_pos(), "0 1")

    def test_move_north(self):
        self.grid.set_hoover_pos(0, 0)
        self.assertEqual(self.grid.get_hoover_pos(), "0 0")
        self.grid.move_north()
        self.assertEqual(self.grid.get_hoover_pos(), "0 1")

    def test_move_south(self):
        self.grid.set_hoover_pos(0, 1)
        self.assertEqual(self.grid.get_hoover_pos(), "0 1")
        self.grid.move_south()
        self.assertEqual(self.grid.get_hoover_pos(), "0 0")

    def test_move_east(self):
        self.grid.set_hoover_pos(0, 1)
        self.assertEqual(self.grid.get_hoover_pos(), "0 1")
        self.grid.move_east()
        self.assertEqual(self.grid.get_hoover_pos(), "1 1")

    def test_move_west(self):
        self.grid.set_hoover_pos(1, 1)
        self.assertEqual(self.grid.get_hoover_pos(), "1 1")
        self.grid.move_west()
        self.assertEqual(self.grid.get_hoover_pos(), "0 1")



if __name__ == "__main__":
    unittest.main()
