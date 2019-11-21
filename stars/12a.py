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
    '...##': '#', '..#..': '#', '.#...': '#', '.#.#.': '#', '.#.##': '#',
    '.##..': '#', '.####': '#', '#.#.#': '#', '#.###': '#', '##.#.': '#',
    '##.##': '#', '###..': '#', '###.#': '#', '####.': '#'
}


class Corridor(object):
    def __init__(self, initial_state, transitions):
        self.transitions = {
            tuple(char == '#' for char in key): val == '#'
            for key, val in transitions.items()
        }
        self.plants = sorted(i for i, c in enumerate(initial_state) if c == '#')

    def cycle(self):
        start = self.plants[0] - 2
        end = self.plants[-1] + 3
        self.plants = [i for i in range(start, end) if self.alive(i)]

    def alive(self, pot):
        input = tuple(i in self.plants for i in range(pot - 2, pot + 3))
        return self.transitions.get(input, False)

    def total(self):
        return sum(self.plants)


corridor = Corridor(INITIAL_STATE, TRANSITIONS)

for i in range(20):
    corridor.cycle()
print(corridor.total())
