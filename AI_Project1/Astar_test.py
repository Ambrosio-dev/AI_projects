import copy

class Node:

    def __init__(self, value=None):
        self.value = value
        self.adj_list = []
        adj_count = 0
        self.up = None
        self.down = None
        self.right = None
        self.left = None
        self.posx = 0
        self.posy = 0
        
    def get_value(self):
        return self.value

    def get_list(self):
        return self.adj_list
    
    def get_posx(self):
        return self.posx
    
    def get_posy(self):
        return self.posy
    
    def app_list(self, num):
        self.adj_list.append(num)

    def set_value(self, value):
        self.value = value
        
    def set_posx(self, posx):
        self.posx = posx
        
    def set_posy(self,posy):
        self.posy = posy
    
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
    
class Board:

    def __init__(self):
        rows, cols = (3, 3)
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def __getitem__(self,index1):
        return self.board[index1]

    def __setitem__(self,index1,node):
        self.board[index1] = node

    def populate_board(self, args):
        x = args.split(" ")
        insert_count = 0
        

        for i in range(0, 3):
            for j in range(0, 3):
                node = Node(x[insert_count])
                self.board[i][j] = node
                self.board[i][j].set_posx(j)
                self.board[i][j].set_posy(i)
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
                    self.board[i][j].set_down(self.board[i+1][j])
                    self.board[i][j].set_right(self.board[i][j+1])
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
                    self.board[i][j].set_down(self.board[i+1][j])
                    self.board[i][j].set_left(self.board[i][j-1])
                elif i == 1 and j == 2:
                    self.board[i][j].set_up(self.board[i-1][j])
                    self.board[i][j].set_down(self.board[i+1][j])
                    self.board[i][j].set_left(self.board[i][j-1])
                elif i == 2 and j == 2:
                    self.board[i][j].set_up(self.board[i-1][j])
                    self.board[i][j].set_left(self.board[i][j-1])

    def get_value(self):
        Node.get_value()

    def print_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.board[i][j].get_value())
                    
    def search_board(self, num):
        for i in range(0, 3):
            for j in range(0, 3):
                value = self.board[i][j].get_value()
                if int(value) == num:
                    temp = self.board[i][j]
        return temp
    
    def list_board(self, state):
        board_list = []
        for i in range(0, 3):
            for j in range(0, 3):
                board_list.append(state[i][j].get_value())
        return board_list

