import constant
from circularPlate import sectorPlate
import math
from datetime import datetime

p2id = constant.person_id
ap_time = constant.appear_time
female_list = constant.female_list
circle_ls = list()
c1 = color(255, 255, 255)
bs=[] # each episode is a branch, this is a global variable.
cir = []
def setup():
    size(800, 800)
    frameRate(24)
    background(0)
    global cir
    
    
    with open('hero.csv', 'r') as infile:
        data = infile.readlines()
    for dt in data:
        bs.append(Branch()) # initialize branches
        
    for img_ind in range(5,20):
        with open('hero.csv', 'r') as infile:
            data = infile.readlines()
        total_time = data[-1].split(',')[3]
        cp = sectorPlate(canvas_size=(height, width), total_time=total_time, person_nums=len(p2id))
        pg = createGraphics(800,800)
        pg.beginDraw()
        pg.background(0)
        # pg.colorMode(RGB)
        for ind,dt in enumerate(data):
            item = dt.split(',')
            b_time = str2time(item[2])
            e_time = str2time(item[3])
            l_time = e_time
            
            source = p2id[item[4]]
            source_pos = cp.getCoordinates(item[2], source)
            drawEllipseInGraphics(pg,source_pos[0],source_pos[1],source,opa=img_ind)
            
            # multiple targets
            if '+' in item[5]: 
                targets = item[5].split('+')
                tgs = [p2id[t] for t in targets]
                for tg in tgs:
                    tg_pos = cp.getCoordinates(item[3], tg)
                    drawEllipseInGraphics(pg,tg_pos[0], tg_pos[1],tg,opa=img_ind)
            else:
                tg = p2id[item[5]]
                tg_pos = cp.getCoordinates(item[3], tg)
                drawEllipseInGraphics(pg,tg_pos[0], tg_pos[1],tg,opa=img_ind)
                
        with open('hero_female.csv', 'r') as infile:
            data = infile.readlines()
    
        for ind,dt in enumerate(data):
            item = dt.split(',')
            b_time = str2time(item[2])
            e_time = str2time(item[3])
            l_time = e_time
            
            source = p2id[item[4]]
            source_pos = cp.getCoordinates(item[2], source)
            drawEllipseInGraphics(pg,source_pos[0],source_pos[1],source,ellipse_color='red',opa =img_ind)
    
            if '+' in item[5]:
                targets = item[5].split('+')
                tgs = [p2id[t] for t in targets]
                for tg in tgs:
                    tg_pos = cp.getCoordinates(item[3], tg)
                    drawEllipseInGraphics(pg,tg_pos[0], tg_pos[1],tg,ellipse_color='red',opa = img_ind)
            else:
                tg = p2id[item[5]]
                tg_pos = cp.getCoordinates(item[3], tg)
                drawEllipseInGraphics(pg,tg_pos[0], tg_pos[1],tg,ellipse_color='red',opa = img_ind)
        pg.filter(BLUR,1.0)
        
        with open('hero.csv', 'r') as infile:
            data = infile.readlines()
        # pg.stroke(0, 150, 255, 75)
        pg.noStroke()
        
        for ind,dt in enumerate(data):
            item = dt.split(',')
            b_time = str2time(item[2])
            e_time = str2time(item[3])
            l_time = e_time
            
            source = p2id[item[4]]
            source_pos = cp.getCoordinates(item[2], source)
            drawEllipseInGraphics(pg,source_pos[0],source_pos[1],source,5,opa=img_ind)
            
            # multiple targets
            if '+' in item[5]: 
                targets = item[5].split('+')
                tgs = [p2id[t] for t in targets]
                for tg in tgs:
                    tg_pos = cp.getCoordinates(item[3], tg)
                    drawEllipseInGraphics(pg,tg_pos[0], tg_pos[1],tg,5,opa=img_ind)
            else:
                tg = p2id[item[5]]
                tg_pos = cp.getCoordinates(item[3], tg)
                drawEllipseInGraphics(pg,tg_pos[0], tg_pos[1],tg,5,opa=img_ind)
                
        with open('hero_female.csv', 'r') as infile:
            data = infile.readlines()
        # pg.stroke(255, 79, 89, 65)  # red
        pg.noStroke()
        for ind,dt in enumerate(data):
            item = dt.split(',')
            b_time = str2time(item[2])
            e_time = str2time(item[3])
            l_time = e_time
            
            source = p2id[item[4]]
            source_pos = cp.getCoordinates(item[2], source)
            drawEllipseInGraphics(pg,source_pos[0],source_pos[1],source,5,ellipse_color='red',opa=img_ind)
    
            if '+' in item[5]:
                targets = item[5].split('+')
                tgs = [p2id[t] for t in targets]
                for tg in tgs:
                    tg_pos = cp.getCoordinates(item[3], tg)
                    drawEllipseInGraphics(pg,tg_pos[0], tg_pos[1],tg,5,ellipse_color='red',opa=img_ind)
            else:
                tg = p2id[item[5]]
                tg_pos = cp.getCoordinates(item[3], tg)
                drawEllipseInGraphics(pg,tg_pos[0], tg_pos[1],tg,5,ellipse_color='red',opa=img_ind)
        pg.endDraw()
        cir.append(pg.get())
    
    for img_ind in reversed(range(15)):
        cir.append(cir[img_ind])

    # with open('hero.csv', 'r') as infile:
    #     data = infile.readlines()
    # for dt in data:
    #     bs.append(Branch()) # initialize branches


