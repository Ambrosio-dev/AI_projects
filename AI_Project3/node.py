

class Node:

    def __init__(self, state):
        self.state = state
        self.path = False
        self.checked = False
        self.upCheck = False
        self.downCheck = False
        self.backCheck = False
        self.val = self.set_val()

    def set_val(self):
        if self.state == " ":
            return 0
        elif self.state == "M":
            return -1
        elif self.state == "H":
            return 1
