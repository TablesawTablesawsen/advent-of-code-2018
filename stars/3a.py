import re

regex = r'#(?P<id>\d*) @ (?P<x>\d*),(?P<y>\d*): (?P<width>\d*)x(?P<height>\d*)'

fabric = {}

with open('input/day3.txt') as claims:
    for claim in claims:
        matches = re.search(regex, claim).groupdict()
        for x in range(int(matches['width'])):
            for y in range(int(matches['height'])):
                coord = (int(matches['x']) + x, int(matches['y']) + y)
                fabric[coord] = fabric.get(coord, []) + [int(matches['id'])]
overlap = sum(1 for coord, ids in fabric.items() if len(ids) > 1)
print(overlap)