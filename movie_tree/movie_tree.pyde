import constant
from circularPlate import sectorPlate
from movieProfile import movieProfile
import math
from datetime import datetime

bs = [] # each episode is a branch, this is a global variable.
cir = []
background_color = 0
# Hero
h_size = 6
freq_size = 1
freq_file = 'hero/hero_freq.txt'

# Lovers
# h_size = 3
# freq_size = 0.2

def setup():
    size(800, 800)
    frameRate(24)
    background(background_color)
    global cir
    global mp
     
    draw_plain_line = False
    draw_color_line = False
    draw_color_sector = True
    
    # Hero female
    # mp = movieProfile(file_dir='hero/hero.csv',female_file_dir='hero/hero_female.csv',female_names=['ry','fx'],character_size={'qc':2,'jd':2.2,'ssm':1.6,'xtj':1.2})
    # Hero Color
    mp = movieProfile(file_dir='hero/hero.csv',color_file_dir='hero/hero_color.txt',freq_file_dir = freq_file,female_names=['ry','fx'],character_size={'qc':2,'jd':2.2,'ssm':1.6,'xtj':1.2})
    
    # Lovers female
    # mp = movieProfile(file_dir='Lovers/movie.csv',female_file_dir='Lovers/movie_female.csv',female_names=['jn','am','xm','nx','dj'],character_size={'nx':1.2,'jn':1.5})
    # Lovers color
    # mp = movieProfile(file_dir='Lovers/movie.csv',color_file_dir='Lovers/lovers_color.txt',female_names=['jn','am','xm','nx','dj'],character_size={'nx':1.2,'jn':1.5})

    for _ in range(mp.LINE_NUM):
        bs.append(Branch()) # initialize branches
    
    for img_ind in range(5,20):
        pg = createGraphics(800,800)
        pg.beginDraw()
        pg.background(background_color)
        pg.colorMode(RGB)
        # all dialogs
        for line_ind in range(mp.LINE_NUM):
            # draw lines
            source_x, source_y = mp.source_points[line_ind]
            target_points = mp.target_points[line_ind]
            source_id = mp.source_ids[line_ind]
            target_ids = mp.target_ids[line_ind]
            dialog_num = mp.dialog_nums[line_ind]
            # if draw_color_sector:
            #     points_sector = mp.points_sector[line_ind]
            #     colors_sector = mp.colors_sector[line_ind]
            
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
                if draw_plain_line:
                    pg.stroke(0, 150, 255, 95)
                    pg.line(source_x, source_y, target_x, target_y)
                # if draw_color_sector:
                #     drawColorSector(pg,points_sector,colors_sector)
                
        # female dialogs
        if draw_plain_line:
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
            if draw_color_line:
                points_list = mp.points_list[line_ind] # 1 or 2 elements
                colors = mp.colors[line_ind] 
            if draw_color_sector:
                points_sector = mp.points_sector[line_ind]
                colors_sector = mp.colors_sector[line_ind]
            
            is_female = False
            if source_id in mp.female_list:
                is_female = True
            drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),2,opa=img_ind,is_female=is_female)
            
            # target may contain multiple person
            for tar_ind in range(len(target_points)):
                target_x = target_points[tar_ind][0]
                target_y = target_points[tar_ind][1]
                target_id = target_ids[tar_ind]
                is_female = False
                if target_id in mp.female_list:
                    is_female = True
                drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),2,opa=img_ind,is_female=is_female)
                
            linewidth = dialog_num/2.0 # propotional to dialog nums in each episode
            if draw_color_line:
                drawColorLine(pg,points_list,colors,linewidth)
            if draw_color_sector:
                drawColorSector(pg,points_sector,colors_sector)
        # female dialogs
        if draw_plain_line:
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

    background(background_color)

    image(cir[frameCount%30],0,0)
    randomSeed(0)
    
    # draw branches
    
    for line_ind in range(mp.LINE_NUM):
        if not mp.colors_sector[line_ind]:
            continue
        r,g,b = mp.colors_sector[line_ind][-1][-1]
        stroke(r,g,b,50)
        branch_x, branch_y = mp.branch_points[line_ind]
        ang = mp.branch_angs[line_ind]
        dialog_num = mp.dialog_nums[line_ind]
        linewidth = ceil(dialog_num/4.0)
        pushMatrix()
        translate(branch_x, branch_y)
        rotate(ang)  
        if freq_file:  
            bs[line_ind].branch(linewidth=linewidth,freq=mp.freqs[line_ind]*freq_size,h=dialog_num*h_size)
        else:
            bs[line_ind].branch(linewidth=linewidth,freq=random(0,1)*freq_size,h=dialog_num*h_size)

        popMatrix()
        strokeWeight(1)
        
    # draw sector background
    noFill()
    mp.drawSector()
    fill(255)
    # saveFrame("frames/tree-######.png")

def drawEllipseInGraphics(pg,x,y,ellipse_size=1,ellipse_width=6,opa=0.5,is_female=False):
    pg.strokeWeight(0)
    if not is_female:
        c = color(0,150,255,20*opa)
        # c = color(255,255,255,10*opa)
    else:
        c = color(255,79,89,20*opa)
        # c = color(255,255,255,10*opa)
    pg.fill(c)
    pg.noStroke()
    pg.ellipse(x, y,ellipse_width*ellipse_size, ellipse_width*ellipse_size) # 2*3
    pg.strokeWeight(1)

def drawColorLine(pg,points,colors,linewidth):
    for line_ind in range(len(colors)):
        seg_color = colors[line_ind]
        r,g,b = seg_color
        for seg_point in points:
            source_x,source_y,target_x,target_y = seg_point[line_ind]
            # pg.noTint()
            pg.stroke(r,g,b)
            pg.fill(r,g,b)
            pg.strokeWeight(linewidth)
            pg.line(source_x, source_y, target_x, target_y)
            # pg.stroke(r, g, b)
            
def drawColorSector(pg,points,colors,linewidth=1):
    for seg_points,seg_colors in zip(points,colors):
        for seg_point,seg_color in zip(seg_points,seg_colors):
            r,g,b = seg_color
            source_x,source_y,target_x,target_y = seg_point
            pg.stroke(r,g,b)
            pg.fill(r,g,b)
            pg.strokeWeight(linewidth)
            pg.line(source_x, source_y, target_x, target_y)
            
            
    

    
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
