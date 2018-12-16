SERIAL_NUMBER = 2866

def power_level(x, y):
    rack_id = x + 10
    pl = rack_id * y
    pl = pl + SERIAL_NUMBER
    pl = pl * rack_id
    digit = int('{:03d}'.format(pl)[-3])
    return digit - 5

grid = {(x, y): power_level(x, y) for x in range(1, 301) for y in range(1, 301)}

def nine_total(x, y):
    return sum(grid[(x+i, y+j)] for i in range(3) for j in range(3))

top = max( ( (x,y) for x in range(1,299) for y in range(1,299) ),
    key=lambda c: nine_total(*c)
    )

print(top)