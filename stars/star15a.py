import enum
import collections
from heapq import heappop, heappush

Point = collections.namedtuple('Point', ['y', 'x'])


def astar_search(start, h_func, moves_func):
    """Find a shortest sequence of states from start to a goal state
    (a state s with h_func(s) == 0)."""
    # A priority queue, ordered by path length, f = g + h
    frontier = [(h_func(start), start)]
    # start state has no previous state; other states will
    previous = {start: None}
    # The cost of the best path to a state.
    path_cost = {start: 0}
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(previous, s)
        for s2 in moves_func(s):
            new_cost = path_cost[s] + 1
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))


def Path(previous, s):
    """Return a list of states that lead to state s,
    according to the previous dict."""
    return ([] if (s is None) else Path(previous, previous[s]) + [s])


class CreatureType(enum.Enum):
    elf = 'elf'
    goblin = 'goblin'


class Creature(object):
    def __init__(self, y, x, HP=200, damage_per_hit=3):
        self.HP = HP
        self.damage_per_hit = damage_per_hit
        self.location = Point(y, x)

    def __lt__(self, other):
        return self.location < other.location

    def in_range(self, other):
        return (
            self.location.x == other.location.x and
            abs(self.location.y - other.location.y) == 1 or
            self.location.y == other.location.y and
            abs(self.location.x - other.location.x) == 1
        )

    def hit(self, other):
        other.take_damage(self.damage_per_hit)

    def take_damage(self, damage):
        self.HP = self.HP - damage

    def attack(self, cavern):
        enemy_to_hit = next(iter(sorted(
            (c for c in cavern.creatures
                if c.side == self.enemy and self.in_range(c)),
            key=lambda c: (c.HP, c.location)
        )), None)
        if enemy_to_hit:
            self.hit(enemy_to_hit)
        return enemy_to_hit

    def take_turn(self, cavern):
        enemy_hit = self.attack(cavern)
        if enemy_hit:
            return enemy_hit
        self.move(cavern)
        enemy_hit = self.attack(cavern)
        if enemy_hit:
            return enemy_hit

    def move(self, cavern):
        def heuristic(point):
            # enemies = {c for c in cavern.creatures if c.side == self.enemy}
            # print(enemies)
            return min(
                (
                    abs(point.x - adj.x) + abs(point.y - adj.y)
                    # for c in enemies
                    for c in cavern.creatures if c.side == self.enemy
                    for adj in cavern.open_adjacent_points(c.location)
                ),
                default=0
            )
        possible_paths = [
            astar_search(adj, heuristic, cavern.open_adjacent_points)
            for adj in cavern.open_adjacent_points(self.location)
        ]

        self.location = next(iter(sorted(
            (p for p in possible_paths if isinstance(p, list)),
            key=lambda p: (len(p), p[0])
        )), [self.location])[0]


class Goblin(Creature):
    side = CreatureType.goblin
    enemy = CreatureType.elf

    def __repr__(self):
        return "Goblin({}, {}, HP={}, damage_per_hit={})".format(
            self.location.y,
            self.location.x,
            self.HP,
            self.damage_per_hit
        )


class Elf(Creature):
    side = CreatureType.elf
    enemy = CreatureType.goblin

    def __repr__(self):
        return "Elf({}, {}, HP={}, damage_per_hit={})".format(
            self.location.y,
            self.location.x,
            self.HP,
            self.damage_per_hit
        )


class Cavern(object):
    def __init__(self, creatures=None, points=None):
        self.creatures = creatures or set()
        self.points = points or set()

    def battle_over(self):
        return not all(
            {c for c in self.creatures if c.side == side}
            for side in CreatureType
        )

    def build(self, inp):
        for y, line in enumerate(inp):
            for x, char in enumerate(line):
                if char == '.':
                    self.points.add(Point(y, x))
                elif char == 'G':
                    self.points.add(Point(y, x))
                    self.creatures.add(Goblin(y, x))
                elif char == 'E':
                    self.points.add(Point(y, x))
                    self.creatures.add(Elf(y, x))

    def open_adjacent_points(self, point):
        open_points = self.points - {c.location for c in self.creatures}

        return {p for p in [
            Point(point.y - 1, point.x),
            Point(point.y, point.x - 1),
            Point(point.y, point.x + 1),
            Point(point.y + 1, point.x),
        ] if p in open_points}

    def execute_round(self):
        initiative = sorted(self.creatures)
        for creature in initiative:
            attacked = creature.take_turn(self)
            if attacked:
                if attacked.HP < 1:
                    self.creatures.remove(attacked)
                if self.battle_over():
                    return True

    def battle(self):
        rnd = 0
        battle_finished = None
        while True:
            rnd += 1
            battle_finished = self.execute_round()
            if battle_finished:
                break
            print(rnd)
        return rnd * sum(c.HP for c in self.creatures)

def do_the_thing(filename):
    cavern = Cavern()
    with open(filename) as inp:
        cavern.build(inp)

    # print(cavern.creatures)

    print(cavern.battle())
    print(cavern.creatures)

if __name__ == '__main__':
    do_the_thing('input/day15-test1.txt')
    do_the_thing('input/day15-test2.txt')
    do_the_thing('input/day15.txt')