def draw():

    background(0)
    # if frameCount==0:

    image(cir[frameCount%30],0,0)

    all_line = list()
    l_time = 0
    with open('hero.csv', 'r') as infile:
        data = infile.readlines()
    total_time = data[-1].split(',')[3]
    print len(p2id)

    cp = sectorPlate(canvas_size=(height, width), total_time=total_time, person_nums=len(p2id))
    stroke(0, 150, 255, 75) # blue, opacity=75%
    randomSeed(0)
     
    # draw male dialogs
    for ind,dt in enumerate(data):
        item = dt.split(',')
        b_time = str2time(item[2])
        e_time = str2time(item[3])
        l_time = e_time
        
        source = p2id[item[4]]
        source_pos = cp.getCoordinates(item[2], source)
        linewidth = ceil(int(item[1])/4.0) # propotional to dialog nums in each episode
        # multiple targets
        if '+' in item[5]: 
            targets = item[5].split('+')
            tgs = [p2id[t] for t in targets]
            for tg in tgs:
                tg_pos = cp.getCoordinates(item[3], tg)
                strokeWeight(linewidth)
                line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
                stroke(0, 150, 255, 95)
                ang = cp.getCurrentAngle(item[3]) # branches' directions
                ang = radians(ang)
                strokeWeight(1)
                idx = len(all_line) # record all lines for interaction
                all_line.append([source_pos, tg_pos, idx])
        else:
            tg = p2id[item[5]]
            tg_pos = cp.getCoordinates(item[3], tg)
            strokeWeight(linewidth)
            line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
            stroke(0, 150, 255, 95)
            strokeWeight(1)
            ang = cp.getCurrentAngle(item[3])
            ang = radians(ang)
            idx = len(all_line) # record all lines for interaction
            all_line.append([source_pos, tg_pos, idx])
        
        # draw branches
        pushMatrix()
        if tg_pos[1] > source_pos[1]:
            translate(source_pos[0], source_pos[1])
        else:
            translate(tg_pos[0], tg_pos[1])
        rotate(ang)    
        bs[ind].branch(linewidth=linewidth,freq=random(0,1),h=int(item[1])*6 ,r=2)
        popMatrix()
        strokeWeight(1)
        
    # draw female dialogs
    with open('hero_female.csv', 'r') as infile:
        data = infile.readlines()
    stroke(255, 79, 89, 65)  # red
    for ind,dt in enumerate(data):
        item = dt.split(',')
        b_time = str2time(item[2])
        e_time = str2time(item[3])
        l_time = e_time
        
        source = p2id[item[4]]
        source_pos = cp.getCoordinates(item[2], source)
        linewidth = round(int(item[1])/4.0)
        if '+' in item[5]:
            targets = item[5].split('+')
            tgs = [p2id[t] for t in targets]
            for tg in tgs:
                tg_pos = cp.getCoordinates(item[3], tg)
                strokeWeight(linewidth)
                line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
                ang = cp.getCurrentAngle(item[3])
                ang = radians(ang)
                strokeWeight(1)
                idx = len(all_line)
                all_line.append([source_pos, tg_pos, idx])
        else:
            tg = p2id[item[5]]
            tg_pos = cp.getCoordinates(item[3], tg)
            strokeWeight(linewidth)
            line(source_pos[0], source_pos[1], tg_pos[0], tg_pos[1])
            strokeWeight(1)
            ang = cp.getCurrentAngle(item[3])
            ang = radians(ang)
            idx = len(all_line)
            all_line.append([source_pos, tg_pos, idx])
        
        
        
    # draw sector background
    noFill()
    cp.drawSector()
    fill(255)
    # saveFrame("frames/tree-######.png")
    
def drawEllipseByID(x,y,id,ellipse_width=3.5):
    # noStroke()
    # fill(255, 130)
    strokeWeight(0)
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
    elif id == 0:
        fill(255)
        ellipse(x, y,ellipse_width,ellipse_width)
        fill(0, 175, 248, 65)
        ellipse(x, y, ellipse_width, ellipse_width)
        fill(255)
    else:   
        ellipse(x, y,ellipse_width,ellipse_width)
    strokeWeight(1)

def drawEllipseInGraphics(pg,x,y,id,ellipse_width=8,ellipse_color='blue',opa=0.5):
    # noStroke()
    # fill(255, 130)
    pg.strokeWeight(0)
    if id not in female_list:
        c = color(0,150,255,10*opa)
    else:
        c = color(255,79,89,10*opa)

    if id == 3: # qc
        pg.fill(c)
        pg.ellipse(x, y,ellipse_width*2, ellipse_width*2) # 2*3
        # pg.fill(bright)
    elif id == 16: # jd
        pg.fill(c)
        pg.ellipse(x, y, ellipse_width*2.2, ellipse_width*2.2)#2*6
        # pg.fill(bright)
    elif id == 17: # ssm
        pg.fill(c)
        pg.ellipse(x, y, ellipse_width*1.6,ellipse_width*1.6)
        # pg.fill(bright)
    elif id == 7: # xtj
        pg.fill(c)
        pg.ellipse(x, y, ellipse_width*1.2,ellipse_width*1.2)
        # pg.fill(bright)
    elif id == 0:
        pg.fill(c)
        pg.ellipse(x, y, ellipse_width, ellipse_width)
        # pg.fill(bright)
    else:   
        pg.fill(c)
        pg.ellipse(x, y,ellipse_width,ellipse_width)
        # pg.fill(255)
    pg.strokeWeight(1)

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
            ellipse(0, 0, 1, 1) # end point always white
            fill(255)
        self.num = self.num + 0.008


def str2time(timestring):
    assert type(timestring) == str
    h = int(timestring[:2])
    m = int(timestring[2:4])
    s = int(timestring[4:])
    time = s + m * 60 + h * 3600
    return time
