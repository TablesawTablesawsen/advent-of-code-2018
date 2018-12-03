freq = 0

with open('input.txt') as input:
    for num in input:
        freq = freq + int(num)

print(freq)