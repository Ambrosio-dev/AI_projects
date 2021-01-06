 from node import *
import copy


class Grid:

    def __init__(self, width=None, height=None):
        self.value = 0
        if width is None:
            self.width = int(input("How wide and tall should this grid be (this is for both the x and y values): "))
        else:
            self.width = width

        if height is None:
            self.height = self.width
        else:
            self.height = height
        self.grid = [["" for x in range(self.width)] for y in range(height)]

        self.grid = self.reset_grid()
        self.first = None
        self.win = False
        self.best = None
        self.next = []

    def reset_grid(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                if i % 2 != 0 and j % 2 == 0:
                    self.grid[i][j] = Node("H")
                elif i % 2 == 0 and j % 2 != 0:
                    self.grid[i][j] = Node("M")
                else:
                    self.grid[i][j] = Node(" ")
        return self.grid

    def get_who_moves_first(self, num):
        if num == 1:
            print("Human player moves first.")
            self.first = "H"
        elif num == 2:
            print("Machine player moves first.")
            self.first = "M"
        else:
            print("Invalid entry, human player moves first.")
            self.first = "H"

    def printer(self):
        print()
        i = 0
        j = 0
        k = 0
        print("  x ", end=' ')
        for k in range(0, self.width):
            print(k, end='  ')
            k += 1
        if k == self.width:
            print()
        k = 0
        print("y \\", end='  ')
        for k in range(0, self.width):
            print("-", end='  ')
            k += 1
        if k == self.width:
            print()
        for j in range(0, self.height):
            for i in range(0, self.width):
                if i == 0:
                    print(str(j) + " | ", end=' ')
                print(self.grid[i][j].state, end='  ')
                if i == self.width - 1:
                    print()
        print()

    def get_human_player_move(self):
        print("Please enter (x,y) coordinates for your move.")
        xV = False
        yV = False
        empty = False
        while not empty:
            while xV == False:
                turnX = turnX = input("Enter x: ")
                turnX = int(turnX)
                if turnX < self.width and turnX >= 0:
                    xV = True
                    break
                print("That value is outside of the board!")
            while yV == False:
                turnY = turnY = input("Enter y: ")
                turnY = int(turnY)
                if turnY < self.height and turnY >= 0:
                    yV = True
                    break
                print("That value is outside of the board!")
            print("You have selected (" + str(turnX) + "," + str(turnY) + ").")
            if self.grid[turnX][turnY].state == " ":
                self.grid[turnX][turnY].state = "H"
                empty = True
            else:
                print("That space is already occupied!")
                xV = False
                yV = False

    def get_next(self, level, max_depth):
        if level == max_depth:
            self.best = self
            return self

        if level % 2 == 0:  # M move
            for i in range(self.width):
                for j in range(self.height):
                    if self.grid[i][j].state == " ":
                        child = Grid(self.width, self.height)
                        child.grid = copy.deepcopy(self.grid)
                        child.grid[i][j] = Node("M")
                        child.update_values()
                        child.value = child.set_grid_value()  # determines value of the board
                        if self.best is None:
                            self.best = child
                        else:
                            if child.value < self.best.value:
                                self.best = child
                        self.next.append(child)
                        child.get_next(level+1, max_depth)
        else:  #H Move
            for i in range(self.width):
                for j in range(self.height):
                    if self.grid[i][j].state == " ":
                        child = Grid(self.width, self.height)
                        child.grid = copy.deepcopy(self.grid)
                        child.grid[i][j] = Node("H")
                        child.update_values()
                        child.value = child.set_grid_value()  # determines value of the board
                        if self.best is None:
                            self.best = child
                        else:
                            if child.value > self.best.value:
                                self.best = child
                        self.next.append(child)
                        child.get_next(level+1, max_depth)

    def set_grid_value(self):
        for i in range(self.width):
            for j in range(self.height):
                self.value += self.grid[i][j].val
        return self.value

    def update_values(self):
        for i in range(self.width):  # tiles on the board 1 point
            for j in range(self.height):
                if self.grid[i][j].state == " ":
                    self.grid[i][j].val = 0
                elif self.grid[i][j].state == "M":
                    self.grid[i][j].val = -1
                elif self.grid[i][j].state == "H":
                    self.grid[i][j].val = 1

        if self.grid[int((self.width-1)/2)][int((self.height-1)/2)].state == "M":
            self.grid[int((self.width-1)/2)][int((self.height-1)/2)].val -= 17
        if self.grid[int((self.width-1)/2)][int((self.height-1)/2)].state == "H":
            self.grid[int((self.width-1)/2)][int((self.height-1)/2)].val += 17

        for i in range(self.width):  # adjacent tiles (horizontal +-5, vertical +1
            for j in range(self.height):
                if self.grid[i][j].state == "M":
                    h_count = 0
                    for k in self.grid[j]:
                        if k.state == "H":
                            h_count += 1
                    if h_count == self.width-1:
                        self.grid[i][j].val -= 20
                    h_count = 0
                    for l in self.grid[i]:
                        if l.state == "H":
                            h_count += 1
                    if h_count == self.height-1:
                        self.grid[i][j].val -= 21
                    if i > 0:
                        back = self.grid[i - 1][j]
                        if back.state == "M":
                            self.grid[i][j].val -= 5
                    else:
                        self.grid[i][j].val -= 2
                    if i < self.width - 1:
                        front = self.grid[i + 1][j]
                        if front.state == "M":
                            self.grid[i][j].val -= 5
                    else:
                        self.grid[i][j].val -= 2
                    if j > 0:
                        down = self.grid[i][j - 1]
                        if down.state == "M":
                            self.grid[i][j].val -= 1
                    if j < self.height - 1:
                        up = self.grid[i][j + 1]
                        if up.state == "M":
                            self.grid[i][j].val -= 1
                elif self.grid[i][j].state == "H":
                    m_count = 0
                    for k in self.grid[j]:
                        if k.state == "M":
                            m_count += 1
                    if m_count == self.width-1:
                        self.grid[i][j].val += 20
                    m_count = 0
                    for l in self.grid[i]:
                        if l.state == "M":
                            m_count += 1
                    if m_count == self.height-1:
                        self.grid[i][j].val += 21
                    if i > 0:
                        back = self.grid[i - 1][j]
                        if back.state == "H":
                            self.grid[i][j].val += 5
                    else:
                        self.grid[i][j].val += 2
                    if i < self.width - 1:
                        front = self.grid[i + 1][j]
                        if front.state == "H":
                            self.grid[i][j].val += 5
                    else:
                        self.grid[i][j].val += 5
                    if j > 0:
                        down = self.grid[i][j - 1]
                        if down.state == "H":
                            self.grid[i][j].val += 1
                    if j < self.height - 1:
                        up = self.grid[i][j + 1]
                        if up.state == "H":
                            self.grid[i][j].val += 1

    def generate_computer_player_move(self):  # still working here
        temp = Grid(self.width, self.height)
        temp.grid = copy.deepcopy(self.grid)
        temp.value = self.value  # determines value of the board
        temp.get_next(0, 3)  # generates all possible moves 3 turns ahead
        v = temp.minimax(temp, 0, float("-inf"), float("inf"))

        for i in temp.next:
            if i.value == v:
                self.grid = i.grid

    def minimax(self, state, level, alpha, beta):
        if len(state.next) == 0:
            state.best = state
            return state.best.value

        if level % 2 == 0:  # minimizer
            best = float("inf")
            for i in state.next:
                v = self.minimax(i, level + 1, alpha, beta)
                if state.best is None:
                    state.best = i
                elif v < state.best.value:
                    state.best = i
                best = min(best, v)
                beta = min(beta, best)
                if beta <= alpha:
                    break

            return state.best.value
        else:  # maximizer
            best = float("-inf")
            for i in state.next:
                v = self.minimax(i, level + 1, alpha, beta)
                if state.best is None:
                    state.best = i
                elif v > state.best.value:
                    state.best = i
                best = max(best, v)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return state.best.value

    def win_reset(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                self.grid[i][j].checked = False
                self.grid[i][j].upCheck = False
                self.grid[i][j].downCheck = False
                self.grid[i][j].backCheck = False
                self.grid[i][j].path = False

    def check_for_a_win(self):

        draw_test = 1
        win_result = 0

        self.win_reset()
        all_checked = 0

        while all_checked < self.height:

            for j in range(0, self.height):
                for i in range(0, self.width):
                    if self.grid[i][j].checked == False:
                        if self.grid[i][j].state == "H":
                            if i == 0:
                                self.grid[i][j].path = True
                            if i > 0:
                                if self.grid[i - 1][j].path == True:
                                    self.grid[i][j].path = True
                                    self.grid[i][j].backCheck = True
                                    if i == self.width - 1:
                                        win_result = 1
                                        return win_result
                            if j > 0 and j < self.height - 1:
                                if self.grid[i][j - 1].path == True:
                                    self.grid[i][j].path = True
                                if self.grid[i][j + 1].path == True:
                                    self.grid[i][j].path = True
                                    self.grid[i][j].downCheck = True
                            if j == 0:
                                if self.grid[i][j + 1].path == True:
                                    self.grid[i][j].path = True
                                    self.grid[i][j].downCheck = True
                        if (self.grid[i][j].upCheck == True) and (self.grid[i][j].downCheck == True) and (
                                self.grid[i][j].backCheck == True):
                            self.grid[i][j].checked = True

            all_checked += 1

        self.win_reset()
        all_checked = 0
        while all_checked < self.height:

            for j in range(0, self.height):
                for i in range(0, self.width):
                    if self.grid[i][j].checked == False:
                        if self.grid[i][j].state == "M":
                            if i == 0:
                                self.grid[i][j].path = True
                            if i > 0:
                                if self.grid[i - 1][j].path == True:
                                    self.grid[i][j].path = True
                                    self.grid[i][j].backCheck = True
                                    if i == self.width - 1:
                                        win_result = 2
                                        return win_result
                            if j > 0 and j < self.height - 1:
                                if self.grid[i][j - 1].path == True:
                                    self.grid[i][j].path = True
                                if self.grid[i][j + 1].path == True:
                                    self.grid[i][j].path = True
                                    self.grid[i][j].downCheck = True
                            if j == 0:
                                if self.grid[i][j + 1].path == True:
                                    self.grid[i][j].path = True
                                    self.grid[i][j].downCheck = True
                        if (self.grid[i][j].upCheck == True) and (self.grid[i][j].downCheck == True) and (
                                self.grid[i][j].backCheck == True):
                            self.grid[i][j].checked = True

            all_checked += 1

            # printer for checking wins
        '''
        for j in range(0, self.height):
            for i in range(0, self.width):
                print(self.grid[i][j].path, end=" ")
                print(i, end=" ")
                print(j, end=" ")
                if i == self.width - 1:
                    print()

                '''

        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.grid[i][j].state == " ":
                    draw_test = 0
                    break
            if draw_test == 0:
                break
        if draw_test == 1:
            win_result = 3

        # win_result:
        #  0- no winner,
        #  1- player one winner (H),
        #  2- player two winner (M)
        #  3- draw
        return win_result

