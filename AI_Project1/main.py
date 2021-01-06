from Board import *
from Search import *


def main():
    puzzle_board = Board(False)
    searcher = Search()

    print("This program solves 8-puzzles using AI!")

    print("First we need a start state for an 8-puzzle.")
    print("In this simulation, 0 represents an empty space.")
    print("This is any combination of numbers from 0-8 without reusing entries and using spaces")
    start_list = list(map(int, input("Enter the start state: ").split()))
    print("Start State: ", start_list)

    print("Second we need a goal state for an 8-puzzle.")
    print("This is any combination of numbers from 0-8 without reusing entries and using spaces")
    goal_list = list(map(int, input("Enter the goal state: ").split()))
    print("Goal State: ", goal_list)

    #start_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    #goal_list = [1, 2, 3, 4, 5, 6, 7, 0, 8]

    puzzle_board.populate_board(start_list)
    puzzle_board.set_goal(goal_list)

    #bfs
    print("")
    print("BFS: ")
    if puzzle_board.test_goal() is True:
        print("board is solved")
    else:
        searcher.bfs_search(puzzle_board, goal_list)

    # greedy
    puzzle_board2 = Board(False)
    searcher2 = Search()
    puzzle_board2.populate_board(start_list)
    puzzle_board2.set_goal(goal_list)
    print("")
    print("Greedy: ")
    searcher2.best_first_search(puzzle_board2, goal_list)

    # amisplaced
    puzzle_board3 = Board(False)
    searcher3 = Search()
    puzzle_board3.populate_board(start_list)
    puzzle_board3.set_goal(goal_list)
    print("")
    print("AMisplaced: ")
    searcher3.mt_search(puzzle_board3, goal_list)
    #searcher.bfs_search(puzzle_board, goal_list)
 

    
    #WARNING: Manhattan search was developed separately in one file and was difficult to merge. 
    # Artifacts of it are still present in this code, but have been disable to prevent errors.
    # Manhattan can be launched from the additionally included file "Astar_test.py"

    # amanhattan


if __name__ == "__main__":
    main()

