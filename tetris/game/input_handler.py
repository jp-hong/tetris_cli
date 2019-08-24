

from msvcrt import getch, kbhit


class InputHandler():

    CONTROLS = {
        27: "ESC",
        72: "UP",
        80: "DOWN",
        75: "LEFT",
        77: "RIGHT",
        32: "SPACE",
        122: "Z",
        120: "X",
        99: "C",
    }

    @staticmethod
    def get_key_press():
        if kbhit():
            key = ord(getch())

            if key == 224:
                key = ord(getch())

            return InputHandler.resolve_key(key)
        else:
            return None

    @staticmethod
    def resolve_key(key):
        if key in InputHandler.CONTROLS:
            return InputHandler.CONTROLS[key]
        else:
            return None

