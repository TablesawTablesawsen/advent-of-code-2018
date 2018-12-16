class Star(object):
    """docstring for Star"""
    def __init__(self, txt):
        self.x, self.y, self.vel_x, self.vel_y = tuple(int(x) for x in txt.split())


        
    def forward(self):
        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y

    def back(self):
        self.x = self.x - self.vel_x
        self.y = self.y - self.vel_y

def get_area(stars):
    x = max(star.x for star in stars) - min(star.x for star in stars) 
    y = max(star.y for star in stars) - min(star.y for star in stars) 
    return x * y

with open('input/day10.txt') as inp:
    stars = {Star(txt) for txt in inp}

last_area = sky_area = get_area(stars)
time = 0
while last_area >= sky_area:
    for star in stars:
        star.forward()
    last_area = sky_area
    sky_area = get_area(stars)
    time = time + 1

for star in stars:
    star.back()

locations = {(star.x, star.y) for star in stars}

def get_char(x, y):
    return '*' if (x, y) in locations else ' '

for y in range(min(star.y for star in stars), max(star.y for star in stars) + 1):
    row = ''.join(get_char(x, y) for x in range(
        min(star.x for star in stars), 
        max(star.x for star in stars) + 1
        ))
    print(row)
print(time)