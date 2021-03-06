import constant
from circularPlate import sectorPlate
from movieProfile import movieProfile
import math
from datetime import datetime

bs = [] # each episode is a branch, this is a global variable.
ms =[]
cir = []
# background_color = 0
background_color = 35
# background_color = 65
# background_color = 255
fig_height = 600
fig_width = 600

draw_plain_line = False
draw_female_dialogs = False
draw_branches = False
draw_ellipse = False

# draw_color_line = False # always set as False
draw_color_sector = True
draw_motions = False

movie_name = 'the_golden_flower'
save_images = False

h_size = 6 # line width
freq_size = 1 # frequency scale

if movie_name == 'lovers':
    freq_file = 'lovers/lovers_freq.txt'
    file_name = 'lovers'

if movie_name == 'hero':
    freq_file = 'hero/hero_freq.txt'
    file_name = 'hero'

if movie_name == 'the_great_wall':
    freq_file = 'the_great_wall/the_great_wall_freq.txt'
    file_name = 'the_great_wall'

if movie_name == 'shadow':
    freq_file = 'shadow/shadow_freq.txt'
    file_name = 'shadow'
    
if movie_name == 'the_golden_flower':
    freq_file = 'the_golden_flower/the_golden_flower_freq.txt'
    file_name = 'the_golden_flower'

