import constant
from circularPlate import circularPlate
from datetime import datetime

p2id = constant.person_id
ap_time = constant.appear_time

circle_ls = list()
c1 = color(255, 255, 255)

def setup():
    size(640, 640)
    background(0)
    noLoop()


        
def draw():
    all_line = list()
    # set white line
    stroke(c1)
    l_time = 0
    with open('hero.csv', 'r') as infile:
        data = infile.readlines()
    
    total_time = data[-1].split(',')[3]
    cp = circularPlate(canvas_size=(height, width), start_angle=0, total_time=total_time, person_nums=len(p2id))
    for dt in data:
        item = dt.split(',')
        b_time = str2time(item[2])
        e_time = str2time(item[3])

        l_time = e_time
        
        source = p2id[item[4]]
        source_pos = cp.getCoordinates(item[2], source)
        # print(b_time)
        if '+' in item[5]:
            targets = item[5].split('+')
            tgs = [p2id[t] for t in targets]
            for tg in tgs:
                tg_pos = cp.getCoordinates(item[3], tg)
                line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
                idx = len(all_line)
                print('{}--{}'.format(source, tg))
                all_line.append([source_pos, tg_pos, idx])
        else:
            tg = p2id[item[5]]
            tg_pos = cp.getCoordinates(item[3], tg)
            line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
            idx = len(all_line)
            print('{}--{}'.format(source, tg))
            all_line.append([source_pos, tg_pos, idx])


def mouseClicked(): 
    pass




def str2time(timestring):
    assert type(timestring) == str
    h = int(timestring[:2])
    m = int(timestring[2:4])
    s = int(timestring[4:])
    time = s + m * 60 + h * 3600
    return time
