import itertools
import datetime
import string

# about 35s
# def remove_reactions(polymer):
#     reduced_polymer = ''
#     while polymer:
#         char = polymer[0]
#         polymer = polymer[1:]
#         if polymer and char.lower() == polymer[0].lower() and char != polymer[0]:
#             polymer = polymer[1:]
#         else:
#             reduced_polymer = reduced_polymer + char
#     return reduced_polymer

# about 20s (felt longer the first time)
# def remove_reactions(polymer):
#     removed_indexes = set()
#     for i in range(len(polymer) - 1):
#         if i in removed_indexes:
#             continue
#         char = polymer[i]
#         nextchar = polymer[i+1]
#         if char.lower() == nextchar.lower() and char != nextchar:
#             removed_indexes.add(i)
#             removed_indexes.add(i+1)
#     return ''.join(polymer[i] for i in range(len(polymer)) if i not in removed_indexes)

reactions = [''.join(t) for t in itertools.chain(
    zip(string.ascii_lowercase, string.ascii_uppercase),
    zip(string.ascii_uppercase, string.ascii_lowercase)
    )]

def remove_reactions(polymer):
    for reaction in reactions:
        polymer = polymer.replace(reaction, '')
    return polymer

def reducing_polymer(polymer):
    previous_polymer = ''
    while len(polymer) != len(previous_polymer):
        yield polymer
        previous_polymer = polymer
        polymer = remove_reactions(previous_polymer)


def get_polymer():
    with open('input/day5.txt') as f:
        return next(f)

if __name__ == '__main__':
    start = datetime.datetime.now()
    polymer = get_polymer()
    for reduced_polymer in reducing_polymer(polymer):
        pass
    end = datetime.datetime.now()

    print(len(reduced_polymer))
    print(end - start)
