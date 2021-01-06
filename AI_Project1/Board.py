from Node import *
from State import *


class Board:

    def __init__(self, is_goal):
        self.is_goal = is_goal
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.zero_tile = None
        self.current = []
        self.goal = []


    def populate_board(self, args):
        insert_count = 0

        for i in range(0, 3):
            for j in range(0, 3):
                node = Node(args[insert_count])
                self.board[i][j] = node
                self.current.append(self.board[i][j].get_value())
                if self.board[i][j].get_value() == 0:
                    self.zero_tile = self.board[i][j]
                insert_count = insert_count + 1

        for i in range(0, 3):
            for j in range(0, 3):
                if i == 0 and j == 0:
                    self.board[i][j].set_down(self.board[i+1][j])
                    self.board[i][j].set_right(self.board[i][j+1])
                elif i == 1 and j == 0:
                    self.board[i][j].set_up(self.board[i-1][j])
                    self.board[i][j].set_right(self.board[i][j+1])
                    self.board[i][j].set_down(self.board[i+1][j])
                elif i == 2 and j == 0:
                    self.board[i][j].set_up(self.board[i-1][j])
                    self.board[i][j].set_right(self.board[i][j+1])
                elif i == 0 and j == 1:
                    self.board[i][j].set_down(self.board[i+1][j])
                    self.board[i][j].set_right(self.board[i][j+1])
                    self.board[i][j].set_left(self.board[i][j-1])
                elif i == 1 and j == 1:
                    self.board[i][j].set_up(self.board[i-1][j])
                    self.board[i][j].set_down(self.board[i+1][j])
                    self.board[i][j].set_left(self.board[i][j-1])
                    self.board[i][j].set_right(self.board[i][j+1])
                elif i == 2 and j == 1:
                    self.board[i][j].set_up(self.board[i-1][j])
                    self.board[i][j].set_left(self.board[i][j-1])
                    self.board[i][j].set_right(self.board[i][j+1])
                elif i == 0 and j == 2:
                    self.board[i][j].set_left(self.board[i][j-1])
                    self.board[i][j].set_down(self.board[i+1][j])
                elif i == 1 and j == 2:
                    self.board[i][j].set_left(self.board[i][j-1])
                    self.board[i][j].set_up(self.board[i-1][j])
                    self.board[i][j].set_down(self.board[i+1][j])
                elif i == 2 and j == 2:
                    self.board[i][j].set_up(self.board[i-1][j])
                    self.board[i][j].set_left(self.board[i][j-1])

    def set_goal(self, goal):
        self.goal = goal

    def get_goal(self):
        return self.goal

    def get_value(self):
        Node.get_value()

    def set_value(self, value):
        Node.set_value(value)

    def get_misplaced(self):
        Node.misplaced()

    def set_misplaced(self, misplaced):
        Node.set_misplaced(misplaced)

    def get_node(self, value):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j].get_value() == value:
                    return self.board[i][j]

    def print_board(self):

        print("[" + str(self.current[0]) + "] [" + str(self.current[1]) + "] [" + str(self.current[2]) + "]")
        print("[" + str(self.current[3]) + "] [" + str(self.current[4]) + "] [" + str(self.current[5]) + "]")
        print("[" + str(self.current[6]) + "] [" + str(self.current[7]) + "] [" + str(self.current[8]) + "]")

    def feed(self):
        count = 0
        mis = self.count_mis(self.goal)
        state = State(self.current, mis)

        if self.zero_tile.get_up() is not None:
            x = self.move(self.zero_tile.get_up())  # next state
            x.set_previous(state)
            state.next_state.append(x)
            for i in range(0, 3):
                for j in range(0, 3):
                    self.board[i][j].set_value(self.current[count])
                    count = count + 1
            count = 0

        if self.zero_tile.get_down() is not None:
            y = self.move(self.zero_tile.get_down())
            y.set_previous(state)
            state.next_state.append(y)
            for i in range(0, 3):
                for j in range(0,3):
                    self.board[i][j].set_value(self.current[count])
                    count = count + 1
            count = 0

        if self.zero_tile.get_right() is not None:
            z = self.move(self.zero_tile.get_right())
            z.set_previous(state)
            state.next_state.append(z)
            for i in range(0, 3):
                for j in range(0,3):
                    self.board[i][j].set_value(self.current[count])
                    count = count + 1
            count = 0

        if self.zero_tile.get_left() is not None:
            w = self.move(self.zero_tile.get_left())
            w.set_previous(state)
            state.next_state.append(w)
            for i in range(0, 3):
                for j in range(0,3):
                    self.board[i][j].set_value(self.current[count])
                    count = count + 1

            count = 0

        return state

    def update(self, state):
        insert_count = 0
        self.current = state.state
        for i in range(0, 3):
            for j in range(0, 3):
                node = Node(state.state[insert_count])
                self.board[i][j] = node
                if self.board[i][j].get_value() == 0:
                    self.zero_tile = self.board[i][j]
                insert_count = insert_count + 1

        for i in range(0, 3):
            for j in range(0, 3):
                if i == 0 and j == 0:
                    self.board[i][j].set_down(self.board[i + 1][j])
                    self.board[i][j].set_right(self.board[i][j + 1])
                elif i == 1 and j == 0:
                    self.board[i][j].set_up(self.board[i - 1][j])
                    self.board[i][j].set_right(self.board[i][j + 1])
                    self.board[i][j].set_down(self.board[i + 1][j])
                elif i == 2 and j == 0:
                    self.board[i][j].set_up(self.board[i - 1][j])
                    self.board[i][j].set_right(self.board[i][j + 1])
                elif i == 0 and j == 1:
                    self.board[i][j].set_down(self.board[i + 1][j])
                    self.board[i][j].set_right(self.board[i][j + 1])
                    self.board[i][j].set_left(self.board[i][j - 1])
                elif i == 1 and j == 1:
                    self.board[i][j].set_up(self.board[i - 1][j])
                    self.board[i][j].set_down(self.board[i + 1][j])
                    self.board[i][j].set_left(self.board[i][j - 1])
                    self.board[i][j].set_right(self.board[i][j + 1])
                elif i == 2 and j == 1:
                    self.board[i][j].set_up(self.board[i - 1][j])
                    self.board[i][j].set_left(self.board[i][j - 1])
                    self.board[i][j].set_right(self.board[i][j + 1])
                elif i == 0 and j == 2:
                    self.board[i][j].set_left(self.board[i][j - 1])
                    self.board[i][j].set_down(self.board[i + 1][j])
                elif i == 1 and j == 2:
                    self.board[i][j].set_left(self.board[i][j - 1])
                    self.board[i][j].set_up(self.board[i - 1][j])
                    self.board[i][j].set_down(self.board[i + 1][j])
                elif i == 2 and j == 2:
                    self.board[i][j].set_up(self.board[i - 1][j])
                    self.board[i][j].set_left(self.board[i][j - 1])

        return self

    def move(self, des): # generate next possible move

        temp = des.get_value()  # new zero value
        new = self.get_node(des.get_value())  # new zero location
        self.zero_tile.set_value(temp) # set zero value to new value
        new.set_value(0)


        x = []
        for i in range(0, 3):
            for j in range(0, 3):
                x.append(self.board[i][j].get_value())

        mis_count = self.count_mis(self.goal)
        state = State(x, mis_count)
        return state

    def count_mis(self, goal):
        count = 0
        mis = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j].get_value() != goal[count]:
                    self.board[i][j].set_misplaced(False)
                    count = count + 1
                    mis = mis + 1
                else:
                    self.board[i][j].set_misplaced(True)
                    count = count + 1
        return mis


    def test_goal(self):
        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current[count] != self.goal[count]:
                    self.board[i][j].set_misplaced(False)
                else:
                    self.board[i][j].set_misplaced(True)

        if self.current == self.goal:
            return True
        else:
            return False

        #goal_val = True
        #for i in range(0, 3):
            #for j in range(0, 3):
                #if self.board[i][j].get_value() != goal.board[i][j].get_value():
                    #goal_val = False
        #return goal_val






















