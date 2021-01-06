#grid file for storing nodes that make the 9 x 9 sudoku board
from node import *


class Grid:
    def __init__(self):
        self.grid = [[0 for x in range(9)] for y in range(9)]
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = 0

    def start(self, file):
        for i in range(0, 9):  # height
            for j in range(0, 9):  # width
                c = file.read(1)
                while c == " " or c == "\n":
                    c = file.read(1)
                self.grid[i][j] = Node(j, i, c)
        self.set_domain()

        # self.appendFunction()
    #def error_check(self):
        #for j in range(0, 9):
            #for i in range(0, 9):
                #if self.grid[i][j].value == "_" and self.grid[i][j].domain:
                   # print("DOMAIN ERROR")

    def appendFunction(self):
        for i in range(0, 9):  # height
            for j in range(0, 9):  # width
                print(self.grid[i][j].value)

    def printer(self):
        print()
        i = 0
        j = 0
        k = 0
        print("  \\", end=' ')
        for k in range(12):
            print("-", end='  ')
            k += 1
        if k == 12:
            print("/", end='  ')
            print()
        for i in range(9):
            for j in range(9):
                # print("i:"+str(i), end='  ')
                if j == 0:
                    print("  | ", end=' ')
                if j == 3 or j == 6:
                    print(" | ", end=' ')
                print(self.grid[i][j].value, end='  ')
                if j == 8:
                    print("| ", end=' ')
                    print()
                # if j == 2 or j == 5:
                #    print(" | ", end=' ')
            if i == 2 or i == 5:
                print("  | ", end=' ')
                for k in range(12):
                    if k == 3 or k == 7:
                        print(" | ", end=' ')
                    else:
                        print("-", end='  ')
                    k += 1
                    if k == 11:
                        print("| ", end=' ')
                        break
                print()
        print("  /", end=' ')
        for k in range(12):
            print("-", end='  ')
            k += 1
        if k == 12:
            print("\\", end='  ')
            print()
        print()

    def test_solution(self, solution):
        #returns 1 of met solution, returns 0 for has not met solution
        for i in range(0, 9):  # height
            for j in range(0, 9):  # width
                if self.grid[i][j].value != solution.grid[i][j].value:
                    return 0
        return 1

    def set_domain(self):
        for i in range(0, 9):  # height
            for j in range(0, 9):  # width
                if self.grid[i][j].value == "0":
                    #  CHECK BOX COL AND ROW FOR ALL POSSIBLE VALUES
                    if i < 3:  # top
                        if j < 3:  # left
                            for k in range(3):
                                for l in range(3):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)
                        elif 3 <= j < 6:  # center
                            for k in range(3):
                                for l in range(3, 6):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)
                        elif j >= 6:  # right
                            for k in range(3):
                                for l in range(6, 9):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)
                    elif 3 <= i < 6:
                        if j < 3:  # left
                            for k in range(3, 6):
                                for l in range(3):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)
                        elif 3 <= j < 6:  # center
                            for k in range(3, 6):
                                for l in range(3, 6):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)
                        elif j >= 6:  # right
                            for k in range(3, 6):
                                for l in range(6, 9):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)
                    elif i >= 6:
                        if j < 3:  # left
                            for k in range(6, 9):
                                for l in range(3):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)
                        elif 3 <= j < 6:  # center
                            for k in range(6, 9):
                                for l in range(3, 6):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)
                        elif j >= 6:  # right
                            for k in range(6, 9):
                                for l in range(6, 9):
                                    if self.grid[k][l].value != "0":
                                        self.grid[i][j].domain.remove(self.grid[k][l].value)

                    for m in range(9):  # check col
                        if self.grid[m][j].value != "0":
                            if self.grid[i][j].domain.count(self.grid[m][j].value) == 1:
                                self.grid[i][j].domain.remove(self.grid[m][j].value)

                    for n in range(9):  # check row
                        if self.grid[i][n].value != "0":
                            if self.grid[i][j].domain.count(self.grid[i][n].value) == 1:
                                self.grid[i][j].domain.remove(self.grid[i][n].value)
