from grid import *
from constraint import *


def main():
    print("Welcome to Sudoku Solver!")
    print("Which difficulty level would you like the AI to solve today?")
    '''
    diff = input("Press 1-5 (1 = easiest, 5 = hardest) then enter to start the solver: ")
    if diff == 1:
        text_doc = "easiest.txt"
        # Solution: https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
    if diff == 2:
        text_doc = "easy.txt"
    if diff == 3:
        text_doc = "medium.txt"
    if diff == 4:
        text_doc = "hard.txt"
    if diff == 5:
        text_doc = "hardest.txt"
    '''
    text_doc = "easiest.txt"
    #IMPORTANT! PRINTER PRINTS FROM LEFT TO RIGHT. THIS MEANS THAT THE NUMBERS FOR DOCUMENTS
    #MUST BE FORMATTED ROW BY ROW WITH LINE BREAKS AS SHOWN IN THE EX. DOCUMENT EASIEST.TXT
    grid = Grid()
    with open(text_doc, "r") as data:
        grid.start(data)
        #grid.error_check()
        grid.printer()

    constraint = Constraint()
    constraint.constrain(grid)


if __name__ == '__main__':
    main()
