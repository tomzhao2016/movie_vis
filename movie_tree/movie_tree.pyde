import constant
from circularPlate import sectorPlate
import math
from datetime import datetime


p2id = constant.person_id
ap_time = constant.appear_time
circle_ls = list()
c1 = color(255, 255, 255)
bs=[]

def setup():
    size(800, 800)
    background(0)
    frameRate(24)
    with open('hero.csv', 'r') as infile:
        data = infile.readlines()
    for dt in data:
        bs.append(Branch())


def draw():

    background(0);
    all_line = list()
    # set white line
    # stroke(c1)
    l_time = 0
    with open('hero.csv', 'r') as infile:
        data = infile.readlines()
    total_time = data[-1].split(',')[3]

    cp = sectorPlate(canvas_size=(height, width), total_time=total_time, person_nums=len(p2id))
    stroke(0, 150, 255, 75)
    randomSeed(0)
    for ind,dt in enumerate(data):
        item = dt.split(',')
        b_time = str2time(item[2])
        e_time = str2time(item[3])

        l_time = e_time
        
        source = p2id[item[4]]
        source_pos = cp.getCoordinates(item[2], source)
        drawEllipseByID(source_pos[0],source_pos[1],source)
        linewidth = round(int(item[1])/3.0)
        ellipse_width = 3
        # print(item[1])
        if '+' in item[5]:
            targets = item[5].split('+')
            tgs = [p2id[t] for t in targets]
            for tg in tgs:
                tg_pos = cp.getCoordinates(item[3], tg)
                drawEllipseByID(tg_pos[0], tg_pos[1],tg)
                strokeWeight(linewidth)
                line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
                ang = (tg_pos[1] - source_pos[1]) / (tg_pos[0] - source_pos[0])
                ang = radians(ang)
                strokeWeight(1)
                idx = len(all_line)
                all_line.append([source_pos, tg_pos, idx])
        else:
            tg = p2id[item[5]]
            tg_pos = cp.getCoordinates(item[3], tg)
            drawEllipseByID(tg_pos[0], tg_pos[1],tg)
            # ellipse(tg_pos[0], tg_pos[1], ellipse_width, ellipse_width)
            strokeWeight(linewidth)
            line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
            strokeWeight(1)
            # ang = (tg_pos[1] - source_pos[1]) / (tg_pos[0] - source_pos[0])
            # ang = atan(ang)-math.pi/2.0
            ang = cp.getCurrentAngle(item[3])
            ang = radians(ang)
            
            pushMatrix()
            if tg_pos[1] > source_pos[1]:
                translate(source_pos[0], source_pos[1])
            else:
                translate(tg_pos[0], tg_pos[1])
            rotate(ang)
            
            bs[ind].branch(linewidth=linewidth,freq=random(0,1),h=int(item[1])*6 ,r=2)
            # bs[ind].branch(linewidth=linewidth)
            popMatrix()
            strokeWeight(1)
            idx = len(all_line)
            all_line.append([source_pos, tg_pos, idx])
            
    with open('hero_female.csv', 'r') as infile:
        data = infile.readlines()
    stroke(255, 79, 89, 65)
    for ind,dt in enumerate(data):
        item = dt.split(',')
        b_time = str2time(item[2])
        e_time = str2time(item[3])

        l_time = e_time
        
        source = p2id[item[4]]
        source_pos = cp.getCoordinates(item[2], source)
        drawEllipseByID(source_pos[0],source_pos[1],source)
        linewidth = round(int(item[1])/3.0)
        ellipse_width = 3
        # print(item[1])
        if '+' in item[5]:
            targets = item[5].split('+')
            tgs = [p2id[t] for t in targets]
            for tg in tgs:
                tg_pos = cp.getCoordinates(item[3], tg)
                drawEllipseByID(tg_pos[0], tg_pos[1],tg)
                strokeWeight(linewidth)
                line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
                ang = (tg_pos[1] - source_pos[1]) / (tg_pos[0] - source_pos[0])
                ang = radians(ang)
                strokeWeight(1)
                idx = len(all_line)
                all_line.append([source_pos, tg_pos, idx])
        else:
            tg = p2id[item[5]]
            
            tg_pos = cp.getCoordinates(item[3], tg)
            drawEllipseByID(tg_pos[0], tg_pos[1],tg)
            # ellipse(tg_pos[0], tg_pos[1], ellipse_width, ellipse_width)
            strokeWeight(linewidth)
            line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
            strokeWeight(1)
            # ang = (tg_pos[1] - source_pos[1]) / (tg_pos[0] - source_pos[0])
            # ang = atan(ang)-math.pi/2.0
            ang = cp.getCurrentAngle(item[3])
            ang = radians(ang)
            
            pushMatrix()
            if tg_pos[1] > source_pos[1]:
                translate(source_pos[0], source_pos[1])
            else:
                translate(tg_pos[0], tg_pos[1])
            rotate(ang)
            fill(255, 79, 89)
            stroke(255, 79, 89)
            bs[ind].branch(linewidth=linewidth,freq=6,h=int(item[1])*6 ,r=2)
            fill(255)
            # bs[ind].branch(linewidth=linewidth)
            popMatrix()
            strokeWeight(1)
            idx = len(all_line)
            all_line.append([source_pos, tg_pos, idx])
    noFill()
    cp.drawSector()
    fill(255)


    
