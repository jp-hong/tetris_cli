

class Tetromino:

    def __init__(self, draw_coords, r_offsets):
        self.orientation = 0
        self.draw_coords = draw_coords
        self.r_offsets = r_offsets

    def rotate_clkwise(self):
        self.orientation = (self.orientation + 1) % 4

    def rotate_cnt_clkwise(self):
        self.orientation = (self.orientation - 1) % 4

    def reset_orientation(self):
        self.orientation = 0

    def next_o(self):
        return (self.orientation + 1) % 4

    def prev_o(self):
        return (self.orientation - 1) % 4

    def draw(self, grid, x, y, fix=False):
        grid_val = 1 if fix else -1

        for coord in self.draw_coords[self.orientation]:
            grid[y + coord[1]][x + coord[0]] = grid_val

    def erase(self, grid, x, y):
        for coord in self.draw_coords[self.orientation]:
            grid[y + coord[1]][x + coord[0]] = 0

    def can_draw(self, grid, x, y, o=-1):
        if o != -1:
            o_test = o
        else:
            o_test = self.orientation

        for coord in self.draw_coords[o_test]:
            if grid[y + coord[1]][x + coord[0]] > 0:
                return False

        return True

