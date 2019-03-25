import constant
from circularPlate import sectorPlate
import math

from datetime import datetime

p2id = constant.person_id
ap_time = constant.appear_time


circle_ls = list()
c1 = color(255, 255, 255)

def setup():
    size(800, 800)
    background(0)
    noLoop()


def draw():

    all_line = list()
    # set white line
    stroke(c1)
    stroke(0, 150, 255, 85)
    l_time = 0
    with open('hero.csv', 'r') as infile:
        data = infile.readlines()
    
    total_time = data[-1].split(',')[3]

    cp = sectorPlate(canvas_size=(height, width), total_time=total_time, person_nums=len(p2id))
    noFill()
    cp.drawSector()
    for dt in data:
        item = dt.split(',')
        b_time = str2time(item[2])
        e_time = str2time(item[3])

        l_time = e_time
        
        source = p2id[item[4]]
        source_pos = cp.getCoordinates(item[2], source)
        linewidth = 1#round(int(item[1])/3)
        if '+' in item[5]:
            targets = item[5].split('+')
            tgs = [p2id[t] for t in targets]
            for tg in tgs:
                tg_pos = cp.getCoordinates(item[3], tg)
                strokeWeight(linewidth)
                ellipse(tg_pos[0], tg_pos[1], linewidth,linewidth)
                line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
                ang = (tg_pos[1] - source_pos[1]) / (tg_pos[0] - source_pos[0])
                ang = radians(ang)
                strokeWeight(1)
                idx = len(all_line)
                all_line.append([source_pos, tg_pos, idx])
            ellipse(source_pos[0],source_pos[1], linewidth, linewidth)
        else:
            tg = p2id[item[5]]
            tg_pos = cp.getCoordinates(item[3], tg)
            strokeWeight(linewidth)
            ellipse(tg_pos[0], tg_pos[1], linewidth, linewidth)
            ellipse(source_pos[0],source_pos[1], linewidth, linewidth)
            line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
            ang = (tg_pos[1] - source_pos[1]) / (tg_pos[0] - source_pos[0])
            ang = radians(atan(ang))
            
            pushMatrix()
            if tg_pos[1] > source_pos[1]:
                translate(source_pos[0], source_pos[1])
            else:
                translate(tg_pos[0], tg_pos[1])
            rotate(ang)
            branch(20, int(item[1]))
            popMatrix()
            strokeWeight(1)
            idx = len(all_line)
            all_line.append([source_pos, tg_pos, idx])



def branch(h=20, r=1, ang=radians(12)):
    """
    h: tree height
    r: round number
    """
    h *= 0.8
    if r > 0:
        pushMatrix()
        rotate(ang)
        line(0, 0, 0, -h)
        translate(0, -h)
        branch(h, r-1, ang)
        popMatrix()
        
        pushMatrix()
        rotate(-ang)
        line(0, 0, 0, -h)
        translate(0, -h)
        branch(h, r-1, -ang)
        popMatrix()

def mouseClicked(): 
    pass




def str2time(timestring):
    assert type(timestring) == str
    h = int(timestring[:2])
    m = int(timestring[2:4])
    s = int(timestring[4:])
    time = s + m * 60 + h * 3600
    return time
