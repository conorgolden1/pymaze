from tkinter import Tk, BOTH, Canvas
import random
import math
import time


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=width,
                             height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()
        print("Closing Window")

    def close(self):
        self.window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Maze():
    def __init__(self, num_rows, num_cols, width_margin_percent=.10, height_margin_percent=.10, win=None, seed=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.width_margin = math.floor(win.width * width_margin_percent)
        self.height_margin = math.floor(win.height * height_margin_percent)
        self.cell_height = (win.height - (self.height_margin * 2)) // num_cols
        self.cell_width = (win.width - (self.width_margin * 2)) // num_rows
        self.cells = []
        self.win = win
        if not seed:
            self.seed = random.seed(0)
        else:
            self.seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for x in range(self.num_rows):
            self.cells.append([])
            for y in range(self.num_cols):
                point_a = Point(self.width_margin + (x * self.cell_width),
                                self.height_margin + (y * self.cell_height))
                point_b = Point(self.width_margin + ((x + 1) * self.cell_width),
                                self.height_margin + ((y + 1) * self.cell_height))
                cell = Cell(point_a, point_b, self.win)
                cell.draw(draw_maze=True)
                self.cells[x].append(Cell(point_a, point_b, self.win))

    def _break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        entrance_cell.has_left_wall = False

        exit_cell = self.cells[self.num_rows - 1][self.num_cols - 1]
        exit_cell.has_bottom_wall = False
        entrance_cell.draw()
        exit_cell.draw()

    def _break_walls_r(self, x, y):
        self.cells[x][y].visited = True
        while True:
            to_visit = []
            if x > 0 and not self.cells[x - 1][y].visited:
                to_visit.append("left")
            if y > 0 and not self.cells[x][y - 1].visited:
                to_visit.append("up")
            if y < self.num_cols - 1 and not self.cells[x][y + 1].visited:
                to_visit.append("down")
            if x < self.num_rows - 1 and not self.cells[x + 1][y].visited:
                to_visit.append("right")

            if len(to_visit) == 0:
                self.cells[x][y].draw()
                return

            random_direction = to_visit[random.randint(0, len(to_visit) - 1)]
            if random_direction == "left":
                self.cells[x][y].has_left_wall = False
                self.cells[x - 1][y].has_right_wall = False
                self._break_walls_r(x - 1, y)
            elif random_direction == "right":
                self.cells[x][y].has_right_wall = False
                self.cells[x + 1][y].has_left_wall = False
                self._break_walls_r(x + 1, y)
            elif random_direction == "up":
                self.cells[x][y].has_top_wall = False
                self.cells[x][y - 1].has_bottom_wall = False
                self._break_walls_r(x, y - 1)
            else:
                self.cells[x][y].has_bottom_wall = False
                self.cells[x][y + 1].has_top_wall = False
                self._break_walls_r(x, y + 1)

    def _reset_cells_visited(self):
        for x in range(self.num_rows):
            for y in range(self.num_cols):
                self.cells[x][y].visited = False

    def solve(self):
        self.solve_r(0, 0)

    def solve_r(self, x, y):
        current = self.cells[x][y]
        current._animate()
        current.visited = True

        if x == self.num_rows - 1 and y == self.num_cols - 1:
            print("Solved!")
            return True

        directions = ["left", "right", "up", "down"]
        random.shuffle(directions)

        for direction in directions:
            if direction == "left" and not (x == 0 and y == 0) and not current.has_left_wall and not self.cells[x - 1][y].visited:
                current.draw_move(self.cells[x - 1][y])
                if self.solve_r(x - 1, y):
                    return True
                else:
                    current.draw_move(self.cells[x - 1][y], undo=True)
            elif direction == "right" and not current.has_right_wall and not self.cells[x + 1][y].visited:
                current.draw_move(self.cells[x + 1][y])
                if self.solve_r(x + 1, y):
                    return True
                else:
                    current.draw_move(self.cells[x + 1][y], undo=True)
            elif direction == "up" and not current.has_top_wall and not self.cells[x][y - 1].visited:
                current.draw_move(self.cells[x][y - 1])
                if self.solve_r(x, y - 1):
                    return True
                else:
                    current.draw_move(self.cells[x][y - 1], undo=True)
            elif not current.has_bottom_wall and not self.cells[x][y + 1].visited:
                current.draw_move(self.cells[x][y + 1])
                if self.solve_r(x, y + 1):
                    return True
                else:
                    current.draw_move(self.cells[x][y + 1], undo=True)

        return False


class Cell():

    def __init__(self, point_a, point_b, window, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.visited = False
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = point_a.x
        self._x2 = point_b.x
        self._y1 = point_a.y
        self._y2 = point_b.y
        self._win = window

    def _animate(self, draw_maze=False):
        self._win.redraw()
        if not draw_maze:
            time.sleep(0.02)

    def draw(self, draw_maze=False):
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")
        self._animate(draw_maze)

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        line = Line(self.get_center_cord(), to_cell.get_center_cord())
        self._win.draw_line(line, fill_color)

    def get_center_cord(self):
        x_cord = self._x1 + ((self._x2 - self._x1) // 2)
        y_cord = self._y1 + ((self._y2 - self._y1) // 2)
        return Point(x_cord, y_cord)


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_a.x, self.point_a.y,
                           self.point_b.x, self.point_b.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)
