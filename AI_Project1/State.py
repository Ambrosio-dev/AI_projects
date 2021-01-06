
class State:
    def __init__(self, state, misplaced):
        self.visited = False
        self.misplaced = misplaced
        self.previous = None #previous state
        self.state = state # current state of board
        self.next_state = [] # list of next states
        self.moves = 0# list of next states
        self.cost = 0

    def is_visited(self):
        return self.visited

    def set_misplaced(self, misplaced):
        self.misplaced = misplaced

    def get_misplaced(self):
        return self.misplaced

    def set_previous(self, node):
        self.previous = node

    def get_previous(self):
        return self.previous
    
    def set_moves(self, previous_move):
        self.moves = previous_move + 1

    def get_best_state(self):
        best = None

        for state in self.next_state:
            if best is None:
                best = state
            elif best.misplaced > state.misplaced:
                best = state
        return best
    def print_path(self):
        if self.previous is None:
            print(str(self.state))
        else:
            self.previous.print_path()
            print(str(self.state))

    
