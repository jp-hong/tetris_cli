

from game.random_generator import RandomGenerator
from game.playfield import Playfield
from tetrominos.tetromino_i import I
from tetrominos.tetromino_j import J
from tetrominos.tetromino_l import L
from tetrominos.tetromino_o import O
from tetrominos.tetromino_s import S
from tetrominos.tetromino_t import T
from tetrominos.tetromino_z import Z


class GameLogic:

    def __init__(self):
        self.t_I = I()
        self.t_J = J()
        self.t_L = L()
        self.t_O = O()
        self.t_S = S()
        self.t_T = T()
        self.t_Z = Z()

        self.t_dic = {
            "I": self.t_I,
            "J": self.t_J,
            "L": self.t_L,
            "O": self.t_O,
            "S": self.t_S,
            "T": self.t_T,
            "Z": self.t_Z
        }

        self.t = None
        self.game_over = False
        self.base_vel = 8
        self.v_mul = 1.75
        self.distance = 0.0
        self.l_clr = 0
        self.lvl_up = 5
        self.rg = RandomGenerator()
        self.p = Playfield()

    def init_game(self):
        self.spawn_new_tetromino()

    def move_left(self):
        if self.t.can_draw(self.p.grid, self.p.x - 1, self.p.y):
            self.t.erase(self.p.grid, self.p.x, self.p.y)
            self.p.update_position(-1, 0)
            self.t.draw(self.p.grid, self.p.x, self.p.y)

    def move_right(self):
        if self.t.can_draw(self.p.grid, self.p.x + 1, self.p.y):
            self.t.erase(self.p.grid, self.p.x, self.p.y)
            self.p.update_position(1, 0)
            self.t.draw(self.p.grid, self.p.x, self.p.y)

    def move_down(self):
        if self.t.can_draw(self.p.grid, self.p.x, self.p.y + 1):
            self.t.erase(self.p.grid, self.p.x, self.p.y)
            self.p.update_position(0, 1)
            self.t.draw(self.p.grid, self.p.x, self.p.y)
        else:
            self.drop()

    def can_rotate_clkwise(self):
        for i in range(5):
            x_off, y_off = self.t.r_offsets[self.t.orientation][i]

            if self.t.can_draw(self.p.grid, self.p.x + x_off, self.p.y + y_off,
                                self.t.next_o()):
                return True, x_off, y_off

        return False, 0, 0

    def can_rotate_cnt_clkwise(self):
        for i in range(5):
            x_off, y_off = self.t.r_offsets[self.t.orientation][i]

            if self.t.can_draw(self.p.grid, self.p.x - x_off, self.p.y - y_off,
                               self.t.prev_o()):
                return True, -x_off, -y_off
            
        return False, 0, 0

    def rotate_clkwise(self):
        can_rotate, x_off, y_off = self.can_rotate_clkwise()

        if can_rotate:
            self.t.erase(self.p.grid, self.p.x, self.p.y)
            self.t.rotate_clkwise()
            self.p.update_position(x_off, y_off)
            self.t.draw(self.p.grid, self.p.x, self.p.y)

    def rotate_cnt_clkwise(self):
        can_rotate, x_off, y_off = self.can_rotate_cnt_clkwise()

        if can_rotate:
            self.t.erase(self.p.grid, self.p.x, self.p.y)
            self.t.rotate_cnt_clkwise()
            self.p.update_position(x_off, y_off)
            self.t.draw(self.p.grid, self.p.x, self.p.y)

    def drop(self):
        delta = 1

        while self.t.can_draw(self.p.grid, self.p.x, self.p.y + delta):
            delta += 1

        self.t.erase(self.p.grid, self.p.x, self.p.y)
        self.p.update_position(0, delta - 1)
        self.t.draw(self.p.grid, self.p.x, self.p.y, fix=True)
        self.clear_lines()
        self.game_over = self.spawn_new_tetromino()

    def clear_lines(self):
        idx = self.p.locate_full_lines()

        if idx:
            for i in range(len(idx)):
                idx[i] += i
            
            self.l_clr += len(idx)

            for i in idx:
                self.p.clear_line_at(i)

    def spawn_new_tetromino(self):
        self.t = self.t_dic[self.rg.get_next_tetromino()]

        self.t.reset_orientation()
        self.p.reset_position()

        if self.t.can_draw(self.p.grid, self.p.x, self.p.y):
            self.t.draw(self.p.grid, self.p.x, self.p.y)
            return False
        else:
            return True

    def freefall(self, start, end):
        velocity = self.base_vel * (self.v_mul ** (self.l_clr // self.lvl_up))
        delta = end - start
        self.distance += (velocity * delta)

        if self.distance > 1:
            self.move_down()
            self.distance = 0

