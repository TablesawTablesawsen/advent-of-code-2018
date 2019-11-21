import collections.abc


class Device(collections.abc.Sequence):
    opcodes = [
        'addi', 'addr',
        'bani', 'banr',
        'bori', 'borr',
        'eqir', 'eqri', 'eqrr',
        'gtir', 'gtri', 'gtrr',
        'muli', 'mulr',
        'seti', 'setr'
    ]

    def __getitem__(self, key):
        return self._registers[key]

    def __len__(self):
        return len(self._registers)

    def __setitem__(self, key, value):
        self._registers[key] = value

    def __init__(self, *registers):
        self._registers = tuple(registers)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def addr(self, a, b, c):
        self[c] = self[a] + self[b]

    def addi(self, a, b, c):
        self[c] = self[a] + b

    def mulr(self, a, b, c):
        self[c] = self[a] * self[b]

    def muli(self, a, b, c):
        self[c] = self[a] * b

    def banr(self, a, b, c):
        self[c] = self[a] & self[b]

    def bani(self, a, b, c):
        self[c] = self[a] & b

    def borr(self, a, b, c):
        self[c] = self[a] | self[b]

    def bori(self, a, b, c):
        self[c] = self[a] | b

    def setr(self, a, _, c):
        self[c] = self[a]

    def seti(self, a, _, c):
        self[c] = a

    def gtir(self, a, b, c):
        if a > self[b]:
            self[c] = 1
        else:
            self[c] = 0

    def gtri(self, a, b, c):
        if self[a] > b:
            self[c] = 1
        else:
            self[c] = 0

    def gtrr(self, a, b, c):
        if self[a] > self[b]:
            self[c] = 1
        else:
            self[c] = 0

    def eqir(self, a, b, c):
        if a == self[b]:
            self[c] = 1
        else:
            self[c] = 0

    def eqri(self, a, b, c):
        if self[a] == b:
            self[c] = 1
        else:
            self[c] = 0

    def eqrr(self, a, b, c):
        if self[a] == self[b]:
            self[c] = 1
        else:
            self[c] = 0


def test_input(inp):
    while True:

# with open("input/16a.txt") as inp:
