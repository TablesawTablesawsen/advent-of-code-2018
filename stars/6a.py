def taxi_distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

with open('input/day6.txt') as input:
    coords = {tuple(map(lambda x: int(x), s.split(', '))) for s in input}

x_coords = sorted(coords, key=lambda t: t[0])
y_coords = sorted(coords, key=lambda t: t[1])

min_x = x_coords[0][0]
max_x = x_coords[-1][0]
min_y = y_coords[0][1]
max_y = y_coords[-1][1]
x_range = range(min_x, max_x + 1)
y_range = range(min_y, max_y + 1)
infinite_coords = set()

space_map = {}
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distances = sorted(((c, taxi_distance(c, (x, y))) for c in coords), 
            key=lambda c: c[1])
        if distances[0][1] != distances[1][1]:
            space_map[(x,y)] = distances[0][0] 


for x in [min_x, max_x]:
    for y in y_range:
        coord = space_map.get((x,y), None)
        if coord:
            infinite_coords.add(coord) 

for x in x_range:
    for y in [min_y, max_y]:
        coord = space_map.get((x,y), None)
        if coord:
            infinite_coords.add(coord) 
finite_coords = coords - infinite_coords

max_domain = max(
    sum(1 for center in space_map.values() if center == coord) 
    for coord in finite_coords
)
print(max_domain)



