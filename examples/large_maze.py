import sys
sys.path.append('../')
import random

from pymaze.graphic import Window
from pymaze.maze_builder import Maze


def main():
    win = Window(1400, 1200)
    num_rows = 50
    num_cols = 50
    width_margin_percent = .01
    height_margin_percent = .01
    sys.setrecursionlimit(12000)
    maze = Maze(num_rows, num_cols, width_margin_percent,
                height_margin_percent, win, seed=random.randint(0, 100_000_000_000))
    maze.solve()
    print("Finished")
    win.wait_for_close()


if __name__ == "__main__":
    main()