def setup():
    # fullScreen()
    size(fig_height,fig_width)
    frameRate(24)
    background(background_color)
    global cir
    global mp
    global ms
    global draw_female_dialogs
    
    if movie_name == 'hero':
         # Hero Color
        if draw_color_sector or draw_motions: 
            draw_female_dialogs = False
            mp = movieProfile(file_dir='hero/movie.csv',color_file_dir='hero/hero_color.txt',freq_file_dir = freq_file,female_names=['ry','fx'],character_size={'qc':2,'jd':2.2,'ssm':1.6,'xtj':1.2})
        # Hero female
        else:
            mp = movieProfile(file_dir='hero/movie.csv',female_file_dir='hero/movie_female.csv',freq_file_dir = freq_file,female_names=['ry','fx'],character_size={'qc':2,'jd':2.2,'ssm':1.6,'xtj':1.2})
    
    if movie_name == 'lovers':
        # Lovers color
        if draw_color_sector or draw_motions:
            draw_female_dialogs = False
            mp = movieProfile(file_dir='Lovers/movie.csv',color_file_dir='Lovers/lovers_color.txt',freq_file_dir = freq_file,female_names=['jn','am','xm','nx','dj'],character_size={'nx':1.2,'jn':1.5})
        # Lovers female
        else:
            mp = movieProfile(file_dir='Lovers/movie.csv',female_file_dir='Lovers/movie_female.csv',freq_file_dir = freq_file,female_names=['jn','am','xm','nx','dj'],character_size={'nx':1.2,'jn':1.5})

    if movie_name == 'the_great_wall':
        # the great wall color
        if draw_color_sector or draw_motions:
            draw_female_dialogs = False
            mp = movieProfile(file_dir='the_great_wall/movie.csv',color_file_dir='the_great_wall/the_great_wall_color.txt',freq_file_dir = freq_file,female_names=['ljj','hjjjjjjj'],character_size={'hjjjjjjj':1.5,'hj':1.5,'ljj':1.5,'xj':1.5,'yj':1.5})
        # the great wall
        else:
            mp = movieProfile(file_dir='the_great_wall/movie.csv',female_file_dir='the_great_wall/movie_female.csv',freq_file_dir = freq_file,female_names=['ljj','hjjjjjjj'],character_size={'hjjjjjjj':2,'hj':2,'lj':2,'xj':2,'yj':2})
    
    if movie_name == 'the_golden_flower':
        # the golden flower color
        if draw_color_sector or draw_motions:
            draw_female_dialogs = False
            mp = movieProfile(file_dir='the_golden_flower/movie.csv',color_file_dir='the_golden_flower/the_golden_flower_color.txt',freq_file_dir = freq_file,female_names=['wh','jc','gn','yxsm'],character_size={'bby':1.2,'gn':1.2,'ylj':2.2,'hjj':2})
        else:
            mp = movieProfile(file_dir='the_golden_flower/movie.csv',female_file_dir='the_golden_flower/movie_female.csv',freq_file_dir = freq_file,female_names=['wh','jc','gn','yxsm'],character_size={'bby':1.2,'gn':1.2,'ylj':2.2,'hjj':2})

    if movie_name == 'shadow':
        # shadow color
        if draw_color_sector or draw_motions:
            draw_female_dialogs = False
            mp = movieProfile(file_dir='shadow/movie.csv',color_file_dir='shadow/shadow_color.txt',freq_file_dir = freq_file,female_names=['qp','xa'],character_size={'tj':1.2,'dc':1.4,'sq':1.6,'sbm':1.8})
        else:
            mp = movieProfile(file_dir='shadow/movie.csv',female_file_dir='shadow/movie_female.csv',freq_file_dir = freq_file,female_names=['qp','xa'],character_size={'tj':1.2,'dc':1.4,'sq':1.6,'sbm':1.8})
   
   
    if draw_motions:
        for line_ind in range(mp.LINE_NUM):
            ms.append(motionSector(mp,line_ind)) # initialize motionSector
    if draw_branches:
        for _ in range(mp.LINE_NUM):
            bs.append(Branch()) # initialize branches
    for img_ind in range(5,20):
        pg = createGraphics(fig_height,fig_width)
        pg.beginDraw()
        pg.background(0,0,0,0)
        pg.colorMode(RGB)
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
            if draw_ellipse:
                drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),opa=img_ind,is_female=is_female)
            
            # target may contain multiple person
            for tar_ind in range(len(target_points)):
                target_x = target_points[tar_ind][0]
                target_y = target_points[tar_ind][1]
                target_id = target_ids[tar_ind]
                
                is_female = False
                if target_id in mp.female_list:
                    is_female = True
                if draw_ellipse:
                    drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),opa=img_ind,is_female=is_female)
                
        # female dialogs
        if draw_female_dialogs:
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
                if draw_ellipse:
                    drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),opa=img_ind,is_female=is_female)
                
                # target may contain multiple person
                for tar_ind in range(len(target_points)):
                    target_x = target_points[tar_ind][0]
                    target_y = target_points[tar_ind][1]
                    target_id = target_ids[tar_ind]
                    is_female = False
                    if target_id in mp.female_list:
                        is_female = True
                    if draw_ellipse:
                        drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),opa=img_ind,is_female=is_female)
                        
        pg.filter(BLUR,1.0)
        for line_ind in range(mp.LINE_NUM):
            # draw lines
            source_x, source_y = mp.source_points[line_ind]
            target_points = mp.target_points[line_ind]
            source_id = mp.source_ids[line_ind]
            target_ids = mp.target_ids[line_ind]
            dialog_num = mp.dialog_nums[line_ind]
            # if draw_color_line:
            #     points_list = mp.points_list[line_ind] # 1 or 2 elements
            #     colors = mp.colors[line_ind] 
            if draw_color_sector:
                points_sector = mp.points_sector[line_ind]
                colors_sector = mp.colors_sector[line_ind]
            
            is_female = False
            if source_id in mp.female_list:
                is_female = True
            if draw_ellipse:
                drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),4,opa=img_ind,is_female=is_female)
            
            # target may contain multiple person
            for tar_ind in range(len(target_points)):
                target_x = target_points[tar_ind][0]
                target_y = target_points[tar_ind][1]
                target_id = target_ids[tar_ind]
                is_female = False
                if target_id in mp.female_list:
                    is_female = True
                if draw_ellipse:
                    drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),4,opa=img_ind,is_female=is_female)
                
            linewidth = dialog_num/2.0 # propotional to dialog nums in each episode
            # draw lines
            # linewidth = ceil(dialog_num/4.0) # propotional to dialog nums in each episode
            if draw_plain_line:
                pg.strokeWeight(linewidth)
                pg.stroke(0, 150, 255, 95)
                # pg.stroke(255, 255,255, 95)
                pg.line(source_x, source_y, target_x, target_y)
            # if draw_color_line:
            #     drawColorLine(pg,points_list,colors,linewidth)
            if draw_color_sector:
                drawColorSector(pg,points_sector,colors_sector)
                
        # female dialogs
        if draw_female_dialogs:
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
                if draw_ellipse:
                    drawEllipseInGraphics(pg,source_x,source_y,mp.id2size(source_id),4,opa=img_ind,is_female=is_female)
                
                # target may contain multiple person
                for tar_ind in range(len(target_points)):
                    target_x = target_points[tar_ind][0]
                    target_y = target_points[tar_ind][1]
                    target_id = target_ids[tar_ind]
                    is_female = False
                    if target_id in mp.female_list:
                        is_female = True
                    if draw_ellipse:
                        drawEllipseInGraphics(pg,target_x,target_y,mp.id2size(target_id),4,opa=img_ind,is_female=is_female)
                    # draw lines
                    if draw_plain_line:
                        linewidth = dialog_num/2.0 # propotional to dialog nums in each episode
                        pg.strokeWeight(linewidth)
                        pg.stroke(255, 79, 89, 155)
                        pg.line(source_x, source_y, target_x, target_y)
                        
        
        pg.endDraw()
        cir.append(pg.get())
    
    for img_ind in reversed(range(15)):
        cir.append(cir[img_ind])

