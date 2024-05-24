# README

## Overview
This repository contains a Python project that constructs and solves mazes using the Tkinter library for graphical representation. The project includes modules for creating the maze, displaying it, and solving it visually.

## Repository Structure
```
examples/
├── large_maze.py
├── medium_maze.py
├── small_maze.py
pymaze/
├── graphic.py
├── maze_builder.py
screenshots/
├── pymaze_screenshot.png
tests/
├── tests.py
README.md
```

### Key Components
- **examples/**: Contains example scripts for generating and solving different sizes of mazes.
  - `large_maze.py`
  - `medium_maze.py`
  - `small_maze.py`
- **pymaze/**: Core library for maze construction and graphical representation.
  - `graphic.py`: Handles graphical elements and drawing using Tkinter.
  - `maze_builder.py`: Contains the `Maze` and `Cell` classes for maze generation and solving.
- **screenshots/**: Contains screenshots of the maze application.
  - `pymaze_screenshot.png`
- **tests/**: Contains unit tests for the maze generation functionality.
  - `tests.py`
- **README.md**: This file.

## Setup and Usage

### Prerequisites
- Python 3.x
- Tkinter library (usually included with standard Python installations)

### Running Examples
Navigate to the `examples` directory and run any of the provided example scripts:
```sh
python3 examples/small_maze.py
```
You can also run `medium_maze.py` and `large_maze.py` in a similar fashion.

### Running Tests
Navigate to the `tests` directory and run the test suite using:
```sh
python3 tests/tests.py
```

## Code Overview

### maze_builder.py
The `Maze` class is responsible for creating the maze structure. It initializes with parameters for the number of rows and columns, and optional margins. The maze is generated using a recursive backtracking algorithm.

Key methods:
- `_create_cells()`: Initializes the grid of cells.
- `_break_entrance_and_exit()`: Creates openings for the entrance and exit of the maze.
- `_break_walls_r(x, y)`: Recursively removes walls to form the maze path.
- `_reset_cells_visited()`: Resets the visited status of all cells, used before solving the maze.
- `solve()`: Initiates the maze-solving process.
- `solve_r(x, y)`: Recursively solves the maze using depth-first search.

### tests.py
The `Tests` class uses the `unittest` framework to verify the correct creation of the maze, including the correct number of cells and the proper placement of the entrance and exit.

## Contributions
Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License.

---

This repository provides an interactive and visual approach to understanding maze generation and solving algorithms using Python and Tkinter.
