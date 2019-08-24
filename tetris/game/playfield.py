

class Playfield:

    # self.__grid values
    # 0 : empty space
    # -1 : falling tetromino
    # 1 : fallen in place tetrominos
    # 2 : wall
    
    W = 12
    H_BUFFER = 2
    H_FIELD = 21
    H = H_BUFFER + H_FIELD
    DEFAULT_X = W // 2 - 1
    DEFAULT_Y = H_BUFFER

    def __init__(self):
        self.grid = Playfield.generate_grid()
        self.w = Playfield.W
        self.h = Playfield.H
        self.h_field = Playfield.H_FIELD
        self.h_buffer = Playfield.H_BUFFER
        self.x = Playfield.DEFAULT_X
        self.y = Playfield.DEFAULT_Y

    def update_position(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def reset_position(self):
        self.x = Playfield.DEFAULT_X
        self.y = Playfield.DEFAULT_Y

    def clear_line_at(self, idx):
        for i in range(idx + self.h_buffer - 1, self.h_buffer - 1, -1):
            for j in range(1, self.w - 1):
                self.grid[i + 1][j] = self.grid[i][j]

        for i in range(1, self.w - 1):
            self.grid[self.h_buffer][i] = 0

    def locate_full_lines(self):
        idx = []

        for i in range(19, -1, -1):
            full = True
            for j in range(1, self.w - 1):
                if self.grid[i + self.h_buffer][j] == 0:
                    full = False

            if full:
                idx.append(i)

        return idx

    def print_grid(self):
        for i in range(self.h):
            for j in range(self.w):
                print(self.grid[i][j], end="")
            print()

    @staticmethod
    def generate_grid():
        line = [0 for _ in range(Playfield.W)]
        grid = [line.copy() for i in range(Playfield.H)]

        for i in range(Playfield.H_BUFFER, Playfield.H):
            grid[i][0] = 2
            grid[i][Playfield.W - 1] = 2

        for i in range(Playfield.W):
            grid[Playfield.H - 1][i] = 2
        
        return grid

