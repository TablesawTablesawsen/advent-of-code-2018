import itertools

# def remove_reactions(polymer):
#     return ''.join(polymer[i] for i in range(len(polymer)) if stable(polymer, i))

# def stable(polymer, i):
#     before = polymer[i-1].lower() if i > 0 else ''
#     char = polymer[i].lower()
#     after = polymer[i+1].lower() if i < len(polymer)-1 else ''
#     return before != char and after != char

def remove_reactions(polymer):
    removed_indexes = set()
    for i in range(len(polymer) - 1):
        if i in removed_indexes:
            continue

        char = polymer[i]
        nextchar = polymer[i+1]
        if char.lower() == nextchar.lower() and char != nextchar:
            removed_indexes.add(i)
            removed_indexes.add(i+1)
    return ''.join(polymer[i] for i in range(len(polymer)) if i not in removed_indexes)

def reducing_polymer(polymer):
    previous_polymer = ''
    while len(polymer) != len(previous_polymer):
        yield polymer
        previous_polymer = polymer
        polymer = remove_reactions(previous_polymer)

with open('input/day5.txt') as f:
    polymer = next(f)

for reduced_polymer in reducing_polymer(polymer):
    pass

print(len(reduced_polymer))

