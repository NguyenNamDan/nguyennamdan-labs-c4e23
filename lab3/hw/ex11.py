def is_inside(x, y):
    if (x[0]>y[0]) and (x[0]<y[0]+y[2]) and (x[1]>y[1]) and (x[1]<y[1]+y[3]) :
        return True
    else:
        return False
inside = is_inside([200, 120], [140, 60, 100, 200])
print(inside) 