def draw():
    sector_time = mp.findSector(mouseX,mouseY)
    background(background_color)
    noFill()
    mp.drawSector()
    
    # draw motion sectors
    if draw_motions:
        gp = createGraphics(fig_height,fig_width)
        gp.beginDraw()
        gp.background(0,0,0,0)
        for line_ind in range(mp.LINE_NUM):
            ms[line_ind].drawSector(gp,frameCount)
        gp.endDraw()
        image(gp,0,0)
        
    image(cir[frameCount%30],0,0)
    
    if sector_time:
        sector_img = loadImage(file_name + "/images/"+file_name+"_"+str(sector_time)+".jpg")
        image(sector_img, mouseX, mouseY, 1.5*sector_img.width, 2*sector_img.height)
        
    
    # background(0,0,0,0)
    # line_ind = frameCount%mp.LINE_NUM
    # # draw lines
    # pg = createGraphics(800,800)
    # pg.beginDraw()
    # pg.background(0,0,0,0)
    # points_sector = mp.points_sector[line_ind]
    # colors_sector = mp.colors_sector[line_ind]
    # dialog_num = mp.dialog_nums[line_ind]
        
    # linewidth = dialog_num/2.0 # propotional to dialog nums in each episode
    # # draw lines
    # # linewidth = ceil(dialog_num/4.0) # propotional to dialog nums in each episode
    # drawColorSector(pg,points_sector,colors_sector)
    # pg.endDraw()
    # pg.save("frames/tree-"+str(frameCount)+".png")
    # image(pg,0,0)
                
    # draw branches
    if draw_branches:
        randomSeed(0)
        for line_ind in range(mp.LINE_NUM):
            if draw_color_sector or draw_motions:
                if not mp.colors_sector[line_ind]:
                    continue
                r,g,b = mp.colors_sector[line_ind][-1][-1]
            else:
                r,g,b = (0, 150, 255)
            branch_x, branch_y = mp.branch_points[line_ind]
            stroke(r,g,b, 50)
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
    # noFill()
    # mp.drawSector()
    # fill(255)
    if save_images:
        saveFrame("frames/tree-######.png")

def drawEllipseInGraphics(pg,x,y,ellipse_size=1,ellipse_width=6,opa=0.5,is_female=False):
    pg.strokeWeight(0)
    if not is_female:
        c = color(0,150,255,5*opa)
        # c = color(255,255,255,10*opa)
    else:
        c = color(255,79,89,5*opa)
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

class motionSector(object):
    def __init__(self,movie_profile,sector_ind):
        self.mp = movie_profile
        self.sid = sector_ind
        
        self.freq = self.mp.freqs[self.sid]

        self.duration = self.freq2dur()
        self.amplitude = self.freq2amp()
        
        # self.gp = []
        # self.buildGP()
    def drawSector(self,pg,frame_num):
        cur_dur = frame_num%self.duration 
        cur_radians = math.pi*2*float(cur_dur)/float(self.duration)
        
        data_line = mp.data[self.sid]
        data_line = data_line.split(',')
        start_time = data_line[2]
        end_time = data_line[3]
        start_sec = mp.plate.str2sec(start_time)
        end_sec = mp.plate.str2sec(end_time)
        source_id = mp.source_ids[self.sid]
        target_id = mp.target_ids[self.sid][-1]
        if source_id > target_id:
            temp_id = source_id
            source_id = target_id
            target_id = temp_id
        seg_points = []
        seg_colors = []
        for time_sec in range(start_sec,end_sec):
            colors = mp.palette_lists[time_sec]
            proportions = mp.proportion_lists[time_sec]
            time_str = mp.sec2str(time_sec)
            points = mp.plate.getCoordinatesByProportion([time_str, time_str], proportions, [[source_id,target_id]],self.amplitude,cur_radians)
            points = points[0]
            seg_points.append(points)
            seg_colors.append(colors)
        drawColorSector(pg,seg_points,seg_colors,linewidth=1)
        
        
    def buildGP(self):
        
        for ind_gp in range(self.duration):
            gp = createGraphics(fig_height,fig_width)
            gp.beginDraw()
            gp.background(0,0,0,0)
            cur_radians = math.pi*2*float(ind_gp)/float(self.duration)
            
            data_line = mp.data[self.sid]
            data_line = data_line.split(',')
            start_time = data_line[2]
            end_time = data_line[3]
            start_sec = mp.plate.str2sec(start_time)
            end_sec = mp.plate.str2sec(end_time)
            source_id = mp.source_ids[self.sid]
            target_id = mp.target_ids[self.sid][-1]
            if source_id > target_id:
                temp_id = source_id
                source_id = target_id
                target_id = temp_id
            seg_points = []
            seg_colors = []
            for time_sec in range(start_sec,end_sec):
                colors = mp.palette_lists[time_sec]
                proportions = mp.proportion_lists[time_sec]
                time_str = mp.sec2str(time_sec)
                points = mp.plate.getCoordinatesByProportion([time_str, time_str], proportions, [[source_id,target_id]],self.amplitude,cur_radians)
                points = points[0]
                seg_points.append(points)
                seg_colors.append(colors)

            drawColorSector(gp,seg_points,seg_colors,linewidth=1)
            gp.endDraw()
            self.gp.append(gp)
        
        
    def freq2dur(self):
        self.max_duration = 50 # slowest
        self.min_duration = 10 # fastest
        # freq = 1: 10 frames for one period
        # freq = 0: 50 frmaes for one period
        return int(self.max_duration - self.freq*(self.max_duration-self.min_duration))
        
    def freq2amp(self):
        return self.mp.plate.radius_scale
         
        
        
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
