numCourses = 2
prerequisites = [[1,0],[0,1]]
visited = [0] * numCourses 
for a, b in prerequisites:
    if [b, a] in prerequisites:
        print(False)
        break
else:
    print(True)