def mousePressed():
    save("movie_tree.gif")
    
def drawEllipseByID(x,y,id,ellipse_width=2):
    
    if id == 3: # qc
        ellipse(x, y,ellipse_width*2, ellipse_width*2) # 2*3
    elif id == 16: # jd
        fill(255)
        ellipse(x, y, ellipse_width*3, ellipse_width*3)
        fill(0, 175, 248, 65)
        ellipse(x, y, ellipse_width*3, ellipse_width*3)#2*6
        fill(255)
    elif id == 17: # ssm
        ellipse(x, y, ellipse_width*1.6,ellipse_width*1.6)
    elif id == 7: # xtj
        ellipse(x, y, ellipse_width*1.2,ellipse_width*1.2)
    else:   
        ellipse(x, y,ellipse_width,ellipse_width)

class Branch(object):
    def __init__(self):
        self.num = 0

        
    def branch(self,linewidth,freq=None,h=40, r=4):
        """
        h: tree height
        r: round number
        """
        h = h*0.5
        if not freq:
            freq=1
        theta = sin(20+self.num*freq) * 3
        linewidth = round(linewidth/2)
        if h > 2:
            pushMatrix()
            rotate(radians(-20+theta))
            strokeWeight(linewidth)
            line(0, 0, 0, -h)
            ellipse(0, -h, 1, 1)
            translate(0, -h)
            self.branch(linewidth,freq,h,r-1)
            popMatrix()
            
            pushMatrix()
            rotate(radians(20-theta))
            strokeWeight(linewidth)
            line(0, 0, 0, -h)
            ellipse(0, -h, 1, 1)
            translate(0, -h)
            self.branch(linewidth,freq,h, r-1)
            popMatrix()
        else:
            fill(255)
            ellipse(0, 0, 2, 2)
            fill(255)
        self.num = self.num + 0.008
        
    


# def branch(h=20, r=3, ang=radians(12)):
#     """
#     h: tree height
#     r: round number
#     """
#     h *= 0.8
#     if r > 0:
#         pushMatrix()
#         rotate(ang)
#         line(0, 0, 0, -h)
#         ellipse(0, -h, 1, 1)
#         translate(0, -h)
#         branch(h, r-1, ang)
#         popMatrix()
        
#         pushMatrix()
#         rotate(-ang)
#         line(0, 0, 0, -h)
#         ellipse(0, -h, 1, 1)
#         translate(0, -h)
#         branch(h, r-1, -ang)
#         popMatrix()



def str2time(timestring):
    assert type(timestring) == str
    h = int(timestring[:2])
    m = int(timestring[2:4])
    s = int(timestring[4:])
    time = s + m * 60 + h * 3600
    return time
