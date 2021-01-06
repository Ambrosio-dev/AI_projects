#nodes for storing both the number and value of squares on the sudoku board


class Node:
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        if self.value == "0":
            self.domain = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        else:
            self.domain = None

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_value(self, val):
        self.value = val
