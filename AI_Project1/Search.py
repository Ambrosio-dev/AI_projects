from Board import *
from State import *


class Search:

    def __init__(self):
        self.open_list = []
        self.closed_list =[]
        self.goal = None

    def bfs_search(self, start, goal):
        expanded_states = 0
        total_states = 0
        self.goal = goal
        root = start.feed()
        self.open_list.append(root)
        total_states = total_states + 1
        expanded_states = expanded_states + 1

        if self.open_list[0].state == goal:
            print(str(self.open_list.pop(0).state))
            expanded_states = expanded_states + 1
            print(str(total_states))
            print(str(expanded_states))

        while self.open_list:
            if expanded_states >= 10000:
                print("Too many nodes have been expanded to be solved")
                break
            if not self.open_list:
                print("No solution")

            if self.open_list[0].state == goal:
                print("Solution Found") 
                state.print_path()
                print(str(self.open_list.pop(0).state))
                expanded_states = expanded_states + 1
                print("total states: " + str(total_states))
                print("expanded states: " + str(expanded_states))
                break

            #self.open_list.append(n)
            for state in self.open_list[0].next_state:
                if state not in self.closed_list:
                    self.open_list.append(state)
                    total_states = total_states + 1

            self.closed_list.append(self.open_list.pop(0))
            start.update(self.open_list[0])
            #start.print_board()
            temp = start.feed()
            expanded_states = expanded_states + 1
            temp.set_previous(self.open_list[0].previous)
            self.open_list[0] = temp


    def best_first_search(self, start, goal):
        expanded_states = 0
        total_states = 0
        self.goal = goal
        root = start.feed()
        self.open_list.append(root)
        total_states = total_states + 1
        expanded_states = expanded_states + 1

        if self.open_list[0].state == goal:
            print(str(self.open_list.pop(0).state))
            expanded_states = expanded_states + 1
            print(str(total_states))
            print(str(expanded_states))

        while self.open_list:
            if expanded_states >= 10000:
                print("things are getting out of hand")
                break
            if not self.open_list:
                print("No solution")

            n = self.open_list[0].get_best_state()

            if n.misplaced == 0:
                print("Solution Found") 
                expanded_states = expanded_states + 1
                n.print_path()
                print("total states: " + str(total_states))
                print("expanded states: " + str(expanded_states))
                break

            #self.open_list.append(n)
            for state in self.open_list[0].next_state:
                if state not in self.open_list and state not in self.closed_list:
                    self.open_list.append(state)
                    total_states = total_states + 1

            self.closed_list.append(self.open_list.pop(0))
            self.open_list.sort(key=lambda state: state.misplaced, reverse=False)
            start.update(self.open_list[0])
            #start.print_board()
            temp = start.feed()
            expanded_states = expanded_states + 1
            temp.set_previous(self.open_list[0].previous)
            self.open_list[0] = temp

    def mt_search(self, start, goal):
        expanded_states = 0
        total_states = 0
        self.goal = goal
        root = start.feed()
        root.cost = root.moves + root.misplaced
        self.open_list.append(root)
        expanded_states = expanded_states + 1

        while self.open_list:
            current = self.open_list.pop(0)
            start.update(current)
            temp = start.feed()
            current.next_state = temp.next_state
            for state in current.next_state:
                state.set_moves(current.moves)
                state.cost = state.moves + state.misplaced
                state.set_previous(current)

            self.closed_list.append(current)

            if current.state == goal:
                print("Solution Found")
                current.print_path() 
                print("total states: " + str(total_states))
                print("expanded states: " + str(expanded_states))
                break
            for item in current.next_state:
                if item.cost < current.cost:
                    self.open_list.append(item)

            self.open_list.sort(key=lambda state: state.cost, reverse=False)
