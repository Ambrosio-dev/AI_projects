from World import *
from Search import *
import random
import time
from math import floor

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print("This is a simulation for calculating the optimal distance for 2 hospitals between n houses.")
    print("In this simulation:")
    print("Empty spaces will be represented by 0" )
    print("Hospitals will be represented by H")
    print("Houses will be represented by h")
    print()

    trapped = True
    random_or_not = 999    
    while trapped:
        if (random_or_not != 999):
            print()
            print("Please only enter 1 or 2 as options...") 
        print("Would you like to set the dimensions of the four grids and the number of houses yourself, or would you like to randomly generate these values? ")
        random_or_not = input("1 for user values or 2 for random values: ")
        if (random_or_not == '1'): 
            trapped = False
        if (random_or_not == '2'): 
            trapped = False

    size = [0, 0, 0, 0]
    house = [0, 0, 0, 0]


    if (random_or_not == '1'): 
        print()
        print("You have selected user input for values. ")
        print("Please set the width and height for the first grid.")
        world1 = World()
        house[0] = input("How many houses will be used for the first grid: ")
        print("Please set the width and height for the second grid.")
        world2 = World()
        house[1] = input("How many houses will be used for the second grid: ")
        print("Please set the width and height for the third grid.")
        world3 = World()
        house[2] = input("How many houses will be used for the third grid: ")
        print("Please set the width and height for the fourth grid.")
        world4 = World()
        house[3] = input("How many houses will be used for the fourth grid: ")
        

        
    if (random_or_not == '2'):
        print()
        print("You have selected random input for values. ")
        i = 0
        while i < 4:
            size[i] = random.randrange(10, 15)
            house[i] = random.randrange(floor(size[i]*size[i]/4), floor(size[i]*size[i]/2))
            i += 1

        world1 = World(size[0],size[0])
        world2 = World(size[1],size[1])
        world3 = World(size[2],size[2])
        world4 = World(size[3],size[3])

    world1.populate(int(house[0]))
    world2.populate(int(house[1]))
    world3.populate(int(house[2]))
    world4.populate(int(house[3]))





    print("The grid (World 1) is " + str(world1.width) + " spaces wide and " + str(world1.height) + " spaces tall with " + str(house[0]) + " houses: ")
    world1.printer()
    print("Sum Distance:", end =' ')
    print(world1.sum_dis)
    print()

    print("The grid (World 2) is " + str(world2.width) + " spaces wide and " + str(world2.height) + " spaces tall with " + str(house[1]) + " houses: ")
    world2.printer()
    print("Sum Distance:", end =' ')
    print(world2.sum_dis)
    print()


    print("The grid (World 3) is " + str(world3.width) + " spaces wide and " + str(world3.height) + " spaces tall with " + str(house[2]) + " houses: ")
    world3.printer()
    print("Sum Distance:", end =' ')
    print(world3.sum_dis)
    print()


    print("The grid (World 4) is " + str(world4.width) + " spaces wide and " + str(world4.height) + " spaces tall with " + str(house[3]) + " houses: ")
    world4.printer()
    print("Sum Distance:", end =' ')
    print(world4.sum_dis)
    print()


    print("Starting hill climbing...")
    
    start = [0,0,0,0,0,0,0,0]
    end = [0,0,0,0,0,0,0,0]
    times = [0,0,0,0,0,0,0,0]

    for i in start:
        start[i] = time.time()

    for i in end:
        end[i] = time.time()

    search = Search()
    Sol1 = search.hcrr(world1)
    world1.rand_restart()
    Sol2 = search.hcrr(world1)
    world1.rand_restart()
    Sol3 = search.hcrr(world1)
    world1.rand_restart()
    Sol4 = search.hcrr(world1)
    world1.rand_restart()

    end[0] = time.time()
    start[1] = time.time()

    Sol5= search.hcrr(world2)
    world2.rand_restart()
    Sol6 = search.hcrr(world2)
    world2.rand_restart()
    Sol7 = search.hcrr(world2)
    world2.rand_restart()
    Sol8 = search.hcrr(world2)
    world2.rand_restart()

    end[1] = time.time()
    start[2] = time.time()

    Sol9 = search.hcrr(world3)
    world3.rand_restart()
    Sol10 = search.hcrr(world3)
    world3.rand_restart()
    Sol11 = search.hcrr(world3)
    world3.rand_restart()
    Sol12 = search.hcrr(world3)
    world3.rand_restart()

    end[2] = time.time()
    start[3] = time.time()

    Sol13 = search.hcrr(world4)
    world4.rand_restart()
    Sol14 = search.hcrr(world4)
    world4.rand_restart()
    Sol15 = search.hcrr(world4)
    world4.rand_restart()
    Sol16 = search.hcrr(world4)
    world4.rand_restart()

    end[3] = time.time()
    print("...Finished")
    print()
    print("Starting simulated annealing...")


    start[4] = time.time()

    Sol17 = search.sa(world1)
    world1.rand_restart()
    Sol18 = search.sa(world1)
    world1.rand_restart()
    Sol19 = search.sa(world1)
    world1.rand_restart()
    Sol20 = search.sa(world1)
    world1.rand_restart()

    end[4] = time.time()
    start[5] = time.time()

    Sol21 = search.sa(world2)
    world2.rand_restart()
    Sol22 = search.sa(world2)
    world2.rand_restart()
    Sol23 = search.sa(world2)
    world2.rand_restart()
    Sol24 = search.sa(world2)
    world2.rand_restart()

    end[5] = time.time()
    start[6] = time.time()

    Sol25 = search.sa(world3)
    world3.rand_restart()
    Sol26 = search.sa(world3)
    world3.rand_restart()
    Sol27 = search.sa(world3)
    world3.rand_restart()
    Sol28 = search.sa(world3)
    world3.rand_restart()

    end[6] = time.time()
    start[7] = time.time()

    Sol29 = search.sa(world4)
    world4.rand_restart()
    Sol30 = search.sa(world4)
    world4.rand_restart()
    Sol31 = search.sa(world4)
    world4.rand_restart()
    Sol32 = search.sa(world4)
    world4.rand_restart()

    end[7] = time.time()
    print("...Finished")

    print("Calculating results...")

    print("Test Results: ")

    print()
    print("Optimal grid after hill climbing for World 1 run 1: ")
    Sol1.printer()
    print("Sum Distance:", end =' ')
    print(Sol1.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 1 run 2: ")
    Sol2.printer()
    print("Sum Distance:", end =' ')
    print(Sol2.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 1 run 3: ")
    Sol3.printer()
    print("Sum Distance:", end =' ')
    print(Sol3.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 1 run 4: ")
    Sol4.printer()
    print("Sum Distance:", end =' ')
    print(Sol4.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 2 run 1: ")
    Sol5.printer()
    print("Sum Distance:", end =' ')
    print(Sol5.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 2 run 2: ")
    Sol6.printer()
    print("Sum Distance:", end =' ')
    print(Sol6.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 2 run 3: ")
    Sol7.printer()
    print("Sum Distance:", end =' ')
    print(Sol7.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 2 run 4: ")
    Sol8.printer()
    print("Sum Distance:", end =' ')
    print(Sol8.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 3 run 1: ")
    Sol9.printer()
    print("Sum Distance:", end =' ')
    print(Sol9.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 3 run 2: ")
    Sol10.printer()
    print("Sum Distance:", end =' ')
    print(Sol10.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 3 run 3: ")
    Sol11.printer()
    print("Sum Distance:", end =' ')
    print(Sol11.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 3 run 4: ")
    Sol12.printer()
    print("Sum Distance:", end =' ')
    print(Sol12.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 4 run 1: ")
    Sol13.printer()
    print("Sum Distance:", end =' ')
    print(Sol13.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 4 run 2: ")
    Sol14.printer()
    print("Sum Distance:", end =' ')
    print(Sol14.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 4 run 3: ")
    Sol15.printer()
    print("Sum Distance:", end =' ')
    print(Sol15.sum_dis)
    print()

    print("Optimal grid after hill climbing for World 4 run 4: ")
    Sol16.printer()
    print("Sum Distance:", end =' ')
    print(Sol16.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 1 run 1: ")
    Sol17.printer()
    print("Sum Distance:", end =' ')
    print(Sol17.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 1 run 2: ")
    Sol18.printer()
    print("Sum Distance:", end =' ')
    print(Sol18.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 1 run 3: ")
    Sol19.printer()
    print("Sum Distance:", end =' ')
    print(Sol19.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 1 run 4: ")
    Sol20.printer()
    print("Sum Distance:", end =' ')
    print(Sol20.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 2 run 1: ")
    Sol21.printer()
    print("Sum Distance:", end =' ')
    print(Sol21.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 2 run 2: ")
    Sol22.printer()
    print("Sum Distance:", end =' ')
    print(Sol22.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 2 run 3: ")
    Sol23.printer()
    print("Sum Distance:", end =' ')
    print(Sol23.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 2 run 4: ")
    Sol24.printer()
    print("Sum Distance:", end =' ')
    print(Sol24.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 3 run 1: ")
    Sol25.printer()
    print("Sum Distance:", end =' ')
    print(Sol25.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 3 run 2: ")
    Sol26.printer()
    print("Sum Distance:", end =' ')
    print(Sol26.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 3 run 3: ")
    Sol27.printer()
    print("Sum Distance:", end =' ')
    print(Sol27.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 3 run 4: ")
    Sol28.printer()
    print("Sum Distance:", end =' ')
    print(Sol28.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 4 run 1: ")
    Sol29.printer()
    print("Sum Distance:", end =' ')
    print(Sol29.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 4 run 2: ")
    Sol30.printer()
    print("Sum Distance:", end =' ')
    print(Sol30.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 4 run 3: ")
    Sol31.printer()
    print("Sum Distance:", end =' ')
    print(Sol31.sum_dis)
    print()

    print("Optimal grid after simulated annealing for World 4 run 4: ")
    Sol32.printer()
    print("Sum Distance:", end =' ')
    print(Sol32.sum_dis)

    print()

    mov = 0
    while mov < 8:
        times[mov] = end[mov] - start[mov]
        mov += 1

    print("Algorithm Speed Results: ")
    print()
    print("Hill climbing speeds: ")
    print(str(times[0:4]) + " seconds")
    print("Average: " + str(sum(times[0:4])/4) + " seconds")
    print()
    print("Simulated Annealing speeds: ")
    print(str(times[4:8]) + " seconds")
    print("Average: " + str(sum(times[4:8])/4) + " seconds")



if __name__ == '__main__':
    main()



