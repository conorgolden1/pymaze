import unittest
from maze_builder import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(num_cols, num_rows)
        self.assertEqual(
                len(m1.cells),
                num_cols,
        )
        self.assertEqual(
                len(m1.cells[0]),
                num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 1000
        num_rows = 1000
        m1 = Maze(num_cols, num_rows)
        self.assertEqual(
                len(m1.cells),
                num_cols,
        )
        self.assertEqual(
                len(m1.cells[0]),
                num_rows,
        )

    def test_maze_create_cells_zero(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(num_cols, num_rows)
        self.assertEqual(
                len(m1.cells),
                num_cols,
        )
        self.assertEqual(
                len(m1.cells),
                num_rows,
        )

    def test_maze_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(num_cols, num_rows)
        entrance_cell = m1.cells[0][0]
        exit_cell = m1.cells[self.num_cols - 1][self.num_rows - 1]
        self.assertFalse(
                entrance_cell.has_left_wall
        )
        self.assertFalse(
                exit_cell.has_bottom_wall
        )



if __name__ == "__main__":
    unittest.main()
