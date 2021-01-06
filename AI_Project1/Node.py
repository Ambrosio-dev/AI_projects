

class Node:

    def __init__(self, value=None):
        self.misplaced = True
        self.value = value
        self.up = None
        self.down = None
        self.right = None
        self.left = None

    def get_misplace(self):
        return self.misplaced

    def set_misplaced(self, misplaced):
        self.misplaced = misplaced

    def get_previous(self):
        return self.previous

    def set_previous(self, previous):
        self.previous = previous

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_up(self, node):
        self.up = node

    def set_down(self, node):
        self.down = node

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_up(self):
        return self.up

    def get_down(self):
        return self.down

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left
