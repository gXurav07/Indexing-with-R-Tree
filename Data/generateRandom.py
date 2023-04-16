import random 
dimension = 128
count = 1000

points = []

for i in range(count):
    points.append([random.random() for i in range(dimension)])
    # print(points[i])

