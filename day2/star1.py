import functools

def has_multiple(box, num):
    for char in box:
        if box.count(char) == num:
            return True
    return False

multiples = [2, 3]
mult_map = {n: 0 for n in multiples} 

with open('input.txt') as input:
    for box in input:
        for n in multiples: 
            if has_multiple(box, n):
                mult_map[n] = mult_map[n] + 1

checksum = functools.reduce(lambda x, y: x*y, mult_map.values())
print(checksum)