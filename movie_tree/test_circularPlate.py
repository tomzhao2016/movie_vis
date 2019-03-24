from circularPlate import circularPlate
cp = circularPlate(canvas_size=(500,500),start_angle=0,total_time='013000',person_nums=10)
x,y = cp.getCoordinates('004500',9)
print(cp.radius_scale)
print(x,y)
