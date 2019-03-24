class circularPlate(object):
    """
    This class creates a compass for the dialog records. Given a record, it returns the coordinates,
    of the start and end time points.
    """
    def __init__(self,canvas_size=(500,500),start_angle=0,total_time,person_nums):
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
        self.start_angle = start_angle # start point
        
        self.person_nums = person_nums # number of concentric circles
        self.radius_scale = self.getRadiusScale() # distance between circulars
        
        self.total_time = self.str2sec(total_time)
        self.angle_scale = self.getAngleScale() # degree per second.
        
    
    def getCenterCoords(self):
        """
        Return: center coordinates (x,y).
        NOTE: width relates to x, height relates to y.
        """
        return self.canvas_width/2, self.canvas_height/2
    
    def getRadiusScale(self):
        """
        distance between circulars.
        Note: leave margins on the canvas, thus set partitions to be person_nums+1.
        """
        return self.canvas_height/(person_nums+1) 
        
    
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
        pass 
        
        
    def drawCircular(self):
        # draw details for the circular
        pass
    
    def getCoordinates(self,timestamp,person_id):
        """
        Inputs: 
            timestamp: string, e.g. '001125' is 00:11:25.
            person_id: the id of the circular.
        Output: tuple of floats. (x,y)
        convert time string into seconds.
        """
        
        pass
        # return x,y
        
    
    
    
        
        
        
