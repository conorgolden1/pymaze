import sys
sys.path.append('../')
import random

from pymaze.graphic import Window
from pymaze.maze_builder import Maze



def main():
    win = Window(800, 600)
    num_rows = 12
    num_cols = 12
    width_margin_percent = .01
    height_margin_percent = .01
    maze = Maze(num_rows, num_cols, width_margin_percent,
                height_margin_percent, win, seed=random.randint(0, 100_000_000_000))
    maze.solve()
    print("Finished")
    win.wait_for_close()


if __name__ == "__main__":
    main()
