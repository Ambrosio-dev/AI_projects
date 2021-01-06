#constraint file which will solve the grid function, this could be deleted and just be in grid I suppose?
from grid import *

class Constraint:
    def __init__(self):
        self.stop = False
        self.naked_double = []
        self.naked_triple = []
        self.guess_state = None

    def constrain(self, grid):
        iter = 0
        loop = 0
        while not self.stop:
            print("this is loop" + str(loop))
            count = 0
            for i in range(9):
                for j in range(9):
                    if grid.grid[i][j].value == "0":
                        v = self.tile_insert(grid.grid[i][j], grid)
                        if v != 0:
                            grid.grid[i][j].value = str(v)
                            grid.grid[i][j].domain = None
                            count += 1
                            iter = 0
                            self.set_tile(grid.grid[i][j], grid)
                            grid.printer()
            loop += 1
            print(str(count))
            if count == 0:
                if self.stop_check(grid):
                    cont_1 = self.naked_double_check(grid)
                    if cont_1:
                        continue
                    else:
                        cont_2 = self.naked_trible_check(grid)
                        if cont_2:
                            continue
                        else:
                            self.guess(grid)
                else:
                    self.stop = True

    def tile_insert(self, node, grid):
        insert = False
        check = 0
        i = node.get_y()
        j = node.get_x()
        if i < 3:  # top
            if j < 3:  # left
                for m in node.domain:
                    for k in range(3):
                        for l in range(3):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break
                    if insert:
                        return m
            elif 3 <= j < 6:
                for m in node.domain:
                    for k in range(3):
                        for l in range(3, 6):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break
                    if insert:
                        return m
            elif j >= 6:
                for m in node.domain:
                    for k in range(3):
                        for l in range(6, 9):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break
                    if insert:
                        return m
        elif 3 <= i < 6:
            if j < 3:  # left
                for m in node.domain:
                    for k in range(3, 6):
                        for l in range(3):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break
                    if insert:
                        return m
            elif 3 <= j < 6:
                for m in node.domain:
                    for k in range(3, 6):
                        for l in range(3, 6):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break
                    if insert:
                        return m
            elif j >= 6:
                for m in node.domain:
                    for k in range(3, 6):
                        for l in range(6, 9):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break
                    if insert:
                        return m
        elif i >= 6:
            if j < 3:  # left
                for m in node.domain:
                    for k in range(6, 9):
                        for l in range(3):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break
                    if insert:
                        return m
            elif 3 <= j < 6:
                for m in node.domain:
                    for k in range(6, 9):
                        for l in range(3, 6):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break

                    if insert:
                        return m
            elif j >= 6:
                for m in node.domain:
                    for k in range(6, 9):
                        for l in range(6, 9):
                            if grid.grid[k][l] is not node and grid.grid[k][l].value == "0":
                                check += 1
                                if not grid.grid[k][l].domain.count(m) == 1:
                                    insert = True
                                else:
                                    insert = False
                                    break
                        else:
                            continue
                        break
                    if insert:
                        return m
        if check == 0:
            return m
        else:
            return 0

    def stop_check(self, grid):
        for i in range(9):
            for j in range(9):
                if grid.grid[i][j].value == "0":
                    return True
        return False

    def is_triple(self, node):
        for triple in self.naked_triple:
            for item in triple:
                if node is item:
                    return True

        return False

    def is_double(self, node):
        for double in self.naked_double:
            for item in double:
                if node is item:
                    return True

        return False

    def set_tile(self, node, grid):
        i = node.get_y()
        j = node.get_x()

        for k in range(9):  # check col
            if grid.grid[k][j].domain is not None:
                if grid.grid[k][j].domain.count(node.value) == 1:
                    grid.grid[k][j].domain.remove(node.value)

        for l in range(9):  # check row
            if grid.grid[i][l].domain is not None:
                if grid.grid[i][l].domain.count(node.value) == 1:
                    grid.grid[i][l].domain.remove(node.value)

    def naked_double_check(self, grid):
        list = []
        count = 0
        for j in range(9):
            for i in range(9):
                if grid.grid[i][j].value == "0":
                    if len(grid.grid[i][j].domain) == 2:
                        if i < 3:  # top
                            if j < 3:  # left
                                for k in range(3):
                                    for l in range(3):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(3):
                                                        for n in range(3):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][
                                                                n] is not grid.grid[k][l] and grid.grid[m][
                                                                n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                            elif 3 <= j < 6:
                                for k in range(3):
                                    for l in range(3, 6):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(3):
                                                        for n in range(3, 6):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][
                                                                n] is not grid.grid[k][l] and grid.grid[m][
                                                                n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                            elif 6 <= j < 9:
                                for k in range(3):
                                    for l in range(6, 9):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(3):
                                                        for n in range(6, 9):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][
                                                                n] is not grid.grid[k][l] and grid.grid[m][
                                                                n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                        elif 3 <= i < 6:
                            if j < 3:  # left
                                for k in range(3, 6):
                                    for l in range(3):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(3, 6):
                                                        for n in range(3):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][
                                                                n] is not grid.grid[k][l] and grid.grid[m][
                                                                n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                            elif 3 <= j < 6:
                                for k in range(3, 6):
                                    for l in range(3, 6):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(3, 6):
                                                        for n in range(3, 6):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][
                                                                n] is not grid.grid[k][l] and grid.grid[m][
                                                                n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                            elif 6 <= j < 9:
                                for k in range(3, 6):
                                    for l in range(6, 9):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(3, 6):
                                                        for n in range(6, 9):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][
                                                                n] is not grid.grid[k][l] and grid.grid[m][
                                                                n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                        elif 6 <= i < 9:
                            if j < 3:  # left
                                for k in range(6, 9):
                                    for l in range(3):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(6, 9):
                                                        for n in range(3):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][
                                                                n] is not grid.grid[k][l] and grid.grid[m][
                                                                n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                            elif 3 <= j < 6:
                                for k in range(6, 9):
                                    for l in range(3, 6):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(6, 9):
                                                        for n in range(3, 6):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][
                                                                n] is not grid.grid[k][l] and grid.grid[m][
                                                                n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                            elif 6 <= j < 9:
                                for k in range(6, 9):
                                    for l in range(6, 9):
                                        if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                            if len(grid.grid[k][l].domain) == 2:
                                                if grid.grid[k][l].domain == grid.grid[i][j].domain:
                                                    list.append(grid.grid[i][j])
                                                    list.append(grid.grid[k][l])
                                                    for m in range(3):
                                                        for n in range(6, 9):
                                                            if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][n] is not grid.grid[k][l] and grid.grid[m][n].value == "0":
                                                                for item in list[0].domain:
                                                                    if grid.grid[m][n].domain.count(item) == 1:
                                                                        grid.grid[m][n].domain.remove(item)
                                                                        count += 1
                                                    list.clear()
                        for k in range(9):  # check col
                            if grid.grid[k][j] is not grid.grid[i][j] and grid.grid[k][j].value == "0":
                                if len(grid.grid[k][j].domain) == 2:
                                    if grid.grid[k][j].domain == grid.grid[i][j].domain:
                                        list.append(grid.grid[i][j])
                                        list.append(grid.grid[k][j])
                                        for l in range(9):
                                            if grid.grid[l][j] is not grid.grid[i][j] and grid.grid[l][j] is not grid.grid[k][j] and grid.grid[l][j].value == "0":
                                                for item in list[0].domain:
                                                    if grid.grid[l][j].domain.count(item) == 1:
                                                        grid.grid[l][j].domain.remove(item)
                                                        count += 1
                                        list.clear()

                                                for k in range(9):  # check row
                            if grid.grid[i][k] is not grid.grid[i][j] and grid.grid[i][k].value == "0":
                                if len(grid.grid[i][k].domain) == 2:
                                    if grid.grid[i][k].domain == grid.grid[i][j].domain:
                                        list.append(grid.grid[i][j])
                                        list.append(grid.grid[i][k])
                                        for l in range(9):
                                            if grid.grid[i][l] is not grid.grid[i][j] and grid.grid[i][l] is not \
                                                    grid.grid[i][k] and grid.grid[i][l].value == "0":
                                                for item in list[0].domain:
                                                    if grid.grid[i][l].domain.count(item) == 1:
                                                        grid.grid[i][l].domain.remove(item)
                                                        count += 1
                                        list.clear()
        if count == 0:
            return False
        else:
            return True

    def naked_trible_check(self, grid):
        list = []
        count = 0
        for j in range(9):
            for i in range(9):
                if grid.grid[i][j].value == "0":
                    if 1 < len(grid.grid[i][j].domain) >= 3:
                        if len(grid.grid[i][j].domain) == 2:
                            if i < 3:  # top
                                if j < 3:  # left
                                    for k in range(3):
                                        for l in range(3):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(3):
                                                            for n in range(3):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and grid.grid[m][n] is not grid.grid[k][l] and grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3):
                                                                                    for p in range(3):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 3 <= j < 6:
                                    for k in range(3):
                                        for l in range(3, 6):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(3):
                                                            for n in range(3, 6):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                        grid.grid[m][n] is not grid.grid[k][l] and \
                                                                        grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3):
                                                                                    for p in range(3, 6):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 6 <= j < 9:
                                    for k in range(3):
                                        for l in range(6, 9):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(3):
                                                            for n in range(6, 9):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                        grid.grid[m][n] is not grid.grid[k][l] and \
                                                                        grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3):
                                                                                    for p in range(6, 9):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                            elif 3 <= i < 6:
                                if j < 3:  # left
                                    for k in range(3, 6):
                                        for l in range(3):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(3, 6):
                                                            for n in range(3):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                        grid.grid[m][n] is not grid.grid[k][l] and \
                                                                        grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3, 6):
                                                                                    for p in range(3):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 3 <= j < 6:
                                    for k in range(3, 6):
                                        for l in range(3, 6):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(3, 6):
                                                            for n in range(3, 6):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                        grid.grid[m][n] is not grid.grid[k][l] and \
                                                                        grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3, 6):
                                                                                    for p in range(3, 6):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 6 <= j < 9:
                                    for k in range(3, 6):
                                        for l in range(6, 9):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(3, 6):
                                                            for n in range(6, 9):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                        grid.grid[m][n] is not grid.grid[k][l] and \
                                                                        grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3, 6):
                                                                                    for p in range(6, 9):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                            elif 6 <= i < 9:
                                if j < 3:  # left
                                    for k in range(6, 9):
                                        for l in range(3):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(6, 9):
                                                            for n in range(3):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                        grid.grid[m][n] is not grid.grid[k][l] and \
                                                                        grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(6, 9):
                                                                                    for p in range(3):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 3 <= j < 6:
                                    for k in range(6, 9):
                                        for l in range(3, 6):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(6, 9):
                                                            for n in range(3, 6):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                        grid.grid[m][n] is not grid.grid[k][l] and \
                                                                        grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(6, 9):
                                                                                    for p in range(3, 6):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 6 <= j < 9:
                                    for k in range(6, 9):
                                        for l in range(6, 9):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if len(grid.grid[k][l].domain) == 2:
                                                    share = False
                                                    for item in grid.grid[i][j].domain:
                                                        for element in grid.grid[k][l].domain:
                                                            if element == item:
                                                                if not share:
                                                                    share = True
                                                                    shared = element
                                                                else:
                                                                    share = False
                                                    if share:
                                                        target_1 = None
                                                        target_2 = None
                                                        for item in grid.grid[i][j].domain:
                                                            if item != shared:
                                                                target_1 = item
                                                        for element in grid.grid[k][l].domain:
                                                            if element != shared:
                                                                target_2 = element
                                                        for m in range(6, 9):
                                                            for n in range(6, 9):
                                                                if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                        grid.grid[m][n] is not grid.grid[k][l] and \
                                                                        grid.grid[m][n].value == "0":
                                                                    if len(grid.grid[m][n].domain) == 2:
                                                                        if grid.grid[m][n].domain.count(target_1) == 1:
                                                                            if grid.grid[m][n].domain.count(target_2) == 1:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(6, 9):
                                                                                    for p in range(6, 9):
                                                                                        if grid.grid[o][p] is not \
                                                                                                grid.grid[i][j] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[k][l] and \
                                                                                                grid.grid[o][p] is not \
                                                                                                grid.grid[m][n] and \
                                                                                                grid.grid[o][
                                                                                                    p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][p].domain.count(domain) == 1:
                                                                                                        grid.grid[o][p].domain.remove(domain)
                                                                                                        count += 1
                                                                                list.clear()
                            for k in range(9):  # check col
                                if grid.grid[k][j] is not grid.grid[i][j] and grid.grid[k][j].value == "0":
                                    if len(grid.grid[k][j].domain) == 2:
                                        share = False
                                        for item in grid.grid[i][j].domain:
                                            for element in grid.grid[k][j].domain:
                                                if element == item:
                                                    if not share:
                                                        share = True
                                                        shared = element
                                                    else:
                                                        share = False
                                        if share:
                                            target_1 = None
                                            target_2 = None
                                            for item in grid.grid[i][j].domain:
                                                if item != shared:
                                                    target_1 = item
                                            for element in grid.grid[k][j].domain:
                                                if element != shared:
                                                    target_2 = element
                                            for l in range(9):
                                                if grid.grid[l][j] is not grid.grid[i][j] and grid.grid[l][j] is not \
                                                        grid.grid[k][j] and grid.grid[l][j].value == "0":
                                                    if len(grid.grid[l][j].domain) == 2:
                                                        if grid.grid[l][j].domain.count(target_1) == 1:
                                                            if grid.grid[l][j].domain.count(target_2) == 1:
                                                                list.append(grid.grid[i][j])
                                                                list.append(grid.grid[k][j])
                                                                list.append(grid.grid[l][j])
                                                                for m in range(9):
                                                                    if grid.grid[m][j] is not grid.grid[i][j] and \
                                                                            grid.grid[m][j] is not grid.grid[k][j] and \
                                                                            grid.grid[m][j] is not grid.grid[l][j] and grid.grid[i][l].value == "0":
                                                                        for triple in list:
                                                                            for domain in triple.domain:
                                                                                if grid.grid[m][j].domain.count(
                                                                                        domain) == 1:
                                                                                    grid.grid[m][j].domain.remove(
                                                                                        domain)
                                                                                    count += 1
                                                                list.clear()
                            for k in range(9):  # check row
                                if grid.grid[i][k] is not grid.grid[i][j] and grid.grid[i][k].value == "0":
                                    if len(grid.grid[i][k].domain) == 2:
                                        share = False
                                        for item in grid.grid[i][j].domain:
                                            for element in grid.grid[i][k].domain:
                                                if element == item:
                                                    if not share:
                                                        share = True
                                                        shared = element
                                                    else:
                                                        share = False
                                        if share:
                                            target_1 = None
                                            target_2 = None
                                            for item in grid.grid[i][j].domain:
                                                if item != shared:
                                                    target_1 = item
                                            for element in grid.grid[i][k].domain:
                                                if element != shared:
                                                    target_2 = element
                                            for l in range(9):
                                                if grid.grid[i][l] is not grid.grid[i][j] and grid.grid[i][l] is not \
                                                        grid.grid[i][k] and grid.grid[i][l].value == "0":
                                                    if len(grid.grid[i][l].domain) == 2:
                                                        if grid.grid[i][l].domain.count(target_1) == 1:
                                                            if grid.grid[i][l].domain.count(target_2) == 1:
                                                                list.append(grid.grid[i][j])
                                                                list.append(grid.grid[i][k])
                                                                list.append(grid.grid[i][l])
                                                                for m in range(9):
                                                                    if grid.grid[i][m] is not grid.grid[i][j] and \
                                                                            grid.grid[i][m] is not \
                                                                            grid.grid[i][k] and grid.grid[i][m] is not grid.grid[i][l] and grid.grid[i][m].value == "0":
                                                                        for triple in list:
                                                                            for domain in triple.domain:
                                                                                if grid.grid[i][m].domain.count(
                                                                                        domain) == 1:
                                                                                    grid.grid[i][m].domain.remove(
                                                                                        domain)
                                                                                    count += 1
                                                                list.clear()
                        elif len(grid.grid[i][j].domain) == 3:
                            if i < 3:  # top
                                if j < 3:  # left
                                    for k in range(3):
                                        for l in range(3):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(3):
                                                                for n in range(3):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3):
                                                                                        for p in range(3):
                                                                                            if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3):
                                                                                        for p in range(3):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(3):
                                                                for n in range(3):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3):
                                                                                    for p in range(3):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 3 <= j < 6:
                                    for k in range(3):
                                        for l in range(3, 6):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(3):
                                                                for n in range(3, 6):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3):
                                                                                        for p in range(3, 6):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3):
                                                                                        for p in range(3, 6):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(3):
                                                                for n in range(3, 6):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3):
                                                                                    for p in range(3, 6):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 6 <= j < 9:
                                    for k in range(3):
                                        for l in range(6, 9):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(3):
                                                                for n in range(6, 9):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3):
                                                                                        for p in range(6, 9):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3):
                                                                                        for p in range(6, 9):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(3):
                                                                for n in range(6, 9):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3):
                                                                                    for p in range(6, 9):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                            elif 3 <= i < 6:
                                if j < 3:
                                    for k in range(3, 6):
                                        for l in range(3):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(3, 6):
                                                                for n in range(3):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3, 6):
                                                                                        for p in range(3):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3, 6):
                                                                                        for p in range(3):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(3, 6):
                                                                for n in range(3):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3, 6):
                                                                                    for p in range(3):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 3 <= j < 6:
                                    for k in range(3, 6):
                                        for l in range(3, 6):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(3, 6):
                                                                for n in range(3, 6):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3, 6):
                                                                                        for p in range(3, 6):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3, 6):
                                                                                        for p in range(3, 6):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(3, 6):
                                                                for n in range(3, 6):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3, 6):
                                                                                    for p in range(3, 6):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 6 <= j < 9:
                                    for k in range(3, 6):
                                        for l in range(6, 9):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(3, 6):
                                                                for n in range(6, 9):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3, 6):
                                                                                        for p in range(6, 9):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(3, 6):
                                                                                        for p in range(6, 9):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(3, 6):
                                                                for n in range(6, 9):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(3, 6):
                                                                                    for p in range(6, 9):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                            elif 6 <= i < 9:
                                if j < 3:
                                    for k in range(6, 9):
                                        for l in range(3):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(6, 9):
                                                                for n in range(3):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(6, 9):
                                                                                        for p in range(3):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(6, 9):
                                                                                        for p in range(3):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(6, 9):
                                                                for n in range(3):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(6, 9):
                                                                                    for p in range(3):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 3 <= j < 6:
                                    for k in range(6, 9):
                                        for l in range(3, 6):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(6, 9):
                                                                for n in range(3, 6):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(6, 9):
                                                                                        for p in range(3, 6):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(6, 9):
                                                                                        for p in range(3, 6):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(6, 9):
                                                                for n in range(3, 6):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(6, 9):
                                                                                    for p in range(3, 6):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                                elif 6 <= j < 9:
                                    for k in range(6, 9):
                                        for l in range(6, 9):
                                            if grid.grid[k][l] is not grid.grid[i][j] and grid.grid[k][l].value == "0":
                                                if 1 < len(grid.grid[k][l].domain) >= 3:
                                                    if len(grid.grid[k][l].domain) == 3:
                                                        if grid.grid[i][j].domain == grid.grid[k][l].domain:
                                                            for m in range(6, 9):
                                                                for n in range(6, 9):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if 1 < len(grid.grid[m][n].domain) >= 3:
                                                                            if len(grid.grid[m][n].domain) == 3:
                                                                                if grid.grid[m][n].domain == grid.grid[k][l].domain:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(6, 9):
                                                                                        for p in range(6, 9):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                                domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                                            else:
                                                                                num = 0
                                                                                for item in grid.grid[m][n].domain:
                                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                                        num += 1
                                                                                if num == 2:
                                                                                    list.append(grid.grid[i][j])
                                                                                    list.append(grid.grid[k][l])
                                                                                    list.append(grid.grid[m][n])
                                                                                    for o in range(6, 9):
                                                                                        for p in range(6, 9):
                                                                                            if grid.grid[o][p] is not \
                                                                                                    grid.grid[i][j] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[k][l] and \
                                                                                                    grid.grid[o][
                                                                                                        p] is not \
                                                                                                    grid.grid[m][n] and \
                                                                                                    grid.grid[o][
                                                                                                        p].value == "0":
                                                                                                for triple in list:
                                                                                                    for domain in triple.domain:
                                                                                                        if grid.grid[o][
                                                                                                            p].domain.count(
                                                                                                            domain) == 1:
                                                                                                            grid.grid[
                                                                                                                o][
                                                                                                                p].domain.remove(
                                                                                                                domain)
                                                                                                            count += 1
                                                                                    list.clear()
                                                    else:
                                                        share_1 = False
                                                        share_2 = False
                                                        for item in grid.grid[i][j].domain:
                                                            for element in grid.grid[k][l].domain:
                                                                if element == item:
                                                                    if not share_1:
                                                                        share_1 = True
                                                                        shared_1 = element
                                                                    elif share_1 and not share_2:
                                                                        share_2 = True
                                                                        shared_2 = element
                                                                    else:
                                                                        share_1 = False
                                                                        share_2 = False
                                                        if share_1 and share_2:
                                                            target_1 = None
                                                            for item in grid.grid[i][j].domain:
                                                                if item != shared_1 or item != shared_2:
                                                                    target_1 = item
                                                            check_again = False
                                                            check_more = False
                                                            for m in range(6, 9):
                                                                for n in range(6, 9):
                                                                    if grid.grid[m][n] is not grid.grid[i][j] and \
                                                                            grid.grid[m][n] is not grid.grid[k][l] and \
                                                                            grid.grid[m][n].value == "0":
                                                                        if len(grid.grid[m][n].domain) == 2:
                                                                            for element in grid.grid[m][n].domain:
                                                                                if element == target_1:
                                                                                    check_again = True
                                                                                elif element == shared_1 or element == shared_2:
                                                                                    check_more = True
                                                                                else:
                                                                                    check_again = False
                                                                                    check_more = False
                                                                            if check_again and check_more:
                                                                                list.append(grid.grid[i][j])
                                                                                list.append(grid.grid[k][l])
                                                                                list.append(grid.grid[m][n])
                                                                                for o in range(6, 9):
                                                                                    for p in range(6, 9):
                                                                                        if grid.grid[o][p] is not grid.grid[i][j] and grid.grid[o][p] is not grid.grid[k][l] and grid.grid[o][p] is not grid.grid[m][n] and grid.grid[o][p].value == "0":
                                                                                            for triple in list:
                                                                                                for domain in triple.domain:
                                                                                                    if grid.grid[o][
                                                                                                        p].domain.count(
                                                                                                        domain) == 1:
                                                                                                        grid.grid[
                                                                                                            o][
                                                                                                            p].domain.remove(
                                                                                                            domain)
                                                                                                        count += 1
                                                                                list.clear()
                            for k in range(9):  # check col
                                if grid.grid[k][j] is not grid.grid[i][j] and grid.grid[k][j].value == "0":
                                    if 1 < len(grid.grid[k][j].domain) >= 3:
                                        if len(grid.grid[k][j].domain) == 3:
                                            if grid.grid[i][j].domain == grid.grid[k][j].domain:
                                                for l in range(9):
                                                    if grid.grid[l][j] is not grid.grid[i][j] and grid.grid[l][j] is not grid.grid[k][j] and grid.grid[l][j].value == "0":
                                                        if 1 < len(grid.grid[l][j].domain) >= 3:
                                                            if len(grid.grid[l][j].domain) == 3:
                                                                if grid.grid[l][j].domain == grid.grid[k][j].domain:
                                                                    list.append(grid.grid[i][j])
                                                                    list.append(grid.grid[k][j])
                                                                    list.append(grid.grid[l][j])
                                                                    for m in range(9):
                                                                        if grid.grid[m][j] is not grid.grid[i][j] and grid.grid[m][j] is not grid.grid[k][j] and grid.grid[m][j] is not grid.grid[l][j] and grid.grid[m][j].value == "0":
                                                                            for triple in list:
                                                                                for domain in triple.domain:
                                                                                    if grid.grid[m][j].domain.count(domain) == 1:
                                                                                        grid.grid[m][j].domain.remove(domain)
                                                                                        count += 1
                                                                    list.clear()
                                                            else:
                                                                num = 0
                                                                for item in grid.grid[l][j].domain:
                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                        num += 1
                                                                if num == 2:
                                                                    list.append(grid.grid[i][j])
                                                                    list.append(grid.grid[k][j])
                                                                    list.append(grid.grid[l][j])
                                                                    for m in range(9):
                                                                        if grid.grid[m][j] is not grid.grid[i][j] and grid.grid[m][j] is not grid.grid[k][j] and grid.grid[m][j] is not grid.grid[l][j] and grid.grid[m][j].value == "0":
                                                                            for triple in list:
                                                                                for domain in triple.domain:
                                                                                    if grid.grid[m][j].domain.count(domain) == 1:
                                                                                        grid.grid[m][j].domain.remove(domain)
                                                                                        count += 1
                                                                    list.clear()
                                        else:
                                            share_1 = False
                                            share_2 = False
                                            for item in grid.grid[i][j].domain:
                                                for element in grid.grid[k][j].domain:
                                                    if element == item:
                                                        if not share_1:
                                                            share_1 = True
                                                            shared_1 = element
                                                        elif share_1 and not share_2:
                                                            share_2 = True
                                                            shared_2 = element
                                                        else:
                                                            share_1 = False
                                                            share_2 = False
                                                if share_1 and share_2:
                                                    target_1 = None
                                                    for item in grid.grid[i][j].domain:
                                                        if item != shared_1 or item != shared_2:
                                                            target_1 = item
                                                    check_again = False
                                                    check_more = False
                                                    for l in range(9):
                                                        if grid.grid[l][j] is not grid.grid[i][j] and grid.grid[l][j] is not grid.grid[k][j] and grid.grid[l][j].value == "0":
                                                            if len(grid.grid[l][j].domain) == 2:
                                                                for element in grid.grid[l][j].domain:
                                                                    if element == target_1:
                                                                        check_again = True
                                                                    elif element == shared_1 or element == shared_2:
                                                                        check_more = True
                                                                    else:
                                                                        check_again = False
                                                                        check_more = False
                                                                if check_again and check_more:
                                                                    list.append(grid.grid[i][j])
                                                                    list.append(grid.grid[k][j])
                                                                    list.append(grid.grid[l][j])
                                                                    for m in range(9):
                                                                        if grid.grid[m][j] is not grid.grid[i][j] and grid.grid[m][j] is not grid.grid[k][j] and grid.grid[m][j] is not grid.grid[l][j] and grid.grid[m][j].value == "0":
                                                                            for triple in list:
                                                                                for domain in triple.domain:
                                                                                    if grid.grid[m][j].domain.count(domain) == 1:
                                                                                        grid.grid[m][j].domain.remove(domain)
                                                                                        count += 1
                                                                    list.clear()
                            for k in range(9):  # check row
                                if grid.grid[i][k] is not grid.grid[i][j] and grid.grid[i][k].value == "0":
                                    if 1 < len(grid.grid[i][k].domain) >= 3:
                                        if len(grid.grid[i][k].domain) == 3:
                                            if grid.grid[i][j].domain == grid.grid[i][k].domain:
                                                for l in range(9):
                                                    if grid.grid[i][l] is not grid.grid[i][j] and grid.grid[i][l] is not grid.grid[i][k] and grid.grid[i][l].value == "0":
                                                        if 1 < len(grid.grid[i][l].domain) >= 3:
                                                            if len(grid.grid[i][l].domain) == 3:
                                                                if grid.grid[i][l].domain == grid.grid[i][k].domain:
                                                                    list.append(grid.grid[i][j])
                                                                    list.append(grid.grid[i][k])
                                                                    list.append(grid.grid[i][l])
                                                                    for m in range(9):
                                                                        if grid.grid[i][m] is not grid.grid[i][j] and grid.grid[i][m] is not grid.grid[i][k] and grid.grid[i][m] is not grid.grid[i][l] and grid.grid[i][m].value == "0":
                                                                            for triple in list:
                                                                                for domain in triple.domain:
                                                                                    if grid.grid[i][m].domain.count(domain) == 1:
                                                                                        grid.grid[i][m].domain.remove(domain)
                                                                                        count += 1
                                                                    list.clear()
                                                            else:
                                                                num = 0
                                                                for item in grid.grid[i][l].domain:
                                                                    if grid.grid[i][j].domain.count(int) == 1:
                                                                        num += 1
                                                                if num == 2:
                                                                    list.append(grid.grid[i][j])
                                                                    list.append(grid.grid[i][k])
                                                                    list.append(grid.grid[i][l])
                                                                    for m in range(9):
                                                                        if grid.grid[i][m] is not grid.grid[i][j] and \
                                                                                grid.grid[i][m] is not grid.grid[i][
                                                                            k] and grid.grid[i][m] is not grid.grid[i][
                                                                            l] and grid.grid[i][m].value == "0":
                                                                            for triple in list:
                                                                                for domain in triple.domain:
                                                                                    if grid.grid[i][m].domain.count(domain) == 1:
                                                                                        grid.grid[i][m].domain.remove(domain)
                                                                                        count += 1
                                                                    list.clear()
                                        else:
                                            share_1 = False
                                            share_2 = False
                                            for item in grid.grid[i][j].domain:
                                                for element in grid.grid[i][k].domain:
                                                    if element == item:
                                                        if not share_1:
                                                            share_1 = True
                                                            shared_1 = element
                                                        elif share_1 and not share_2:
                                                            share_2 = True
                                                            shared_2 = element
                                                        else:
                                                            share_1 = False
                                                            share_2 = False
                                                if share_1 and share_2:
                                                    target_1 = None
                                                    for item in grid.grid[i][j].domain:
                                                        if item != shared_1 or item != shared_2:
                                                            target_1 = item
                                                    check_again = False
                                                    check_more = False
                                                    for l in range(9):
                                                        if grid.grid[i][l] is not grid.grid[i][j] and grid.grid[i][
                                                            l] is not grid.grid[i][k] and grid.grid[i][l].value == "0":
                                                            if len(grid.grid[i][l].domain) == 2:
                                                                for element in grid.grid[i][l].domain:
                                                                    if element == target_1:
                                                                        check_again = True
                                                                    elif element == shared_1 or element == shared_2:
                                                                        check_more = True
                                                                    else:
                                                                        check_again = False
                                                                        check_more = False
                                                                if check_again and check_more:
                                                                    list.append(grid.grid[i][j])
                                                                    list.append(grid.grid[i][k])
                                                                    list.append(grid.grid[i][l])
                                                                    for m in range(9):
                                                                        if grid.grid[i][m] is not grid.grid[i][j] and \
                                                                                grid.grid[i][m] is not grid.grid[i][
                                                                            k] and grid.grid[i][m] is not grid.grid[i][
                                                                            l] and grid.grid[i][m].value == "0":
                                                                            for triple in list:
                                                                                for domain in triple.domain:
                                                                                    if grid.grid[i][m].domain.count(domain) == 1:
                                                                                        grid.grid[i][m].domain.remove(domain)
                                                                                        count += 1
                                                                    list.clear()
        if count == 0:
            return False
        else:
            return True

        def guess(self, grid):
        self.guess_state = grid.deepcopy()
        hold = None
        hold_item = None
        hold_count = 100
        for i in range(9):
            for j in range(9):
                if grid.grid[i][j].value == "0":
                    for item in grid.grid[i][j].domain():
                        count = 0
                        for k in range(9): # col
                            if grid.grid[k][j].domain.count(item) == 1:
                                count += 1
                        for l in range(9):
                            if grid.grid[i][l].domain.count(item) == 1:
                                count += 1
                        if i < 3:  # top
                            if j < 3:  # left
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                            elif 3 < j <= 6:
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                            elif 6 < j <= 9:
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                        elif 3 < i <= 6:
                            if j < 3:  # left
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                            elif 3 < j <= 6:
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                            elif 6 < j <= 9:
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                        elif 6 < i <= 9:
                            if j < 3:  # left
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                            elif 3 < j <= 6:
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                            elif 6 < j <= 9:
                                for m in range(3):
                                    for n in range(3):
                                        if grid.grid[m][n].domain.count(item) == 1:
                                            count += 1
                        if count < hold_count:
                            hold_count = count
                            hold = grid.grid[i][j]
                            hold_item = item
        hold.value = hold_item
        self.set_tile(hold, grid)
