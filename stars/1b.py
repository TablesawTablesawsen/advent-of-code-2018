import itertools

freq = 0
freq_set = set()

with open('input.txt') as input:
    for num in itertools.cycle(input):
        freq = freq + int(num)
        if freq in freq_set:
            break
        freq_set.add(freq)

print(freq)