
class Node:

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.dis = 0

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_state(self, state):
        self.state = state

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_state(self):
        return self.state

    def get_dis(self, h1, h2):  #gets the dis from house node to hospital node.
        return self.dis

    def set_dis(self, h1, h2): # sets the dis from current house node to nearest hospital
        if self.x > h1.x:
            x_dis = self.x - h1.x
        else:
            x_dis = h1.x - self.x

        if self.y > h1.y:
            y_dis = self.y - h1.y
        else:
            y_dis = h1.y - self.y

        h1_dis = x_dis + y_dis

        if self.x > h2.x:
            x_dis = self.x - h2.x
        else:
            x_dis = h2.x - self.x

        if self.y > h2.y:
            y_dis = self.y - h2.y
        else:
            y_dis = h2.y - self.y

        h2_dis = x_dis + y_dis

        if h1_dis < h2_dis:
            self.dis = h1_dis
        else:
            self.dis = h2_dis
