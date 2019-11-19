import datetime

TEST1 = 5, '01245'
TEST3 = 9, '51589'
TEST2 = 18, '92510'
TEST4 = 2018, '59414'
INPUT = '147061'


class Kitchen(object):
    def __init__(self, recipes):
        self.recipes = recipes
        # self.elves = tuple(range(len(self.recipes)))
        self.elf1 = 0
        self.elf2 = 1

    def create_new_recipes(self):
        # self.recipes += str(sum(
            # int(self.recipes[elf]) for elf in self.elves))
        # self.elves = tuple(
        #     (elf + 1 + int(self.recipes[elf])) % len(self.recipes)
        #     for elf in self.elves
        # )
        self.recipes = ''.join([
            self.recipes,
            str(int(self.recipes[self.elf1]) + int(self.recipes[self.elf2]))
        ])
        self.elf1 = (
            self.elf1 + 1 + int(self.recipes[self.elf1])) % len(self.recipes)
        self.elf2 = (
            self.elf2 + 1 + int(self.recipes[self.elf2])) % len(self.recipes)
        # self.elves = tuple(
        #     (elf + 1 + int(self.recipes[elf])) % len(self.recipes)
        #     for elf in self.elves
        # )

    # def get_all_recipes(self):
    #     return ''.join(str(i) for i in self.recipes)

    # def get_new_recipes(self, start):
    #     return ''.join(str(i) for i in self.recipes[start:])

    # def get_sequences(self, length):
    #     sequences = {}
    #     if len(self.recipes) < length:
    #         return {}
    #     # sequences[''.join(
    #     #     str(self.recipes[i]) for i in range(0 - length, -0, 1)
    #     # )] = len(self.recipes) - length
    #     sequences[
    #         ''.join(str(c) for c in self.recipes[0 - length:])
    #     ] = len(self.recipes) - length

    #     if len(self.recipes) < length + 1:
    #         return {}
    #     # sequences[''.join(
    #     #     str(self.recipes[i]) for i in range(-1 - length, -1, 1)
    #     # )] = len(self.recipes) - length - 1
    #     sequences[
    #         ''.join(str(c) for c in self.recipes[1 - length: -1])
    #     ] = len(self.recipes) - length
    #     return sequences


def get_answer(kitchen, seq):
    # start = 0
    # length = len(seq)
    count = 0
    while seq not in kitchen.recipes[-7:]:
        # for i in range(100000):
        kitchen.create_new_recipes()
        count += 1
        if count % 100000 == 0:
            print(count)
        if count > 15561683:
            print('problem!')
        # recipes = kitchen.get_new_recipes(start)
        # recipes = kitchen.get_a_recipes(start)
        # start = len(recipes) - length
    return kitchen.recipes.find(seq)


# for answer, sequence in [TEST1, TEST2, TEST3, TEST4]:
#     assert get_answer(Kitchen('37'), sequence) == answer
#     print(answer)


start = datetime.datetime.now()
score = '37'
elf1 = 0
elf2 = 1
count = 0
while INPUT not in score[-7:]:
    score += str(int(score[elf1]) + int(score[elf2]))
    elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
    elf2 = (elf2 + int(score[elf2]) + 1) % len(score)
    count += 1

print('Part 2:', score.index(INPUT), count)
print(datetime.datetime.now() - start)

for answer, sequence in [TEST1, TEST2, TEST3, TEST4]:
    assert get_answer(Kitchen('37'), sequence) == answer
    print(answer)

start = datetime.datetime.now()
print(get_answer(Kitchen('37'), INPUT))
print(datetime.datetime.now() - start)
