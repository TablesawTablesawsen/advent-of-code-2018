import collections

TEST1 = 5, '0124515891'
TEST2 = 18, '9251071085'
TEST3 = 9, '5158916779'
TEST4 = 2018, '5941429882'
INPUT = 147061


class Kitchen(object):
    def __init__(self, recipes):
        self.recipes = collections.deque(recipes)
        self.elves = tuple(range(len(self.recipes)))

    def create_new_recipes(self):
        self.recipes.extend(
            int(d) for d in str(sum(self.recipes[elf] for elf in self.elves))
        )
        self.elves = tuple(
            (elf + 1 + self.recipes[elf]) % len(self.recipes)
            for elf in self.elves
        )

    def get_recipes(self, start_after, count):
        return ''.join(
            str(self.recipes[i])
            for i in range(start_after, start_after + count)
        )


def get_answer(kitchen, start_after, count):
    while len(kitchen.recipes) < start_after + count:
        kitchen.create_new_recipes()
    return kitchen.get_recipes(start_after, count)


k = Kitchen([3, 7])
for start_after, answer in [TEST1, TEST2, TEST3, TEST4]:
    assert get_answer(k, start_after, 10) == answer

print(get_answer(k, INPUT, 10))
