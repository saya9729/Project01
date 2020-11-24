




# input data-------------------------
file = open("map1.txt", "r")
line = file.readlines()
n = int(line[0].split()[0])
m = int(line[0].split()[1])
map = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        map[i][j] = int(line[i + 1].split()[j])


