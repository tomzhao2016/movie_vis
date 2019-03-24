import constant

p2id = constant.person_id
ap_time = constant.appear_time

circle_ls = list()
c1 = color(255, 255, 255)

def setup():
    size(640, 640)
    background(0)
    # noLoop()

with open('./hero.csv', 'r') as infile:
    lines = infile.readlines()
        
def draw():
    stroke(c1)
    line(30, 20, 85, 75)
