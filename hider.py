import math
import random
class Hider:
    movement = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, -1]]
    a_coeff = 1.0
    b_coeff = 1.0
    c_coeff = 0.0
    hide_value = 0.6324
    vision_radius = 2

    def __init__(this, n_input, m_input, map_input, x, y):
        this.next_step=0
        this.seen=False
        this.pos = [x, y]
        this.anno = [0, 0]
        this.seeker_pos=[0,0]
        this.n = n_input
        this.m = m_input
        this.map = map_input
        this.visited = [[False for i in range(this.m)] for j in range(this.n)]
        for i in range(this.n):
            for j in range(this.m):
                if this.map[i][j] == 1:
                    this.visited[i][j] = True
                if this.map[i][j] == 3:
                    this.seeker_pos = [i, j]

    def look(this):
        this.seen = False
        if abs(this.pos[0]-this.seeker_pos[0])<=this.vision_radius and abs(this.pos[1]-this.seeker_pos[1])<=this.vision_radius and this.can_be_seen(this.pos[0],this.pos[1],this.seeker_pos[0],this.seeker_pos[1]):
            this.seen = True

    def cal_distance(this, x, y):
        return abs(float(this.a_coeff * x + this.b_coeff * y + this.c_coeff)) / math.sqrt(
            this.a_coeff ** 2 + this.b_coeff ** 2) if (
                    this.a_coeff != 0 or this.b_coeff != 0 and this.a_coeff != this.b_coeff) else 1.0

    def cal_line(this, hider_index):
        this.a_coeff = this.hider[hider_index].pos[1] - this.pos[1]
        this.b_coeff = this.pos[0] - this.hider[hider_index].pos[0]
        this.c_coeff = (this.a_coeff * this.pos[0] + this.b_coeff * this.pos[1]) * (-1)

    def cal_line_2(this, x1, y1, x2, y2):
        this.a_coeff = y2 - y1
        this.b_coeff = x1 - x2
        this.c_coeff = (this.a_coeff * x1 + this.b_coeff * y1) * (-1)

    def set_direction(this):
        this.next_step = -1  # reset first
        if this.seen:
            maxVal = 0
            for i in range(8):
                if this.pos[0] + this.movement[i][0] < 0 or this.pos[0] + this.movement[i][0] >= this.n or this.pos[1] + \
                        this.movement[i][1] < 0 or this.pos[1] + this.movement[i][1] >= this.m:
                    continue
                if this.pos[0] + this.movement[i][0] >= 0 and this.pos[1] + this.movement[i][1] >= 0 and this.pos[0] + \
                        this.movement[i][0] < this.n and this.pos[1] + this.movement[i][1] < this.m and \
                        this.map[this.pos[0] + this.movement[i][0]][this.pos[1] + this.movement[i][1]] != 1:
                    if this.a_heuristic(i, this.seeker_pos[0],
                                        this.seeker_pos[1]) > maxVal:
                        maxVal = this.a_heuristic(i, this.seeker_pos[0],
                                               this.seeker_pos[1])
                        this.next_step = i
        else:
            this.next_step=-1

    def a_heuristic(this, next_step, x, y):
        return max(abs(this.pos[0] + this.movement[next_step][0] - x),
                   abs(this.pos[1] + this.movement[next_step][1] - y))

    def can_be_seen(this, x1, y1, x2, y2):
        if x1 > x2:
            x_max = x1
            x_min = x2
        else:
            x_min = x1
            x_max = x2
        if y1 > y2:
            y_max = y1
            y_min = y2
        else:
            y_min = y1
            y_max = y2
        this.cal_line_2(x1, y1, x2, y2)
        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                if this.map[i][j] == 1 and this.cal_distance(i, j) < this.hide_value:
                    return False
        return True

    def move(this):
        if this.next_step!=-1:
            this.map[this.pos[0]][this.pos[1]] = 0
            this.pos[0] += this.movement[this.next_step][0]
            this.pos[1] += this.movement[this.next_step][1]
            this.map[this.pos[0]][this.pos[1]] = 2

    def announce(this,n,m):
        this.anno[0]=this.pos[0]+math.floor(random.uniform(-3,4))
        this.anno[1] = this.pos[1] + math.floor(random.uniform(-3, 4))
        if this.anno[0]<0:
            this.anno[0]=0
        elif this.anno[0]>=n:
            this.anno[0] = n-1
        if this.anno[1]<0:
            this.anno[1]=0
        elif this.anno[1]>=m:
            this.anno[1] = m-1
