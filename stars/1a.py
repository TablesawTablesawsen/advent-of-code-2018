with open('input/day1.txt') as input:
    freq = sum(int(num) for num in input)

print(freq)