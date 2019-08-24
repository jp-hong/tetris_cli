

import sys
import time
from tools.cursor_control import print_at


class DisplayManager:

    W_FRAME = 24
    H_FRAME = 23
    REFRESH_RATE = 60

    def __init__(self):
        self.frame = DisplayManager.init_frame()
        self.conv_x = lambda x : x * 2
        self.conv_y = lambda y : y
        self.display_guides = False

    @staticmethod
    def init_frame():
        line = [" " for _ in range(DisplayManager.W_FRAME)]
        frame = [line.copy() for _ in range(DisplayManager.H_FRAME)]

        for i in range(2, 23):
            frame[i][1] = "X"
            frame[i][DisplayManager.W_FRAME - 2] = "X"

        for i in range(2, DisplayManager.W_FRAME - 2):
            frame[DisplayManager.H_FRAME - 1][i] = "X"

        return frame

    def update_frame(self, p):
        for i in range(p.h - 1):
            y = self.conv_y(i)

            for j in range(1, p.w - 1):
                x = self.conv_x(j)

                if p.grid[i][j] == 0:
                    self.frame[y][x] = " "
                    self.frame[y][x + 1] = " "

                elif p.grid[i][j] == -1 or p.grid[i][j] == 1:
                    self.frame[y][x] = "["
                    self.frame[y][x + 1] = "]"

    def display_frame(self, lines_cleared):
        f = ""

        for line in self.frame:
            f += ("".join(line) + "\n")
        
        f += ("\n   LINES CLEARED : " + str(lines_cleared) + "\n")
        print_at(0, 0, f)
    
    def refresh(self, p, lines_cleared):
        self.update_frame(p)
        self.display_frame(lines_cleared)

    def pace_frame(self, start, end):
        delta = end - start
        time.sleep(max(0, 1.0 / DisplayManager.REFRESH_RATE - delta))

