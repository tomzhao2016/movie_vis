import constant
from circularPlate import sectorPlate
from movieProfile import movieProfile
import math
from datetime import datetime

bs = [] # each episode is a branch, this is a global variable.
cir = []

# Hero
#  h_size = 6
# freq_size = 1

# Lovers
h_size = 3
freq_size = 0.2

def setup():
    size(800, 800)
    frameRate(24)
    background(0)
    global cir
    global mp
    draw_color_line = False
    
    # Hero
    # mp = movieProfile(file_dir='hero/hero.csv',female_file_dir='hero/hero_female.csv',female_names=['ry','fx'],character_size={'qc':2,'jd':2.2,'ssm':1.6,'xtj':1.2})
    
    # Lovers
    mp = movieProfile(file_dir='Lovers/movie.csv',female_file_dir='Lovers/movie_female.csv',female_names=['jn','am','xm','nx','dj'],character_size={'nx':1.2,'jn':1.5})

    for _ in range(mp.LINE_NUM):
        bs.append(Branch()) # initialize branches
    
    for img_ind in range(5,20):
        pg = createGraphics(800,800)
        pg.beginDraw()
        pg.background(0)
        # all dialogs
        for line_ind in range(mp.LINE_NUM):
            # draw lines
            source_x, source_y = mp.source_points[line_ind]
            target_points = mp.target_points[line_ind]
            source_id = mp.source_ids[line_ind]
            target_ids = mp.target_ids[line_ind]
            dialog_num = mp.dialog_nums[line_ind]
            is_female = False
            if source_id in mp.female_list:
                is_female = True
            drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),opa=img_ind,is_female=is_female)
            
            # target may contain multiple person
            for tar_ind in range(len(target_points)):
                target_x = target_points[tar_ind][0]
                target_y = target_points[tar_ind][1]
                target_id = target_ids[tar_ind]
                is_female = False
                if target_id in mp.female_list:
                    is_female = True
                drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),opa=img_ind,is_female=is_female)
                
                # draw lines
                linewidth = ceil(dialog_num/4.0) # propotional to dialog nums in each episode
                strokeWeight(linewidth)
                pg.stroke(0, 150, 255, 95)
                if not draw_color_line:
                    pg.line(source_x, source_y, target_x, target_y)
                else:
                    drawColorLine()
                
        # female dialogs
        if not draw_color_line:
            for line_ind in range(mp.FEMALE_LINE_NUM):
                # draw lines
                source_x, source_y = mp.female_source_points[line_ind]
                target_points = mp.female_target_points[line_ind]
                source_id = mp.female_source_ids[line_ind]
                target_ids = mp.female_target_ids[line_ind]
                dialog_num = mp.female_dialog_nums[line_ind]
                is_female = False
                if source_id in mp.female_list:
                    is_female = True
                drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),opa=img_ind,is_female=is_female)
                
                # target may contain multiple person
                for tar_ind in range(len(target_points)):
                    target_x = target_points[tar_ind][0]
                    target_y = target_points[tar_ind][1]
                    target_id = target_ids[tar_ind]
                    is_female = False
                    if target_id in mp.female_list:
                        is_female = True
                    drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),opa=img_ind,is_female=is_female)
                    
                    # draw lines
                    linewidth = ceil(dialog_num/4.0) # propotional to dialog nums in each episode
                    strokeWeight(linewidth)
                    pg.stroke(255, 79, 89, 65)
                    pg.line(source_x, source_y, target_x, target_y)
                        
        pg.filter(BLUR,1.0)
        for line_ind in range(mp.LINE_NUM):
            # draw lines
            source_x, source_y = mp.source_points[line_ind]
            target_points = mp.target_points[line_ind]
            source_id = mp.source_ids[line_ind]
            target_ids = mp.target_ids[line_ind]
            dialog_num = mp.dialog_nums[line_ind]
            is_female = False
            if source_id in mp.female_list:
                is_female = True
            drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),5,opa=img_ind,is_female=is_female)
            
            # target may contain multiple person
            for tar_ind in range(len(target_points)):
                target_x = target_points[tar_ind][0]
                target_y = target_points[tar_ind][1]
                target_id = target_ids[tar_ind]
                is_female = False
                if target_id in mp.female_list:
                    is_female = True
                drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),5,opa=img_ind,is_female=is_female)
                
        # female dialogs
        if not draw_color_line:
            for line_ind in range(mp.FEMALE_LINE_NUM):
                # draw lines
                source_x, source_y = mp.female_source_points[line_ind]
                target_points = mp.female_target_points[line_ind]
                source_id = mp.female_source_ids[line_ind]
                target_ids = mp.female_target_ids[line_ind]
                dialog_num = mp.female_dialog_nums[line_ind]
                is_female = False
                if source_id in mp.female_list:
                    is_female = True
                drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),5,opa=img_ind,is_female=is_female)
                
                # target may contain multiple person
                for tar_ind in range(len(target_points)):
                    target_x = target_points[tar_ind][0]
                    target_y = target_points[tar_ind][1]
                    target_id = target_ids[tar_ind]
                    is_female = False
                    if target_id in mp.female_list:
                        is_female = True
                    drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),5,opa=img_ind,is_female=is_female)
        
        pg.endDraw()
        cir.append(pg.get())
    
    for img_ind in reversed(range(15)):
        cir.append(cir[img_ind])

def draw():

    background(0)
    # if frameCount==0:

    image(cir[frameCount%30],0,0)
    randomSeed(0)
    
    # draw branches
    for line_ind in range(mp.LINE_NUM):
        branch_x, branch_y = mp.branch_points[line_ind]
        ang = mp.branch_angs[line_ind]
        dialog_num = mp.dialog_nums[line_ind]
        linewidth = ceil(dialog_num/4.0)
        pushMatrix()
        translate(branch_x, branch_y)
        rotate(ang)    
        bs[line_ind].branch(linewidth=linewidth,freq=random(0,1)*freq_size,h=dialog_num*h_size)
        popMatrix()
        strokeWeight(1)
        
    # draw sector background
    noFill()
    mp.drawSector()
    fill(255)
    # saveFrame("frames/tree-######.png")

def drawEllipseInGraphics(pg,x,y,ellipse_size=1,ellipse_width=8,opa=0.5,is_female=False):
    pg.strokeWeight(0)
    if not is_female:
        c = color(0,150,255,10*opa)
    else:
        c = color(255,79,89,10*opa)
    pg.fill(c)
    pg.ellipse(x, y,ellipse_width*ellipse_size, ellipse_width*ellipse_size) # 2*3
    pg.strokeWeight(1)

def drawColorLine():
    pass
    
class Branch(object):
    def __init__(self):
        self.num = 0

    def branch(self,linewidth,freq=None,h=40):
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
            self.branch(linewidth,freq,h)
            popMatrix()
            
            pushMatrix()
            rotate(radians(20-theta))
            strokeWeight(linewidth)
            line(0, 0, 0, -h)
            ellipse(0, -h, 1, 1)
            translate(0, -h)
            self.branch(linewidth,freq,h)
            popMatrix()
        else:
            fill(255)
            ellipse(0, 0, 1, 1) # end point always white
            fill(255)
        self.num = self.num + 0.008
