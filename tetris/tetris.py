

import time
import os
from game.input_handler import InputHandler
from game.display_manager import DisplayManager
from game.game_logic import GameLogic
from tools.cursor_control import *


def main():

    hide_cursor()

    dm = DisplayManager()
    gl = GameLogic()
    gl.init_game()

    os.system("cls")

    while True:
        start = time.time()
        dm.refresh(gl.p, gl.l_clr)

        if gl.game_over:
            break

        key = InputHandler.get_key_press()

        if key == "LEFT":
            gl.move_left()
        elif key == "RIGHT":
            gl.move_right()
        elif key == "UP" or key == "X":
            gl.rotate_clkwise()
        elif key == "Z":
            gl.rotate_cnt_clkwise()
        elif key == "SPACE":
            gl.drop()
        elif key == "DOWN":
            gl.move_down()
        elif key == "ESC":
            return

        end = time.time()
        gl.freefall(start, end)

        end = time.time()
        dm.pace_frame(start, end)

    print("\n   G A M E    O V E R")

    show_cursor()

main()
