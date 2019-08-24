

from random import shuffle


class RandomGenerator:
    
    __DEFAULT_BAG = ["I", "J", "L", "O", "S", "T", "Z"]

    def __init__(self):
        self.__bag = None
        self.__refill_bag()

    def get_next_tetromino(self):
        if not self.__bag:
            self.__refill_bag()

        return self.__bag.pop(0)

    def __refill_bag(self):
        self.__bag = RandomGenerator.__DEFAULT_BAG.copy()
        shuffle(self.__bag)

