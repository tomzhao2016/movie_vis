import math

class circularPlate(object):
    """
    This class creates a compass for the dialog records. Given a record, it returns the coordinates,
    of the start and end time points.
    """
    def __init__(self,total_time,person_nums,canvas_size=(500,500),start_angle=0):
        """
        initial inputs:
            canvas_size: tuple of integers (height,width). assert height==width.
            start_angle: integer scalar(default 0), the angle of start time. Range: (0,360).
            total_time: string, for example, '013007' is 01:30:07.
            person_nums: integer scalar, number of circulars.
        """
        # circularPlate basic properties
        self.canvas_size = canvas_size
        self.canvas_height, self.canvas_width = canvas_size
        self.center_x,self.center_y = self.getCenterCoords() # center
        self.start_angle = start_angle # w.r.t. the 12 o'clock pointer in the circular
        
        self.person_nums = person_nums # number of concentric circles
        self.radius_scale = self.getRadiusScale() # distance between circulars
        
        self.total_time = self.str2sec(total_time)
        self.angle_scale = self.getAngleScale() # degree per second.
        
    
    def getCenterCoords(self):
        """
        Return: center coordinates (x,y).
        NOTE: width relates to x, height relates to y.
        The top left point is (0,0).
        """
        return self.canvas_width/2, self.canvas_height/2
    
    def getRadiusScale(self):
        """
        distance between circulars.
        Note: leave margins on the canvas, thus set partitions to be person_nums+1.
        """
        return self.center_x/(self.person_nums+1)

    def getAngleScale(self):
        """
        degree per second.
        """
        return 360.0/self.total_time
        
    
    def str2sec(self,time):
        """
        Input: string.
        Output: Integer.
        convert time string into seconds.
        """
        return int(time[:2])*3600+int(time[2:4])*60+int(time[4:6])
        
        
    def drawCircular(self):
        # draw details for the circular
        pass
    
    def getCoordinates(self,timestamp,person_id):
        """
        Find x,y in polar coordinates.
        Inputs: 
            timestamp: string, e.g. '001125' is 00:11:25.
            person_id: the id of the circular.
        Output: tuple of floats. (x,y)
        convert time string into seconds.
        """
        timestamp = self.str2sec(timestamp)
        current_angle = self.start_angle + self.angle_scale*timestamp
        polar_angle = 2.5*180.0-current_angle-self.start_angle
        current_radius = (person_id+1)*self.radius_scale
        y = current_radius*math.sin(polar_angle/180*math.pi)
        x = current_radius*math.cos(polar_angle/180*math.pi)
        return x+self.center_x, self.center_y - y
        
    
class sectorPlate(object):
    def __init__(self,total_time,person_nums,sector_range = 160,canvas_size=(500,500)):
        self.canvas_size = canvas_size
        self.canvas_height, self.canvas_width = canvas_size

        self.sector_range = sector_range
        self.center_x, self.center_y = self.getSectorCenterCoords()

        self.person_nums = person_nums  # number of concentric circles
        self.radius_scale = self.getRadiusScale()

        self.start_angle = -sector_range/2
        self.end_angle = sector_range/2

        self.total_time = self.str2sec(total_time)
        self.angle_scale = self.getAngleScale()

    def getSectorCenterCoords(self):
        return self.canvas_width/2,self.canvas_height*(2.0/3.0)

    def getAngleScale(self):
        return self.sector_range/float(self.total_time)

    def getRadiusScale(self):
        """
        distance between circulars.
        Note: leave margins on the canvas, thus set partitions to be person_nums+1.
        """
        return self.center_x / (self.person_nums + 1 + 3)

    def str2sec(self, time):
        """
        Input: string.
        Output: Integer.
        convert time string into seconds.
        """
        return int(time[:2]) * 3600 + int(time[2:4]) * 60 + int(time[4:6])

    def getCoordinates(self,timestamp,person_id):
        """
        Find x,y in polar coordinates.
        Inputs:
            timestamp: string, e.g. '001125' is 00:11:25.
            person_id: the id of the circular.
        Output: tuple of floats. (x,y)
        convert time string into seconds.
        """
        timestamp = self.str2sec(timestamp)
        current_angle = self.start_angle + self.angle_scale*timestamp
        polar_angle = 90-current_angle
        current_radius = (person_id+1+3)*self.radius_scale
        y = current_radius*math.sin(polar_angle/180*math.pi)
        x = current_radius*math.cos(polar_angle/180*math.pi)
        return x+self.center_x, self.center_y - y

    def drawSector(self):
        stroke(255,255,255,50)
        start_angle = -(180-(180-self.sector_range)/2.0)/180.0*math.pi
        end_angle = -(180-self.sector_range)/2.0/180.0*math.pi
        for i in range(self.person_nums):
            arc(self.center_x, self.center_y, (i+1+3)*self.radius_scale*2, (i+1+3)*self.radius_scale*2,
                start_angle, end_angle)
        stroke(0, 150, 255, 85)






        
        
        
