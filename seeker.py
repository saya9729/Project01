import brain
import main
import math
import random

class seeker:
    dead = False
    caught = False
    best = False
    vision = []
    fitness = 0
    decision = []
    step_to_go = 100
    next_step = 0
    movement = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, -1]]
    a_coeff = 0.0
    b_coeff = 0.0
    c_coeff = 0.0
    hide_value = 0.6324

    def __init__(this, x, y):
        for i in range(main.n):
            for j in range(main.m):
                if main.map[i][j] == 2:
                    this.hider_loc = [i, j]
                    this.vision.append(0)
                else:
                    this.vision.append(main.map[i][j])
                if main.map[i][j] == 3:
                    this.seeker_loc = [x, y]

        this.Brain = brain.neural_network(main.m*main.n, 25, 8)
        this.step_to_go = 100

    def mutate(this,rate):
        this.Brain.mutate(rate)

    def set_direction(this):
        this.decision = this.Brain.output(this.vision)

        max = 0
        this.next_step = 0
        for i in range(len(this.decision)):
            if max < this.decision[i]:
                max = this.decision[i]
                this.next_step = i

    def suicide(this, next_step):
        if this.seeker_loc[0] + this.movement[next_step][0] < 0 or this.seeker_loc[0] + this.movement[next_step][
            0] >= main.n or this.seeker_loc[1] + this.movement[next_step][1] < 0 or this.seeker_loc[1] + \
                this.movement[next_step][1] >= main.m:
            return True
        if main.map[this.seeker_loc[0] + this.movement[next_step][0]][
            this.seeker_loc[1] + this.movement[next_step][1]] == 1:
            return True

    def catch(this, next_step):
        if main.map[this.seeker_loc[0] + this.movement[next_step][0]][
                this.seeker_loc[1] + this.movement[next_step][1]] == 3:
            return True

    def move(this):
        this.step_to_go -= 1
        if this.step_to_go < 0:
            this.dead = True
        if this.suicide(this.next_step):
            this.dead = True
        if this.catch(this.next_step):
            this.caught = True
            this.dead=True

    def look(this):
        if abs(this.seeker_loc[0] - this.hider_loc[0]) > main.vision_radius or abs(this.seeker_loc[1] - this.hider_loc[1]) > main.vision_radius:
            return
        if this.seeker_loc[0] > this.hider_loc[0]:
            x_max = this.seeker_loc[0]
            x_min = this.hider_loc[0]
        else:
            x_min = this.seeker_loc[0]
            x_max = this.hider_loc[0]
        if this.seeker_loc[1] > this.hider_loc[1]:
            y_max = this.seeker_loc[1]
            y_min = this.hider_loc[1]
        else:
            y_min = this.seeker_loc[1]
            y_max = this.hider_loc[1]
        this.cal_line()
        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                if this.cal_distance(i, j) < this.hide_value:
                    return
        this.update_vision()

    def cal_line(this):
        this.a_coeff = this.hider_loc[1] - this.seeker_loc[1]
        this.b_coeff = this.seeker_loc[0] - this.hider_loc[0]
        this.c_coeff = this.a_coeff * this.seeker_loc[0] + this.b_coeff * this.seeker_loc[1]

    def cal_distance(this, x, y):
        return abs(this.a_coeff * x + this.b_coeff * y + this.c_coeff) / math.sqrt(
            this.a_coeff ** 2 + this.b_coeff ** 2)

    def update_vision(this):
        this.vision[this.hider_loc[0] * main.m + this.hider_loc[1]] = 2
        if this.step_to_go%main.hint_interval==0:
            hint_loc=[this.hider_loc[0]+math.floor(random.uniform(0,main.hint_radius)),this.hider_loc[1]+math.floor(random.uniform(0,main.hint_radius))]
            if hint_loc[0]<0:
                hint_loc[0]=0
            if hint_loc[0]>=main.n:
                hint_loc[0]=main.n
            if hint_loc[1]<0:
                hint_loc[1]=0
            if hint_loc[1]>=main.m:
                hint_loc[1]=main.m
            this.vision[hint_loc[0] * main.m + hint_loc[1]] = 4
    def cal_fitness(this):
        return this.step_to_go+20 if this.caught else 0

    def save_seeker(this, seeker_id,score,pop_id):
        file=open("data/seeker_no_"+seeker_id+".txt","w")
        print(score,pop_id,file=file)
        #later lol :v