INITIAL_STATE = '.#####.##.#.##...#.#.###..#.#..#..#.....#..####.#.##.#######..#...##.#..#.#######...#.#.#..##..#.#.#'
TEST_STATE = '#..#.#..##......###...###'

TRANSITIONS = {
    '#..#.': '.', '##...': '#', '#....': '.', '#...#': '#', '...#.': '.', 
    '.#..#': '#', '#.#.#': '.', '.....': '.', '##.##': '#', '##.#.': '#', 
    '###..': '#', '#.##.': '.', '#.#..': '#', '##..#': '#', '..#.#': '#', 
    '..#..': '.', '.##..': '.', '...##': '#', '....#': '.', '#.###': '#', 
    '#..##': '#', '..###': '#', '####.': '#', '.#.#.': '#', '.####': '.', 
    '###.#': '#', '#####': '#', '.#.##': '.', '.##.#': '.', '.###.': '.', 
    '..##.': '.', '.#...': '#'
}

TEST_TRANSITIONS = {
    '...##':'#', '..#..':'#', '.#...':'#', '.#.#.':'#', '.#.##':'#', 
    '.##..':'#', '.####':'#', '#.#.#':'#', '#.###':'#', '##.#.':'#', 
    '##.##':'#', '###..':'#', '###.#':'#', '####.':'#'
}

import datetime

class Corridor(object):
    def __init__(self, initial_state, transitions):
        self.transitions = { 
            tuple(char == '#' for char in key): val == '#' 
            for key, val in transitions.items()
        }
        self.plants = set(i for i, c in enumerate(initial_state) if c == '#')
        self.start = -2
        self.end = len(initial_state) + 3

    def cycle(self):
        self.plants = set(i for i in range(self.start, self.end) if self.alive(i))
        self.reset_range()

    def alive(self, pot):
        input = tuple(i in self.plants for i in range(pot-2, pot+3))
        return self.transitions.get(input, False)

    def total(self):
        return sum(self.plants)

    def reset_range(self):
        i = self.start
        while i not in self.plants:
            i = i + 1
        self.start = i - 2

        i = self.end
        while i not in self.plants:
            i = i - 1
        self.end = i + 3

TARGET = 50000000000

corridor = Corridor(INITIAL_STATE, TRANSITIONS)
for i in range(100):
    corridor.cycle()
stable_sum = corridor.total()
print(corridor.total() + 62 * (TARGET - 100))