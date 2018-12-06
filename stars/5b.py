import itertools
import datetime
import string

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
    polymer = get_polymer()
    results = {}
    for letter in string.ascii_lowercase:
        test_polymer = polymer.replace(letter, '').replace(letter.upper(), '')
        for reduced_polymer in reducing_polymer(test_polymer):
            pass
        print (letter, len(reduced_polymer))
        results[letter] = len(reduced_polymer)

    print(results)
