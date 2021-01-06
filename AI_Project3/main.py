from grid import *



def main():
    print()
    print("This is a game called pathways.")
    print("You will compete against an AI player by placing marks on the board.")
    print("The AI player's marks will be represented by M's and yours will be represented by H's.")
    print("Your goal is to connect adjacent Hs and connect the left side of the board with the right.")
    print("Good luck!")
    print()
    grid = Grid(int(input("Enter width of grid.")), int(input("Enter height of grid.")))
    #print("Who moves first?")
    
    mode = input("Who moves first? Input 1 for Human and 2 for Machine: ")

    grid.get_who_moves_first(mode)  # Human 1 Machine 2
    tester = 0
    block = 1
    while block:
        if grid.first == "H":
            tester = grid.check_for_a_win()
            if tester != 0:
                break
            grid.printer()
            grid.get_human_player_move()
            tester = grid.check_for_a_win()
            if tester != 0:
                break
            grid.printer()
            grid.generate_computer_player_move()
        elif grid.first == "M":
            tester = grid.check_for_a_win()
            if tester != 0:
                break
            grid.printer()
            grid.generate_computer_player_move()
            tester = grid.check_for_a_win()
            if tester != 0:
                break
            grid.printer()
            grid.get_human_player_move()
            
    grid.printer()
    if tester == 1:
        print("Player One (Human/H) Wins!")
    if tester == 2:
        print("Player Two (Machine/M) Wins!")
    if tester == 3:
        print("It's a draw!")

        
'''
    while grid.win is False:
        if grid.first == "H":
            grid.get_human_player_move()
            if grid.win is True:
                break
            grid.generate_computer_player_move()
            if grid.win is True:
                break
        elif grid.first == "M":
            grid.generate_computer_player_move()
            if grid.win is True:
                break
            grid.get_human_player_move()
            if grid.win is True:
                break
                
    print("game over")
'''
if __name__ == '__main__':
    main()
