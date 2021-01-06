from World import *
import math
import random


class Search:

    def __init__(self):
        self.current = None
        self.next = []
        self.local_max = None
        self.init_temp = 1
        self.min_temp = 0.0001

    def hcrr(self, init):
        self.next = [0, 0, 0, 0, 0, 0, 0, 0]  # 8 spots for 8 new states
        self.current = init
        count = 0
        change = False
        # generate states for self.next:
        while count < 10:
            for i in range(8):
                new_world = self.current.next(i)
                self.next[i] = new_world

            for i in range(8):
                if self.next[i] != 0:
                    if self.current.sum_dis > self.next[i].sum_dis:
                        self.current = self.next[i]
                        self.local_max = self.current
                        change = True

            if change is False:
                self.local_max = self.current
                self.current = self.current.rand_restart()
                count = 0

            count = count + 1

        return self.local_max

    def sa(self, init):
        self.init_temp = 1
        self.next = [0, 0, 0, 0, 0, 0, 0, 0]  # 8 spots for 8 new states
        self.current = init
        self.local_max = self.current
        min = None

        while self.init_temp > self.min_temp:
            for j in range(10):
                for i in range(8):
                    new_world = self.current.next(i)
                    self.next[i] = new_world

                num = random.randrange(0, 7)
                if self.next[num] != 0:
                    min = self.next[num]
                else:
                    while self.next[num] == 0:
                        num = random.randrange(0, 8)
                        if self.next[num] != 0:
                            min = self.next[num]

                if self.current.sum_dis > min.sum_dis:
                    self.current = min

                    if self.current.sum_dis < self.local_max.sum_dis:
                        self.local_max = self.current
                else:
                    ap = math.exp((self.current.sum_dis - min.sum_dis)/self.init_temp)

                    if ap > random.random():
                        self.current = min

            self.init_temp *= 1 - 0.03

        return self.local_max

