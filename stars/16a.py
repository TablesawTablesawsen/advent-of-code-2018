import collections.abc
import itertools


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def parse_nums(s):
    return [int(num) for num in s.split()]


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

    __delitem__ = None

    def __eq__(self, other):
        return tuple(self._registers) == tuple(other)

    def __init__(self, *registers):
        self._registers = list(registers)

    def __call__(self, *args, name=None):
        if name not in self.opcodes:
            raise ValueError('Keyword name not in opcodes')
        return getattr(self, name)(*args[1:])

    def addr(self, a, b, c):
        self[c] = self[a] + self[b]
        return self

    def addi(self, a, b, c):
        self[c] = self[a] + b
        return self

    def mulr(self, a, b, c):
        self[c] = self[a] * self[b]
        return self

    def muli(self, a, b, c):
        self[c] = self[a] * b
        return self

    def banr(self, a, b, c):
        self[c] = self[a] & self[b]
        return self

    def bani(self, a, b, c):
        self[c] = self[a] & b
        return self

    def borr(self, a, b, c):
        self[c] = self[a] | self[b]
        return self

    def bori(self, a, b, c):
        self[c] = self[a] | b
        return self

    def setr(self, a, _, c):
        self[c] = self[a]
        return self

    def seti(self, a, _, c):
        self[c] = a
        return self

    def gtir(self, a, b, c):
        if a > self[b]:
            self[c] = 1
        else:
            self[c] = 0
        return self

    def gtri(self, a, b, c):
        if self[a] > b:
            self[c] = 1
        else:
            self[c] = 0
        return self

    def gtrr(self, a, b, c):
        if self[a] > self[b]:
            self[c] = 1
        else:
            self[c] = 0
        return self

    def eqir(self, a, b, c):
        if a == self[b]:
            self[c] = 1
        else:
            self[c] = 0
        return self

    def eqri(self, a, b, c):
        if self[a] == b:
            self[c] = 1
        else:
            self[c] = 0
        return self

    def eqrr(self, a, b, c):
        if self[a] == self[b]:
            self[c] = 1
        else:
            self[c] = 0
        return self


with open("input/16a.txt") as inp:
    matches_iter = (sum(
        (Device(*parse_nums(test[0]))(*parse_nums(test[1]), name=opcode) ==
            Device(*parse_nums(test[2])) for opcode in Device.opcodes)
    ) for test in grouper(inp, 4))
    print(sum(1 for matches in matches_iter if matches >= 3))
