import random
import copy
from Node import *


class World:

    def __init__(self, width = None, height = None):
        if width is None:
            self.width = int(input("How wide and tall should this grid be (this is for both the x and y values): "))
        else:
            self.width = width

        if height is None:
            self.height = self.width
        else:
            self.height = height

        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]
        self.sum_dis = 0
        self.h1 = None
        self.h2 = None

    def populate(self, house):  # parameter house is the number of house to be placed on the grid
        for i in range(0, 2):
            node_width = random.randrange(0, self.width)
            node_height = random.randrange(0, self.height)
            node = Node(node_width, node_height, "H")
            if self.grid[node_width][node_height] == 0:
                self.grid[node_width][node_height] = node
                if self.h1 is None:
                    self.h1 = node
                elif self.h2 is None:
                    self.h2 = node
            else:
                while self.grid[node_width][node_height] != 0:
                    node_width = random.randrange(0, self.width)
                    node_height = random.randrange(0, self.height)
                    if self.grid[node_width][node_height] == 0:
                        self.grid[node_width][node_height] = node
                        if self.h1 is None:
                            self.h1 = node
                        elif self.h2 is None:
                            self.h2 = node
                        break

        for i in range(0, house):
            node_width = random.randrange(0, self.width)
            node_height = random.randrange(0, self.height)
            node = Node(node_width, node_height, "h")
            if self.grid[node_width][node_height] == 0:
                self.grid[node_width][node_height] = node
                node.set_dis(self.h1, self.h2)
            else:
                while self.grid[node_width][node_height] != 0:
                    node_width = random.randrange(0, self.width)
                    node_height = random.randrange(0, self.height)
                    node.set_x(node_width)
                    node.set_y(node_height)
                    if self.grid[node_width][node_height] == 0:
                        self.grid[node_width][node_height] = node
                        node.set_dis(self.h1, self.h2)
                        break
        self.sum_dis = self.get_sum_dis()

    def get_sum_dis(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.grid[i][j] != 0:
                    if self.grid[i][j].state == "h":
                        self.sum_dis = self.sum_dis + self.grid[i][j].dis

        return self.sum_dis

    def printer(self):
        print()
        i = 0
        for s in self.grid:
            while i < self.width:
                if isinstance(s[i], Node):
                    print(s[i].state, end=' ')
                    i += 1
                else:
                    print(s[i], end=' ')
                    i += 1
                if i == self.width:
                    print()
            i = 0
        print()

    def next(self, num):  # num: 0-7
        temp_world = World(self.width, self.height)
        temp_world.grid = copy.deepcopy(self.grid)
        temp_world.h1 = copy.deepcopy(self.h1)
        temp_world.h2 = copy.deepcopy(self.h2)

        if num == 0:  # moving h1 up
            if temp_world.h1.y == temp_world.height-1:
                return 0
            temp_world.grid[temp_world.h1.x][temp_world.h1.y] = 0
            temp_world.h1.y = temp_world.h1.y + 1
            if temp_world.grid[temp_world.h1.x][temp_world.h1.y] == 0:
                temp_world.grid[temp_world.h1.x][temp_world.h1.y] = temp_world.h1
            else:
                return 0
        elif num == 1:  # moving h1 right
            if temp_world.h1.x == temp_world.width-1:
                return 0
            temp_world.grid[temp_world.h1.x][temp_world.h1.y] = 0
            temp_world.h1.x = temp_world.h1.x + 1
            if temp_world.grid[temp_world.h1.x][temp_world.h1.y] == 0:
                temp_world.grid[temp_world.h1.x][temp_world.h1.y] = temp_world.h1
            else:
                return 0
        elif num == 2:  # moving h1 down
            if temp_world.h1.y == 0:
                return 0
            temp_world.grid[temp_world.h1.x][temp_world.h1.y] = 0
            temp_world.h1.y = temp_world.h1.y - 1
            if temp_world.grid[temp_world.h1.x][temp_world.h1.y] == 0:
                temp_world.grid[temp_world.h1.x][temp_world.h1.y] = temp_world.h1
            else:
                return 0
        elif num == 3:  # moving h1 left
            if temp_world.h1.x == 0:
                return 0
            temp_world.grid[temp_world.h1.x][temp_world.h1.y] = 0
            temp_world.h1.x = temp_world.h1.x - 1
            if temp_world.grid[temp_world.h1.x][temp_world.h1.y] == 0:
                temp_world.grid[temp_world.h1.x][temp_world.h1.y] = temp_world.h1
            else:
                return 0
        elif num == 4:  # moving h2 up
            if temp_world.h2.y == temp_world.height-1:
                return 0
            temp_world.grid[temp_world.h2.x][temp_world.h2.y] = 0
            temp_world.h2.y = temp_world.h2.y + 1
            if temp_world.grid[temp_world.h2.x][temp_world.h2.y] == 0:
                temp_world.grid[temp_world.h2.x][temp_world.h2.y] = temp_world.h2
            else:
                return 0
        elif num == 5:  # moving h2 right
            if temp_world.h2.x == temp_world.width-1:
                return 0
            temp_world.grid[temp_world.h2.x][temp_world.h2.y] = 0
            temp_world.h2.x = temp_world.h2.x + 1
            if temp_world.grid[temp_world.h2.x][temp_world.h2.y] == 0:
                temp_world.grid[temp_world.h2.x][temp_world.h2.y] = temp_world.h2
            else:
                return 0
        elif num == 6:  # moving h2 down
            if temp_world.h2.y == 0:
                return 0
            temp_world.grid[temp_world.h2.x][temp_world.h2.y] = 0
            temp_world.h2.y = temp_world.h2.y - 1
            if temp_world.grid[temp_world.h2.x][temp_world.h2.y] == 0:
                temp_world.grid[temp_world.h2.x][temp_world.h2.y] = temp_world.h2
            else:
                return 0
        elif num == 7:  # moving h2 left
            if temp_world.h1.x == 0:
                return 0
            temp_world.grid[temp_world.h2.x][temp_world.h2.y] = 0
            temp_world.h2.x = temp_world.h2.x - 1
            if temp_world.grid[temp_world.h2.x][temp_world.h2.y] == 0:
                temp_world.grid[temp_world.h2.x][temp_world.h2.y] = temp_world.h2
            else:
                return 0

        for i in range(temp_world.width):
            for j in range(temp_world.height):
                if temp_world.grid[i][j] != 0:
                    if temp_world.grid[i][j].state == "h":
                        temp_world.grid[i][j].set_dis(temp_world.h1, temp_world.h2)

        temp_world.sum_dis = temp_world.get_sum_dis()
        return temp_world

    def rand_restart(self):
        temp_world = World(self.width, self.height)
        temp_world.grid = copy.deepcopy(self.grid)
        temp_world.h1 = copy.deepcopy(self.h1)
        temp_world.h2 = copy.deepcopy(self.h2)

        temp_world.grid[temp_world.h1.x][temp_world.h1.y] = 0
        temp_world.grid[temp_world.h2.x][temp_world.h2.y] = 0

        for i in range(2):
            node_width = random.randrange(0, temp_world.width)
            node_height = random.randrange(0, temp_world.height)

            if temp_world.grid[node_width][node_height] == 0:
                if i == 0:
                    temp_world.h1.set_x(node_width)
                    temp_world.h1.set_y(node_height)
                    temp_world.grid[node_width][node_height] = temp_world.h1
                else:
                    temp_world.h2.set_x(node_width)
                    temp_world.h2.set_y(node_height)
                    temp_world.grid[node_width][node_height] = temp_world.h2
            else:
                while temp_world.grid[node_width][node_height] != 0:
                    node_width = random.randrange(0, temp_world.width)
                    node_height = random.randrange(0, temp_world.height)
                    if temp_world.grid[node_width][node_height] == 0:
                        if i == 0:
                            temp_world.h1.set_x(node_width)
                            temp_world.h1.set_y(node_height)
                            temp_world.grid[node_width][node_height] = temp_world.h1
                            break
                        else:
                            temp_world.h2.set_x(node_width)
                            temp_world.h2.set_y(node_height)
                            temp_world.grid[node_width][node_height] = temp_world.h2
                            break

        for i in range(temp_world.width):
            for j in range(temp_world.height):
                if temp_world.grid[i][j] != 0:
                    if temp_world.grid[i][j].state == "h":
                        temp_world.grid[i][j].set_dis(temp_world.h1, temp_world.h2)

        temp_world.sum_dis = temp_world.get_sum_dis()
        return temp_world
