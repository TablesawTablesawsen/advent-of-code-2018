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

safe_places = set()
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distances = sum((taxi_distance(c, (x, y))) for c in coords)
        if distances < 10000:
            safe_places.add((x,y))

print(len(safe_places))