def aStar(start_state, end_state):
        
        cur_list = start_state.list_board(start_state)
        end_list = end_state.list_board(end_state)
    
        if cur_list == end_list:
            print("the given start state is equal to the given end state!!")
            return 0
        # setting the start state to open and having no closed states yet
        closed_states = []
        open_states = [start_state]
        # NOT SURE IF I NEED A PATH TAKEN LIST!!!
        path_taken = []
        #setting fNum, hNum, and gNum to 0 to start
        fNum = 0
        hNum = 0
        gNum = 0
        # setting the current state to the start state and moving it 
        # to the closed list
        current_state = copy.deepcopy(start_state)
        hNum = Manhatten(current_state, end_state)
                
        closed_states.append(cur_list)
        open_states.remove(start_state)
        
        # While loop to iterate through states
        while current_state != end_state:
        
            # finding the "blank" or zero node on the board
            node_zero = current_state.search_board(0)
            # creating new states based on what directions are open
            # and adding them to the open states list with their fNum values
            if node_zero.get_up() != None:
                #new_state = Board()
                #new_state.populate_board(str(cur_list))
                
                # copying the current state into a new state
                new_state = copy.deepcopy(current_state)
                # creating a temp node for the node above the 0 node
                temp_node = node_zero.get_up()
                # editing the new state by swapping the temp node and zero node
                new_state[temp_node.posy][temp_node.posx] = node_zero
                new_state[node_zero.posy][node_zero.posx] = temp_node
                # generating an updated board for new state 
                new_state = gen_board(new_state)
                # calculating the manhatten number
                hNum = Manhatten(new_state, end_state)
                # calculating the f number
                fNum = gNum + hNum
                # a way to see if the new state is in the closed and open lists
                cur_list = new_state.list_board(new_state)
                if cur_list == end_list:
                    print("match!!")
                    return 0
                # setting match found to false
                match_found = False
                temp_list = []
                # checking to see if current list is in closed states
                if cur_list not in closed_states:
                    # checking to see if match found is in open states
                    for first,*args in open_states:
                        # if a match is found, match found is set to true
                        temp_list = first.list_board(first)
                        if temp_list == cur_list:
                            match_found = True
                            break
                # adding the new state to the open list
                if match_found == False:
                    open_states.append((new_state, fNum))
            if node_zero.get_down() != None:
                #new_state = Board()
                #new_state.populate_board(str(cur_list))
                
                # copying the current state into a new state
                new_state = copy.deepcopy(current_state)
                # creating a temp node for the node above the 0 node
                temp_node = node_zero.get_down()
                # editing the new state by swapping the temp node and zero node
                new_state[temp_node.posy][temp_node.posx] = node_zero
                new_state[node_zero.posy][node_zero.posx] = temp_node
                # generating an updated board for new state 
                new_state = gen_board(new_state)
                # calculating the manhatten number
                hNum = Manhatten(new_state, end_state)
                # calculating the f number
                fNum = gNum + hNum
                # a way to see if the new state is in the closed and open lists
                cur_list = new_state.list_board(new_state)
                if cur_list == end_list:
                    print("match!!")
                    return 0
                # setting match found to false
                match_found = False
                temp_list = []
                # checking to see if current list is in closed states
                if cur_list not in closed_states:
                    # checking to see if match found is in open states
                    for first,*args in open_states:
                        # if a match is found, match found is set to true
                        temp_list = first.list_board(first)
                        if temp_list == cur_list:
                            match_found = True
                            break
                # adding the new state to the open list
                if match_found == False:
                    open_states.append((new_state, fNum))
            if node_zero.get_right() != None:
                #new_state = Board()
                #new_state.populate_board(str(cur_list))
                
                # copying the current state into a new state
                new_state = copy.deepcopy(current_state)
                # creating a temp node for the node above the 0 node
                temp_node = node_zero.get_right()
                # editing the new state by swapping the temp node and zero node
                new_state[temp_node.posy][temp_node.posx] = node_zero
                new_state[node_zero.posy][node_zero.posx] = temp_node
                # generating an updated board for new state 
                new_state = gen_board(new_state)
                # calculating the manhatten number
                hNum = Manhatten(new_state, end_state)
                # calculating the f number
                fNum = gNum + hNum
                # a way to see if the new state is in the closed and open lists
                cur_list = new_state.list_board(new_state)
                if cur_list == end_list:
                    print("match!!")
                    return 0
                # setting match found to false
                match_found = False
                temp_list = []
                # checking to see if current list is in closed states
                if cur_list not in closed_states:
                    # checking to see if match found is in open states
                    for first,*args in open_states:
                        # if a match is found, match found is set to true
                        temp_list = first.list_board(first)
                        if temp_list == cur_list:
                            match_found = True
                            break
                # adding the new state to the open list
                if match_found == False:
                    open_states.append((new_state, fNum))
            if node_zero.get_left() != None:
                #new_state = Board()
                #new_state.populate_board(str(cur_list))
                
                # copying the current state into a new state
                new_state = copy.deepcopy(current_state)
                # creating a temp node for the node above the 0 node
                temp_node = node_zero.get_left()
                # editing the new state by swapping the temp node and zero node
                new_state[temp_node.posy][temp_node.posx] = node_zero
                new_state[node_zero.posy][node_zero.posx] = temp_node
                # generating an updated board for new state 
                new_state = gen_board(new_state)
                # calculating the manhatten number
                hNum = Manhatten(new_state, end_state)
                # calculating the f number
                fNum = gNum + hNum
                # a way to see if the new state is in the closed and open lists
                cur_list = new_state.list_board(new_state)
                if cur_list == end_list:
                    print("match!!")
                    return 0
                # setting match found to false
                match_found = False
                temp_list = []
                # checking to see if current list is in closed states
                if cur_list not in closed_states:
                    # checking to see if match found is in open states
                    for first,*args in open_states:
                        # if a match is found, match found is set to true
                        temp_list = first.list_board(first)
                        if temp_list == cur_list:
                            match_found = True
                            break
                # adding the new state to the open list
                if match_found == False:
                    open_states.append((new_state, fNum))
        
            #SORT OPEN STATES BASED ON FNUM(THE SECOND NUMBER IN THE TUPLE)
            gNum = gNum + 1
            sort_list(open_states)        
            # NOW CURRENT STATE CHANGES TO THE FIRST STATE IN THE OPEN STATES LIST
            temp_tup = open_states[0]
            current_state = copy.deepcopy(temp_tup[0])
            # REMOVE THAT STATE AND ADD IT TO THE CLOSED STATES LIST
            closed_states.append(cur_list)
            open_states.pop(0)
            # CHECK TO SEE IF CURRENT STATE MATCHES END STATE
            if cur_list == end_list:
                print("the current state is the end state!!!")
                return 0
            # IF NOT REPEATE PROCESS UNTIL IT DOES
        
def Manhatten(current_state, end_state):
    hNum = 0
    for i in range(0, 9):
        temp_current_node = current_state.search_board(i)
        temp_end_node = end_state.search_board(i)
        current_posx = temp_current_node.get_posx()
        current_posy = temp_current_node.get_posy()
        end_posx = temp_end_node.get_posx()
        end_posy = temp_end_node.get_posy()
        xDiff = current_posx - end_posx
        yDiff = current_posy - end_posy
        if xDiff < 0:
            xDiff = xDiff * -1
        if yDiff < 0:
            yDiff = yDiff * -1
        hNum = hNum + xDiff + yDiff
    return hNum
    
def gen_board(new_state):
    new_order = []
    for i in range(0, 3):
        for j in range(0, 3):
            value = new_state[i][j].get_value()
            new_order.append(value)
    new_args = " ".join(new_order)
    temp = Board()
    temp.populate_board(new_args)
    return temp
    
def sort_list(tup):
    tup.sort(key = lambda x: x[1])  
    return tup  
        
def main():               
    
    start = "0 1 2 3 4 5 6 7 8"
    end = "1 2 3 4 5 6 0 7 8"
    startState = Board()
    startState.populate_board(start)
    
    endState = Board()
    endState.populate_board(end)

    aStar(startState,endState)
main()
    