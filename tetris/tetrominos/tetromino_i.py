

from tetrominos.tetromino import Tetromino


class I(Tetromino):

    DRAW_COORDS = [
        [
            (-1, 0),
            (0, 0),
            (1, 0),
            (2, 0)
        ],
        [
            (1, -1),
            (1, 0),
            (1, 1),
            (1, 2)
        ],
        [
            (-1, 1),
            (0, 1),
            (1, 1),
            (2, 1)
        ],
        [
            (0, -1),
            (0, 0),
            (0, 1),
            (0, 2)
        ]
    ]

    R_OFFSETS = [
        [
            (0, 0),
            (-2, 0),
            (1, 0),
            (-2, 1),
            (1, -2)
        ],
        [
            (0, 0),
            (-1, 0),
            (-2, 0),
            (-1, -2),
            (2, 1)
        ],
        [
            (0, 0),
            (2, 0),
            (-1, 0),
            (2, -1),
            (-1, 2)
        ],
        [
            (0, 0),
            (1, 0),
            (-2, 0),
            (1, 2),
            (-2, -1)
        ]
    ]

    def __init__(self):
        super(I, self).__init__(I.DRAW_COORDS, I.R_OFFSETS)

