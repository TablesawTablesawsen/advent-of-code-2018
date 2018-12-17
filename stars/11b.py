import datetime
import itertools

SERIAL_NUMBER = 2866

def power_level(x, y):
    rack_id = x + 10
    pl = rack_id * y
    pl = pl + SERIAL_NUMBER
    pl = pl * rack_id
    digit = int('{:03d}'.format(pl)[-3])
    return digit - 5

grid = {(x, y): power_level(x, y) for x in range(1, 301) for y in range(1, 301)}

# for x in range(1,11): 
#     print(' '.join(str(grid[(x,y)]) for y in range(1,11)))
# def nine_total(x, y):
#     return sum(grid[(x+i, y+j)] for i in range(3) for j in range(3))
# square_size = 0

# def square_total(x, y, s):
#     return sum(grid[(x+i, y+j)] for i in range(s) for j in range(s))

# top = max(
#     ((x,y,s) for s in range(1, 301) for x in range(1,302-s) for y in range(1,302-s)),
#     key=lambda c: square_total(*c)
#     )

def squares(grid):
    for x in range(1, 301):
        start = datetime.datetime.now()
        for y in range(1, 301):
            square_total = 0
            max_square = 301 - max(x, y)
            for s in range(1,max_square+1):
                next_col = sum(grid[(x+s-1, y+row)] for row in range(s))
                next_row = sum(grid[(x+col, y+s-1)] for col in range(s-1))
                square_total = square_total + next_col + next_row
                yield (x,y,s), square_total
        elapsed = datetime.datetime.now() - start
        print(x, elapsed)


top_coord, val = max(squares(grid), key=lambda t: t[1])
print(top_coord, val)
# itr = squares(grid)
# for n in range(10):
#     coord, val = next(itr)
#     check = square_total(*coord)
#     print(coord, val, check)