

from tetrominos.tetromino import Tetromino


class Z(Tetromino):

    DRAW_COORDS = [
        [
            (-1, -1),
            (0, -1),
            (0, 0),
            (1, 0)
        ],
        [
            (1, -1),
            (1, 0),
            (0, 0),
            (0, 1)
        ],
        [
            (-1, 0),
            (0, 0),
            (0, 1),
            (1, 1)
        ],
        [
            (0, -1),
            (0, 0),
            (-1, 0),
            (-1, 1)
        ]
    ]

    R_OFFSETS = [
        [
            (0, 0),
            (-1, 0),
            (-1, -1),
            (0, 2),
            (-1, 2)
        ],
        [
            (0, 0),
            (1, 0),
            (1, 1),
            (0, -2),
            (1, -2)
        ],
        [
            (0, 0),
            (1, 0),
            (1, -1),
            (0, 2),
            (1, 2)
        ],
        [
            (0, 0),
            (-1, 0),
            (-1, 1),
            (0, -2),
            (-1, -2)
        ]
    ]

    def __init__(self):
        super(Z, self).__init__(Z.DRAW_COORDS, Z.R_OFFSETS)
