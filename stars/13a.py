import itertools
import collections

Point = collections.namedtuple('Point', ['y', 'x'])


class Cart(object):
    def __init__(self, location, direction):
        self.location = location
        self.direction = direction
        self.turn_iterator = itertools.cycle(['l', 's', 'r'])

    def __lt__(self, other):
        return self.location < other.location

    def next_location(self):
        loc = self.location
        return {
            '<': Point(loc.y, loc.x - 1),
            '>': Point(loc.y, loc.x + 1),
            '^': Point(loc.y - 1, loc.x),
            'v': Point(loc.y + 1, loc.x)
        }[self.direction]

    def turn(self, tracks):
        track = tracks[self.location]
        if track == '+':
            relative_turn = next(self.turn_iterator)
            if relative_turn == 'l':
                self.direction = {
                    '^': '<',
                    '>': '^',
                    'v': '>',
                    '<': 'v',
                }[self.direction]
            elif relative_turn == 'r':
                self.direction = {
                    '^': '>',
                    '>': 'v',
                    'v': '<',
                    '<': '^',
                }[self.direction]
        elif track in ['/', '\\']:
            self.direction = {
                ('/', '^'): '>',
                ('/', '>'): '^',
                ('/', 'v'): '<',
                ('/', '<'): 'v',
                ('\\', '^'): '<',
                ('\\', '>'): 'v',
                ('\\', 'v'): '>',
                ('\\', '<'): '^',
            }[(track, self.direction)]
        return self.direction


class Mine(object):
    def __init__(self, inp):
        self.tracks = {}
        self.carts = set()
        for y, line in enumerate(inp):
            for x, char in enumerate(line):
                loc = Point(y, x)
                if char in ['<', '>']:
                    self.carts.add(Cart(loc, char))
                    char = '-'
                if char in ['^', 'v']:
                    self.carts.add(Cart(loc, char))
                    char = '|'
                if not char.isspace():
                    self.tracks[loc] = char

    def tick(self):
        for cart in sorted(self.carts):
            next_location = cart.next_location()
            if any(c.location == next_location for c in self.carts):
                return next_location
            cart.location = next_location
            cart.turn(self.tracks)


with open('input/day13.txt') as inp:
    mine = Mine(inp)

collision = None
while not collision:
    collision = mine.tick()

print(collision)
