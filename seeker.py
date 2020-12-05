import math
import Hider


class Seeker:
    seen = False
    next_step = 0
    movement = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, -1]]
    a_coeff = 1.0
    b_coeff = 1.0
    c_coeff = 0.0
    hide_value = 0.6324
    vision_radius = 3
    score = 100
    hider = []
    nearest_hider = 0
    anno_inteval = 5
    anno = False

    def __init__(this, n_input, m_input, map_input):
        this.n = n_input
        this.m = m_input
        this.map = map_input
        this.visited = [[False for i in range(this.m)] for j in range(this.n)]
        for i in range(this.n):
            for j in range(this.m):
                if this.map[i][j] == 1:
                    this.visited[i][j] = True
                if this.map[i][j] == 2:
                    this.hider.append(Hider.Hider(i, j))
                    # this.map[i][j] = 0
                if this.map[i][j] == 3:
                    this.pos = [i, j]
                    # this.map[i][j] = 0
        this.hider_seen = [False for i in range(len(this.hider))]
        this.hider_caught = [False for i in range(len(this.hider))]

    def look(this):
        if (101 - this.score) % this.anno_inteval == 0:
            this.anno = True
            for i in range(len(this.hider)):
                this.hider[i].announce(this.n, this.m)
        for i in range(len(this.hider)):
            if not this.hider_caught[i]:
                this.check_hider(i)
        this.seen = False
        for i in range(len(this.hider)):
            if not this.hider_caught[i] and this.hider_seen[i]:
                this.seen = True

    def check_hider(this, hider_index):
        if this.hider_seen[hider_index]:
            return
        if abs(this.pos[0] - this.hider[hider_index].pos[0]) > this.vision_radius or abs(
                this.pos[1] - this.hider[hider_index].pos[1]) > this.vision_radius:
            return
        if this.pos[0] > this.hider[hider_index].pos[0]:
            x_max = this.pos[0]
            x_min = this.hider[hider_index].pos[0]
        else:
            x_min = this.pos[0]
            x_max = this.hider[hider_index].pos[0]
        if this.pos[1] > this.hider[hider_index].pos[1]:
            y_max = this.pos[1]
            y_min = this.hider[hider_index].pos[1]
        else:
            y_min = this.pos[1]
            y_max = this.hider[hider_index].pos[1]
        this.cal_line(hider_index)
        this.hider_seen[hider_index] = True
        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                if this.map[i][j] == 1 and this.cal_distance(i, j) < this.hide_value:
                    this.hider_seen[hider_index] = False
                    return

    def cal_distance(this, x, y):
        return abs(this.a_coeff * x + this.b_coeff * y + this.c_coeff) / math.sqrt(
            this.a_coeff ** 2 + this.b_coeff ** 2) if this.a_coeff != 0 and this.b_coeff != 0 else 1

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
            min = max(this.n, this.m)
            for i in range(len(this.hider_seen)):
                if this.hider_seen[i] and not this.hider_caught[i]:
                    if max(abs(this.pos[0] - this.hider[i].pos[0]), abs(this.pos[1] - this.hider[i].pos[1])) < min:
                        min = max(abs(this.pos[0] - this.hider[i].pos[0]), abs(this.pos[1] - this.hider[i].pos[1]))
                        this.nearest_hider = i
            min = max(this.n, this.m)
            for i in range(8):
                if this.pos[0] + this.movement[i][0] < 0 or this.pos[0] + this.movement[i][0] >= this.n or this.pos[1] + \
                        this.movement[i][1] < 0 or this.pos[1] + this.movement[i][1] >= this.m:
                    continue
                if this.map[this.pos[0] + this.movement[i][0]][this.pos[1] + this.movement[i][1]] != 1:
                    if this.a_heuristic(i, this.hider[this.nearest_hider].pos[0],
                                        this.hider[this.nearest_hider].pos[1]) < min:
                        min = this.a_heuristic(i, this.hider[this.nearest_hider].pos[0],
                                               this.hider[this.nearest_hider].pos[1])
                        this.next_step = i
        elif this.anno:
            min = max(this.n, this.m)
            for i in range(len(this.hider)):
                if not this.hider_caught[i]:
                    if max(abs(this.pos[0] - this.hider[i].anno[0]), abs(this.pos[1] - this.hider[i].anno[1])) < min:
                        min = max(abs(this.pos[0] - this.hider[i].anno[0]), abs(this.pos[1] - this.hider[i].anno[1]))
                        this.nearest_hider = i
            min = max(this.n, this.m)
            for i in range(8):
                if this.pos[0] + this.movement[i][0] < 0 or this.pos[0] + this.movement[i][0] >= this.n or this.pos[1] + \
                        this.movement[i][1] < 0 or this.pos[1] + this.movement[i][1] >= this.m:
                    continue
                if this.map[this.pos[0] + this.movement[i][0]][this.pos[1] + this.movement[i][1]] != 1:
                    if this.a_heuristic(i, this.hider[this.nearest_hider].anno[0],
                                        this.hider[this.nearest_hider].anno[1]) < min:
                        min = this.a_heuristic(i, this.hider[this.nearest_hider].anno[0],
                                               this.hider[this.nearest_hider].anno[1])
                        this.next_step = i
        else:
            max_val = -1
            for i in range(8):
                if this.map[this.pos[0] + this.movement[i][0]][this.pos[1] + this.movement[i][1]] != 1:
                    if this.tai_heuristic(i) > max_val:
                        max_val = this.tai_heuristic(i)
                        this.next_step = i

    def a_heuristic(this, next_step, x, y):
        return max(abs(this.pos[0] + this.movement[next_step][0] - x),
                   abs(this.pos[1] + this.movement[next_step][1] - y))

    def tai_heuristic(this, next_step):
        count = 0
        for i in range(this.pos[0] + this.movement[next_step][0] - 3, this.pos[0] + this.movement[next_step][0] + 4):
            for j in range(this.pos[1] + this.movement[next_step][1] - 3,
                           this.pos[1] + this.movement[next_step][1] + 4):
                if i < 0 or j < 0 or i >= this.n or j >= this.m:
                    continue
                if not this.visited[i][j]:
                    if this.can_be_seen(this.pos[0] + this.movement[next_step][0],
                                        this.pos[1] + this.movement[next_step][1], i, j):
                        count += 1
        return count

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
                if this.map[i][j]==1 and this.cal_distance(i, j) < this.hide_value:
                    return False
        return True

    def catch(this):
        if this.pos[0] + this.movement[this.next_step][0] == this.hider[this.nearest_hider].pos[0] and this.pos[1] + \
                this.movement[this.next_step][1] == this.hider[this.nearest_hider].pos[1]:
            this.map[this.hider[this.nearest_hider].pos[0]][this.hider[this.nearest_hider].pos[1]] = 0
            return True

    def move(this):
        this.score -= 1
        if this.catch():
            this.hider_caught[this.nearest_hider] = True
            this.score += 20
        this.map[this.pos[0]][this.pos[1]] = 0
        this.pos[0] += this.movement[this.next_step][0]
        this.pos[1] += this.movement[this.next_step][1]
        this.map[this.pos[0]][this.pos[1]] = 3
        this.update_seen()

    def update_seen(this):
        for i in range(this.pos[0] - 3, this.pos[0] + 4):
            for j in range(this.pos[1] - 3, this.pos[1] + 4):
                if i < 0 or j < 0 or i >= this.n or j >= this.m:
                    continue
                if not this.visited[i][j]:
                    if this.can_be_seen(this.pos[0],this.pos[1],i,j):
                        this.visited[i][j]=True