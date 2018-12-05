import re

regex = r'#(?P<id>\d*) @ (?P<x>\d*),(?P<y>\d*): (?P<width>\d*)x(?P<height>\d*)'

fabric = {}
claim_ids = set()

with open('input/day3.txt') as claims:
    for claim in claims:
        matches = re.search(regex, claim).groupdict()
        claim_ids.add(matches['id'])
        for x in range(int(matches['width'])):
            for y in range(int(matches['height'])):
                coord = (int(matches['x']) + x, int(matches['y']) + y)
                fabric[coord] = fabric.get(coord, []) + [matches['id']]


overlap_ids = {id for ids in fabric.values() if len(ids) > 1 for id in ids }
print(claim_ids - overlap_ids)